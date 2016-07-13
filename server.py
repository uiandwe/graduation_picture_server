from config import *

from flask import Flask, request, redirect, url_for
from flask_cors import CORS, cross_origin

# Base Flask app settings
app = Flask(__name__, static_url_path='/static')
app.config.from_object('config')
CORS(app)

# urls patterns
from api.files.controllers import files_api as files_api_urls

# Register blueprints
app.register_blueprint(files_api_urls)


app.run(
    host=HOST,
    port=PORT,
    debug=DEBUG,
)

