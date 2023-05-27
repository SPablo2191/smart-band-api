from dotenv import load_dotenv
from flask_cors import CORS
from database.db import init_app, initialize_db, add_engine
from resources.routes import initialize_routes,register_docs
from flask_restful import Api
from functions.encrypt import initialize_encrypt
from flask_jwt_extended import JWTManager
from functions.swagger import api_spec_conf
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
    initialize_encrypt(app=app)
    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
    jwt = JWTManager(app)
    api_spec_conf(app=app)
    register_docs()

