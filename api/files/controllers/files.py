#-*- coding: utf-8 -*-
__author__ = 'hyeonsj'
from flask import url_for
from flask import request
from api.files.controllers import files_api
from api.utils.json_decorator import json
from api.db.dbController import db_session
from api.files.models import File
from api.utils.errors import unprocessable_entry
from werkzeug.utils import secure_filename
from config import UPLOAD_FOLDER
from flask import render_template, request


@files_api.route("/", methods=['GET', 'POST'])
def files_list():
    view_type = request.args.get('type', '')
    if view_type == "index":
        files = db_session.query(File).group_by(File.type)
    else:
        files = db_session.query(File).filter(File.type == view_type)

    data = []
    for item in files:
        data_dict = item.to_json()
        data_dict['href'] = request.host_url[:-1] + url_for('files_api.files_detail', file_id=item.id)
        data.append(data_dict)
    return render_template('index.html', data=data)


@files_api.route("/", methods=['GET', 'POST'])
def carousel():
    return render_template('index.html')


@files_api.route("/api/", methods=['GET', 'POST'])
@json
def api_files_list():
    if request.method == 'GET':
        view_type = request.args.get('type', '')
        if view_type == "index":
            files = db_session.query(File).group_by(File.type)
        else:
            files = db_session.query(File).filter(File.type == view_type)

        data = []
        for item in files:
            data_dict = item.to_json()
            data_dict['href'] = request.host_url[:-1] + url_for('files_api.files_detail', file_id=item.id)
            data.append(data_dict)
        return {"data": data}, 200

    elif request.method == 'POST':

        import os
        upload_files = request.files.getlist('files', None)
        upload_file_type = request.form['type']

        if upload_file_type == "" or upload_file_type is None:
            return unprocessable_entry("type is required parameters")

        return_json = []
        for upload_file in upload_files:
            file_name = secure_filename(upload_file.filename)

            if file_name == "":
                return unprocessable_entry("file name are required parameters")

            #확장자 변경
            file_name_list = file_name.split(".")
            if file_name_list[-1] == "jpg-original":
                file_name_list[-1] = "jpg"
            file_type = file_name_list[-1]
            #파일 중복 확인
            files_count = db_session.query(File).filter(File.file_name == file_name).count()

            if files_count > 0:
                file_name_list[-2] = file_name_list[-2]+"_"+str(files_count)
            file_name = ".".join(file_name_list)

            #파일 저장
            file_path = UPLOAD_FOLDER+"/"+upload_file_type+"/"+file_name
            upload_file.save(os.path.join(file_path))

            #파일 사이즈
            file_size = os.path.getsize(file_path)

            new_file = File(file_name, file_type, file_size/1024.0, request.host_url[:-1]+file_path[1:],
                            upload_file_type)
            db_session.add(new_file)

            try:
                db_session.commit()
                data = new_file.to_json()
                data['href'] = request.host_url[:-1] + url_for('files_api.files_detail', file_id=new_file.id)
                return_json.append(data)

            except Exception:
                return unprocessable_entry("file should")

        return {"data": return_json}, 201