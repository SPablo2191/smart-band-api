from datetime import datetime
from database.db import db
from marshmallow import Schema, fields
from .disease import DiseaseSchema
from .disease_student import DiseaseStudent
from .result import ResultSchema
from .promotion_student import PromotionStudentSchema
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
    seat_height = db.Column(db.Float,nullable=False)
    waist = db.Column(db.Float, nullable=False)
    register_date = db.Column(db.DateTime, default=datetime.utcnow())
    diseases = db.relationship("DiseaseStudent", back_populates="student", uselist=False)
    promotions = db.relationship("PromotionStudent", back_populates="student", uselist=False)
    results = db.relationship("Result", backref="student", lazy=True)



class StudentSchema(Schema):
    id = fields.Integer()
    DNI = fields.String()
    name = fields.String()
    last_name = fields.String()
    status = fields.Boolean()
    register_date = fields.Date()
    weight = db.Float()
    size = db.Float()
    seat_height = db.Float()
    waist = db.Float()
    diseases = fields.Nested(DiseaseSchema,many=True)
    results = fields.Nested(ResultSchema,many=True)
    promotions = fields.Nested(PromotionStudentSchema,many=True)

student_schema = StudentSchema()
students_schema = StudentSchema(many=True)