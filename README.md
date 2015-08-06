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

Set some environment variables. The following is required. Add as needed.

```
export SETTINGS='config.DevelopmentConfig'
```


Prepare Postgres
----------------

```
createdb -U gis
psql -d gis -c 'CREATE EXTENSION postgis'
```

then create tables

```
python manage.py db migrate
python manage.py upgrade
```

To load data run:

```
python manage.py load_geojson
```

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

