from datetime import datetime
from ..db.dbController import Base, db_session
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime


class File(Base):

    __tablename__ = 'files'
    id = Column(Integer, primary_key=True)
    file_name = Column(String(200))
    file_type = Column(String(20))
    file_size = Column(Integer)
    type = Column(String(45))
    created_at = Column(DateTime(timezone=False))
    updated_at = Column(DateTime(timezone=False))

    def __init__(self, **file_info):
        self.file_name = file_info.get('file_name', None)
        self.file_type = file_info.get('file_type', None)
        self.file_size = file_info.get('file_size', None)
        self.type = file_info.get('type', None)
        self.created_at = datetime.now()
        self.updated_at = datetime.now()



    def to_dict(self, instance_list):
        print(instance_list)
        file_list = [dict(id=file.id, file_name=file.file_name, file_type=file.file_type, file_size=file.file_size,
                          type=file.type) for file in instance_list]

        if len(file_list) > 1:
            return file_list
        else:
            return file_list[0]