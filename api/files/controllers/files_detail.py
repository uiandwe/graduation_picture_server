from flask import url_for
from flask import request

from api.files.models import File
from api.files.controllers import files_api
from api.utils.json_decorator import json


@files_api.route("/<int:file_id>/", methods=['GET'])
@json
def files_detail(file_id):
    file = File.query.get(file_id)
    if file:
        data_dict = file.to_json()
        data_dict['href'] = request.host_url[:-1] + url_for('files_api.files_detail', file_id=file.id)
        return {"data": data_dict}, 200
    return {"error": "URL path invalid, check artist_id"}, 404
