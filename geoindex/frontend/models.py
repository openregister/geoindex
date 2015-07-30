from sqlalchemy import Column, Integer, String
from geoalchemy2 import Geometry

from geoindex.extensions import db
import geoalchemy2.functions as geofunc



class Boundary(db.Model):

    __tablename__ = 'boundary'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    polygon = Column(Geometry('MULTIPOLYGON', srid=4326))


    def to_dict(self):
        #TODO turn it into proper geojson and also
        #reverse multipolygon if required
        polygon = db.session.scalar(geofunc.ST_AsGeoJSON(self.polygon))
        return {"name": self.name, "polygon": polygon}
