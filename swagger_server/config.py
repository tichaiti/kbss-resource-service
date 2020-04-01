import os

from connexion import FlaskApp
from flask_pymongo import PyMongo
from mongodb_migrations.cli import MigrationManager

from swagger_server import migrations

MONGO_DB = PyMongo()


def configure_mongo(app: FlaskApp, py_mongo: PyMongo):
    app.config["MONGO_URI"] = os.environ.get("MONGO_URI", default='mongodb://localhost:27017/myDatabase')
    py_mongo.init_app(app)
    perform_migrations(app.config["MONGO_URI"])


def perform_migrations(mongo_url: str):
    manager = MigrationManager()
    manager.config.mongo_url = mongo_url
    manager.config.mongo_migrations_path = os.path.dirname(migrations.__file__)
    manager.run()

