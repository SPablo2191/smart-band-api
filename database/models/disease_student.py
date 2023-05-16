from datetime import datetime
from database.db import db


class DiseaseStudent(db.Model):
    __tablename__ = "disease_student"
    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer, db.ForeignKey("student.id"), nullable=False)
    disease_id = db.Column(db.Integer, db.ForeignKey("disease.id"), nullable=False)
    status = db.Column(db.Boolean, default=True, nullable=False)
    register_date = db.Column(db.DateTime, default=datetime.utcnow())
