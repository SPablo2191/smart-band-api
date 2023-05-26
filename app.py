from flask import Flask
from config import config
app = Flask(__name__)
config(app=app)

if __name__ == "__main__":
    app.run(debug=True)
