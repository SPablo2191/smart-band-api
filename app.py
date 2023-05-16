from flask import Flask
from flask_cors import CORS
from config import config
from database.db import init_app,initialize_db,add_engine
from database.db_maker import create_db
app = Flask(__name__)
config(app=app)
CORS(app=app)
initialize_db(app=app)
init_app(app=app)
add_engine(app=app)
# drop_db(app=app)
create_db(app=app)

@app.route("/")
@app.route("/api")
def index():
    return {
        "Authors": ["Pablo Sandoval", "Diego Pardo"],
        "message": "Welcome to the API REST from SmartBand 😽",
        "routes": [],
    }


if __name__ == "__main__":
    app.run(debug=True)
