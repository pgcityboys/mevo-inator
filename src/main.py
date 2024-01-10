from flask import Flask
from logger import get_logger
from api.route.start_page import start_api
from api.route.stations import stations_api
from api.route.vehicles_info import vehicles_info_api

logger = get_logger("main")


def create_app():
    logger.debug("Create app")
    app = Flask(__name__)
    app.register_blueprint(start_api, url_prefix='/api')
    app.register_blueprint(vehicles_info_api, url_prefix='/api')
    app.register_blueprint(stations_api, url_prefix='/api')
    return app


if __name__ == '__main__':
    app = create_app()
    app.run(host='0.0.0.0')
