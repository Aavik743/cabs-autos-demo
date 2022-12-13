from flask_mongoengine import MongoEngine

from config import MONGO_DB

db = MongoEngine()


def init_mongodb(app):
    db.init_app(app, config=MONGO_DB)