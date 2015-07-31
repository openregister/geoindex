===============================
geoindex
===============================


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
createdb -U [user name] [db name]
psql -U [user name] -d [db name] -c 'CREATE EXTENSION postgis'
```

then create tables

```
python manage.py db migrate
python manage.py upgrade
```

Once that this all done you can:

```
python manage.py server
```

Deployment
----------

In your production environment, make sure the ``SETTINGS`` environment variable is set to ``config.Config``.

Heroku
------
For heroku deployment use this buildpack [https://github.com/codeforamerica/heroku-buildpack-pygeo] which has all the geo prerequisites.

Shell
-----

To open the interactive shell, run ::

```
python manage.py shell
```
