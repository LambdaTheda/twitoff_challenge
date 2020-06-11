# twitoff_challenge

# Installation 

```sh
deactivate current enviornments: conda deactivate

git clone https://github.com/crd3cc04/twitoff_challenge.git

cd twitoff_challenge
```


# Setup

```sh
create enviornment: python -m venv pipenv

install packages: pip install Flask Flask-SQLAlchemy Flask-Migrate

activate envirornment: pipenv\Scripts\activate

open vs code: code .

Migrate the database:
flask db init
flask db migrate
flask db upgrade
```

# Usage

```sh
to activate flask: set FLASK_APP=app_dev.py flask run
```