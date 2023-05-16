import datetime
from database.db import db


class Teacher(db.model):
    __tablename__ = "teacher"
    id = db.Column(db.Integer, primary_key=True)
    DNI = db.Column(db.String(15), nullable=False)
    name = db.Column(db.String(100), nullable=False)
    last_name = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(150), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    status = db.Column(db.Boolean, default=True, nullable=False)
    register_date = db.Column(db.DateTime, default=datetime.utcnow())
    tests = db.relationship("Test", backref="teacher", lazy=True)
    schools = db.relationship(
        "School", backref="teacher", secondary="school_teacher", lazy=True
    )
