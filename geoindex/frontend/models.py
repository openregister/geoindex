from sqlalchemy import Column, Integer, String
from geoalchemy2 import Geometry

from geoindex.extensions import db

class Boundary(db.Model):

    __tablename__ = 'boundary'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    polygon = Column(Geometry('MULTIPOLYGON', srid=4326))
