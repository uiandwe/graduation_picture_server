from config import *

from flask import Flask

# Base Flask app settings
app = Flask(__name__)
app.config.from_object('config')


app.run(
    host=HOST,
    port=PORT,
    debug=DEBUG,
)
