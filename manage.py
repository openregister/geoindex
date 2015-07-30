#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
from flask.ext.script import Shell, Server, Manager
from flask.ext.migrate import Migrate, MigrateCommand
from flask.ext.sqlalchemy import SQLAlchemy
import geojson
from zipfile import ZipFile
from urllib.request import urlopen
from io import BytesIO, TextIOWrapper
from geoalchemy2.shape import from_shape
from shapely.geometry import asShape


from geoindex.factory import create_app
app = create_app()
app.debug = True
port = os.environ.get('PORT', 8000)

manager = Manager(app)
manager.add_command('server', Server(host="0.0.0.0", port=port))

from geoindex.extensions import db
from geoindex.frontend.models import *

migrate = Migrate(app, db)
manager.add_command('db', MigrateCommand)


@manager.command
def load_geojson():
    result = urlopen('https://github.com/openregister/boundaries/archive/master.zip').read()
    stream = BytesIO(result)
    zipfile = ZipFile(stream, 'r')
    file_names = [name for name in zipfile.namelist()
                  if name.endswith('.geojson')]
    for name in file_names:
        with zipfile.open(name, 'r') as f:
            if name.endswith('.geojson'):
                file_contents = TextIOWrapper(f, encoding='utf-8',
                                          newline='')
                data = geojson.loads(file_contents.read())
                try:
                    name = data['properties']['REGD14NM']
                    geometry = data['geometry']
                    # hackery store everthing as multipolygon
                    if geometry['type'] == 'Polygon':
                        coordinates = []
                        coordinates.append(geometry['coordinates'])
                        geometry['coordinates'] = coordinates
                        geometry['type'] = 'MultiPolygon'
                    polygon = from_shape(asShape(geometry), srid=4326)
                    boundary = Boundary(name=name, polygon=polygon)
                    db.session.add(boundary)
                    db.session.commit()
                except KeyError as e:
                    print("not something we were expecting really")

if __name__ == '__main__':
    manager.run()
