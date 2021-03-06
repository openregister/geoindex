===============================
geoindex
===============================

Requirements
-----------
- python 3.3
- [GEOS](http://trac.osgeo.org/geos/)
- [PROJ.4](http://trac.osgeo.org/proj/)
- [GDAL](http://trac.osgeo.org/gdal/)
- [Shapely](http://toblerity.org/shapely/)

Note if running on heroku the last four listed above can be satisfied by using this [buildpack](https://github.com/codeforamerica/heroku-buildpack-pygeo)

Quickstart
----------

Then run the following commands to bootstrap your environment.

```
mkvirtualenv --python=/path/to/required/python/version [appname]
```

Install python requirements.
```
pip install -r requirements/dev.txt
```

Prepare Postgres
----------------

```
createdb gis
psql -d gis -c 'CREATE EXTENSION postgis'
```

then create tables

```
source environment.sh
python manage.py db upgrade
```

To load data run:

```
python manage.py load_geojson
```

This loads the geojson data from: [https://github.com/openregister/boundaries](https://github.com/openregister/boundaries)

Once that this all done you can run the app:

```
./run.sh
```

Deployment
----------

In your production environment, make sure the ``SETTINGS`` environment variable is set to ``config.Config``.

Heroku
------
For heroku deployment use this [buildpack](https://github.com/codeforamerica/heroku-buildpack-pygeo) which has all the geo prerequisites.

This application is currently deployed at: [http://openregister-geoindex.herokuapp.com/](http://openregister-geoindex.herokuapp.com/)

