from datetime import datetime
from ..db.dbController import Base, db_session
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime


class File(Base):

    __tablename__ = 'files'
    id = Column(Integer, primary_key=True)
    file_name = Column(String(200))
    file_type = Column(String(20))
    file_size = Column(Integer)
    path = Column(String(250))
    type = Column(String(45))
    created_at = Column(DateTime(timezone=False))
    updated_at = Column(DateTime(timezone=False))

    def __init__(self, file_name, file_type=None, file_size=0, path=None, type=None):
        self.file_name = file_name
        self.file_type = file_type
        self.file_size = file_size
        self.path = path
        self.type = type
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def to_json(self):
        file = dict()
        file['id'] = self.id
        file['file_name'] = self.file_name
        file['file_type'] = self.file_type
        file['file_size'] = self.file_size
        file['path'] = self.path
        file['type'] = self.type
        file['created_at'] = self.created_at
        file['updated_at'] = self.updated_at

        return file