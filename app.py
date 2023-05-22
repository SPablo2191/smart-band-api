from flask import Flask
from config import config
app = Flask(__name__)
config(app=app)

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
