from flask_bcrypt import Bcrypt

bcrypt = Bcrypt()


def initialize_encrypt(app):
    bcrypt.init_app(app)
