__author__ = 'hyeonsj'

from flask import Blueprint


# Define URL blueprint for artists endpoints
files_api = Blueprint('files_api', __name__, url_prefix='/files')


# import controller for endpoints
from .files import files_list
from .files_detail import files_detail