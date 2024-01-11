import math
from http import HTTPStatus
from logger import get_logger

import requests as requests
from flask import Blueprint, request
from api.model.station import StationModel
from api.model.stations import StationsModel
from api.schema.stations import StationsSchema

stations_api = Blueprint('stations', __name__)

MEVO_HEADERS = {'Client-Identifier': 'hackaton-pg'}
MEVO_URL = "https://gbfs.urbansharing.com/rowermevo.pl"
logger = get_logger(__name__)


@stations_api.route('/stations')
def find_stations_info():
    params = request.args
    lat = params.get("lat")
    lon = params.get("lon")

    try:
        response = requests.get(MEVO_URL + "/station_information.json", headers=MEVO_HEADERS)
        stations_data = []
        for i in response.json()["data"]["stations"]:
            stations_data.append(get_station_data(i).serialize())

        result = None
        if lat is None or lon is None:
            result = StationsModel(stations_data)
        else:
            closest_stations = get_closest_stations(stations_data, float(lat), float(lon))
            result = StationsModel(closest_stations)
        return StationsSchema().dump(result), HTTPStatus.OK
    except Exception as e:
        logger.error("Stations error: " + str(e))
        return "", HTTPStatus.BAD_REQUEST


def get_station_data(json_row: dict) -> StationModel:
    station_coordinates = {"lat": json_row["lat"], "lon": json_row["lon"]}
    park_zone_coordinates = [{"lat": row[0], "lon": row[1]} for row in json_row["station_area"]["coordinates"][0][0]]

    return StationModel(
        json_row["station_id"],
        json_row["name"],
        json_row["address"],
        station_coordinates,
        park_zone_coordinates
    )


def get_closest_stations(stations: list, lat: float, lon: float) -> list:
    RANGE = 2_000
    close_stations = []
    for station in stations:
        station_lat = float(station["coordinates"]["lat"])
        station_lon = float(station["coordinates"]["lon"])
        if calculate_mercator_difference_in_meters((lat, lon), (station_lat, station_lon)) < RANGE:
            close_stations.append(station)

    return close_stations


def calculate_mercator_difference_in_meters(p1: tuple, p2: tuple):
    R = 6371
    dlat = math.radians(p1[0] - p2[0])
    dlon = math.radians(p1[1] - p2[1])

    a = math.sin(dlat / 2) ** 2 + math.cos(math.radians(p1[0])) * math.cos(math.radians(p1[0])) * math.sin(dlon / 2) ** 2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    distance = R * c

    return distance * 1000
