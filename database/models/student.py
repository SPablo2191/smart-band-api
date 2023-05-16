from datetime import datetime
from database.db import db
from marshmallow import Schema, fields
from .disease import DiseaseSchema


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


class StudentSchema(Schema):
    id = fields.Integer()
    name = fields.String()
    last_name = fields.String()
    age = fields.Float()
    weight = fields.Float()
    size = fields.Float()
    DNI = fields.String()
    status = fields.Boolean()
    register_date = fields.Date()
    diseases = fields.Nested(DiseaseSchema, many=True)


student_schema = StudentSchema()
students_schema = StudentSchema(many=True)
