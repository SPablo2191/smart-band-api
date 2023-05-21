from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from sqlalchemy.pool import QueuePool

ma = Marshmallow()
db = SQLAlchemy()


def initialize_db(app):
    db.init_app(app)


def add_engine(app):
    with app.app_context():
        app.config["SQLALCHEMY_POOL_SIZE"] = 5
        app.config["SQLALCHEMY_MAX_OVERFLOW"] = 5
        engine = db.create_engine(
            app.config["SQLALCHEMY_DATABASE_URI"],
            poolclass=QueuePool,
            pool_size=app.config["SQLALCHEMY_POOL_SIZE"],
            max_overflow=app.config["SQLALCHEMY_MAX_OVERFLOW"],
            pool_timeout=60,
        )
        db.session.configure(bind=engine)


def init_app(app):
    ma.init_app(app)
