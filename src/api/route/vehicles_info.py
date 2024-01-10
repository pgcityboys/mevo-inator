from http import HTTPStatus
from flask import Blueprint, request
from logger import get_logger
from api.model.vehicles_info import VehiclesInfoModel
from api.schema.vehicles_info import VehiclesInfoSchema
from utils.json import find_json_by_value
import requests

logger = get_logger(__name__)

MEVO_URL = "https://gbfs.urbansharing.com/rowermevo.pl"
MEVO_HEADERS = {
    'Client-Identifier': 'hackaton-pg'
}

vehicles_info_api = Blueprint('VehiclesInfoApi', __name__)


def get_vehicles_info(station_id: str) -> dict:
    bikes_data = requests.get(MEVO_URL + "/station_status.json", headers=MEVO_HEADERS)
    station = find_json_by_value("station_id", station_id, bikes_data.json()["data"]["stations"])

    return {
        "vehicles_available": station["vehicle_types_available"],
        "parking_slots_available": station["num_docks_available"],
    }

@vehicles_info_api.route('vehicles/<station_id>')
def vehicles_info_page(station_id : str):
    logger.debug(f"Got request for the {station_id} station")
    try:
        vehicles_info = get_vehicles_info(station_id)
        result = VehiclesInfoModel(vehicles_info['vehicles_available'], vehicles_info['parking_slots_available'])
        return VehiclesInfoSchema().dump(result), HTTPStatus.OK
    except KeyError:
        logger.error(f"{station_id} station is not found")
        return "", HTTPStatus.NOT_FOUND
    except Exception as e:
        logger.error(f"{station_id} station error: " + str(e))
        return "", HTTPStatus.BAD_REQUEST