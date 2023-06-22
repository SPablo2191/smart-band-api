from datetime import datetime
from database.db import db
from marshmallow import Schema, fields
from .school import SchoolSchema
from .student import StudentSchema
class PromotionStudent(db.Model):
    __tablename__ = "promotion_student"
    id = db.Column(db.Integer, primary_key=True)
    promotion_id = db.Column(db.Integer, db.ForeignKey("promotion.id"), nullable=False)
    student_id = db.Column(db.Integer, db.ForeignKey("student.id"), nullable=False)
    status = db.Column(db.Boolean, default=True, nullable=False)
    register_date = db.Column(db.DateTime, default=datetime.utcnow())
    student = db.relationship("Student", back_populates="promotions")
    promotion = db.relationship("Promotion")

class PromotionStudentSchema(Schema):
    school = fields.Nested(SchoolSchema)
    student = fields.Nested(StudentSchema)