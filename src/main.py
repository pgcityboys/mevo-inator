import config
from flask import Flask
from logger import get_logger

logger = get_logger("main")

app = Flask(__name__)

@app.route('/') 
def home():
    logger.debug("Got home request")
    return "Hello, world!"
