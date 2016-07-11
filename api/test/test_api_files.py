import unittest


from ..db.dbController import db_session
from ..files.models import File
import pytest


xfail = pytest.mark.xfail


def test_artists_get():
    files = db_session.query(File).count()

    print(files)
    pass
