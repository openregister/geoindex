import json

from sqlalchemy import Column, Integer, String
from geoalchemy2 import Geometry

from geoindex.extensions import db
import geoalchemy2.functions as geofunc



class Boundary(db.Model):

    __tablename__ = 'boundary'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    code = Column(String)
    polygon = Column(Geometry('MULTIPOLYGON', srid=4326))


    def to_dict(self):
        #TODO turn it into proper geojson and also
        #reverse multipolygon if required
        boundary = {"type": "Feature", "properties": {}, "geometry": {}}
        boundary["properties"] = {"name": self.name, "code": self.code}

        polygon = json.loads(db.session.scalar(geofunc.ST_AsGeoJSON(self.polygon)))
        coordinates = polygon["coordinates"]

        if len(coordinates) == 1:
            boundary["geometry"]["type"] = "Polygon"
            boundary["geometry"]["coordinates"] = coordinates[0]

        return boundary
