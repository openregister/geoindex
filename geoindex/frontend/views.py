import requests

from flask import (
    Blueprint,
    render_template,
    current_app,
    abort,
    url_for,
    redirect
)

from sqlalchemy import func
from geoalchemy2.shape import from_shape
from shapely.geometry import Point

from geoindex.frontend.models import Boundary
from geoindex.frontend.forms import PostcodeForm

frontend = Blueprint('frontend', __name__, template_folder='templates')

@frontend.route('/', methods=['GET', 'POST'])
def index():
    form = PostcodeForm()
    if form.validate_on_submit():
        postcode = form.data['postcode'].strip().upper()
        current_app.logger.info(postcode)
        url = 'http://postcode.openregister.org/search'
        params = {'_query': postcode, '_representation': 'json'}
        headers = {'Content-type': 'application/json'}
        try:
            resp = requests.get(url, headers=headers, params=params)
            resp.raise_for_status()
            entry = resp.json()['entries'][0]
            current_app.logger.info(entry)
            latitude = entry['entry']['latitude']
            longitude = entry['entry']['longitude']
            return redirect(url_for('frontend.location', latitude=latitude, longitude=longitude))

        except requests.exceptions.HTTPError as e:
            abort(resp.status_code)
    return render_template('index.html', form=form)


@frontend.route('/location/<latitude>/<longitude>')
def location(latitude, longitude):
    point = Point(float(longitude), float(latitude))
    wkb_element = from_shape(point, srid=4326)
    boundaries = Boundary.query.filter(func.ST_Contains(Boundary.polygon, wkb_element)).all()
    for boundary in boundaries:
        current_app.logger.info(boundary.name)
    return render_template('location.html', latitude=latitude, longitude=longitude, boundary=boundary)
