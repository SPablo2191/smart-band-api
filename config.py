from dotenv import load_dotenv
from flask_cors import CORS
from database.db import init_app, initialize_db, add_engine
from resources.routes import initialize_routes
from flask_restful import Api
import os


def config(app):
    load_dotenv()
    app.config[
        "SQLALCHEMY_DATABASE_URI"
    ] = f"postgresql://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}@{os.getenv('DB_HOST')}/{os.getenv('DB_NAME')}"
    CORS(app=app)
    initialize_db(app=app)
    init_app(app=app)
    add_engine(app=app)
    api = Api(app)
    initialize_routes(api=api)
