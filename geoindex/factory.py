# -*- coding: utf-8 -*-
'''The app module, containing the app factory function.'''
import os
from flask import Flask, render_template
from geoindex.extensions import db


def asset_path_context_processor():
    return {'asset_path': '/static/'}


def create_app():
    app = Flask(__name__)
    app.config.from_object(os.environ['SETTINGS'])
    register_errorhandlers(app)
    register_blueprints(app)
    register_extensions(app)
    app.context_processor(asset_path_context_processor)
    return app


def register_errorhandlers(app):
    def render_error(error):
        # If a HTTPException, pull the `code` attribute; default to 500
        error_code = getattr(error, 'code', 500)
        return render_template("{0}.html".format(error_code)), error_code
    for errcode in [401, 404, 500]:
        app.errorhandler(errcode)(render_error)
    return None


def register_blueprints(app):
    from geoindex.frontend.views import frontend
    app.register_blueprint(frontend)


def register_extensions(app):
    db.init_app(app)
