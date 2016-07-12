from config import *

from flask import Flask, request, redirect, url_for

# Base Flask app settings
app = Flask(__name__, static_url_path='/static')
app.config.from_object('config')


# urls patterns
from api.files.controllers import files_api as files_api_urls

# Register blueprints
app.register_blueprint(files_api_urls)


app.run(
    host=HOST,
    port=PORT,
    debug=DEBUG,
)

