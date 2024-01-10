from http import HTTPStatus
from flask import Blueprint
from api.model.hello import HelloModel
from api.schema.hello import HelloSchema

start_api = Blueprint('api', __name__)

@start_api.route('/')
def start_page():
    result = HelloModel()
    return HelloSchema().dump(result), HTTPStatus.OK