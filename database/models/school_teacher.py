from datetime import datetime
from database.db import db
from marshmallow import Schema, fields
from .school import SchoolSchema
class SchoolTeacher(db.Model):
    __tablename__ = "school_teacher"
    id = db.Column(db.Integer, primary_key=True)
    school_id = db.Column(db.Integer, db.ForeignKey("school.id"), nullable=False)
    teacher_id = db.Column(db.Integer, db.ForeignKey("teacher.id"), nullable=False)
    status = db.Column(db.Boolean, default=True, nullable=False)
    register_date = db.Column(db.DateTime, default=datetime.utcnow())
    teacher = db.relationship('Teacher', back_populates='schools')
    school = db.relationship('School', back_populates='teacher_schools')

class TeacherSchoolSchema(Schema):
    school = fields.Nested(SchoolSchema)