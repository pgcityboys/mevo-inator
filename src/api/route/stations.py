from http import HTTPStatus
from logger import get_logger

import requests as requests
from flask import Blueprint
from api.model.station import StationModel
from api.model.stations import StationsModel
from api.schema.stations import StationsSchema

stations_api = Blueprint('stations', __name__)

MEVO_HEADERS = {'Client-Identifier': 'hackaton-pg'}
MEVO_URL = "https://gbfs.urbansharing.com/rowermevo.pl"
logger = get_logger(__name__)


@stations_api.route('/stations')
def find_stations_info():
    try:
        response = requests.get(MEVO_URL + "/station_information.json", headers=MEVO_HEADERS)
        stations_data = []
        for i in response.json()["data"]["stations"]:
            stations_data.append(get_station_data(i).serialize())
        result = StationsModel(stations_data)
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
