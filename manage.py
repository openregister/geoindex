#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
from flask.ext.script import Shell, Server, Manager
from flask.ext.migrate import Migrate, MigrateCommand
from flask.ext.sqlalchemy import SQLAlchemy

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

if __name__ == '__main__':
    manager.run()
