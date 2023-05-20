from datetime import datetime
from database.db import db
from marshmallow import Schema, fields
from .school import SchoolSchema


class Teacher(db.Model):
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


class TeacherSchema(Schema):
    id = fields.Integer()
    DNI = fields.String()
    name = fields.String()
    last_name = fields.String()
    password = fields.String()
    email = fields.String()
    status = fields.Boolean()
    register_date = fields.Date()
    schools = fields.Nested(SchoolSchema, many=True)
