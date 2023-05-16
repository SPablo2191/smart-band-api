from datetime import datetime
from database.db import db


class Student(db.Model):
    __tablename__ = "student"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    last_name = db.Column(db.String(100), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    weight = db.Column(db.Float, nullable=False)
    size = db.Column(db.Float, nullable=False)
    DNI = db.Column(db.String(15), nullable=False)
    status = db.Column(db.Boolean, default=True, nullable=False)
    register_date = db.Column(db.DateTime, default=datetime.utcnow())
    diseases = db.relationship(
        "Disease", backref="student", secondary="disease_student", lazy=True
    )
    results = db.relationship("Result", backref="student", lazy=True)
