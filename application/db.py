from flask_mongoengine import MongoEngine

db = MongoEngine()


def ini_db(app):
    db.init_app(app)
