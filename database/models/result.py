from datetime import datetime
from database.db import db


class Result(db.Model):
    __tablename__ = "result"
    id = db.Column(db.Integer, primary_key=True)
    number_steps = db.Column(db.Integer, nullable=False)
    calories = db.Column(db.Float, nullable=False)
    average_heart_rate = db.Column(db.Float, nullable=False)
    distance = db.Column(db.Float, nullable=False)
    average_rate = db.Column(db.String(20), nullable=False)
    average_speed = db.Column(db.Float, nullable=False)
    average_cadene = db.Column(db.Float, nullable=False)
    average_stride = db.Column(db.Float, nullable=False)
    result = db.Column(db.Float, nullable=False)
    device_name = db.Column(db.String(100), nullable=False)
    status = db.Column(db.Boolean, default=True, nullable=False)
    register_date = db.Column(db.DateTime, default=datetime.utcnow())
    exercise_test_id = db.Column(db.Integer, db.ForeignKey("exercise.id"), nullable=False)
    student_id = db.Column(db.Integer, db.ForeignKey("student.id"), nullable=False)
    # student = db.relationship("Student", backref="result", uselist=False)
