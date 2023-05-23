from datetime import datetime
from database.db import db
from marshmallow import Schema, fields
from .exercise import ExerciseSchema
class ExerciseTest(db.Model):
    __tablename__ = "exercise_test"
    id = db.Column(db.Integer, primary_key=True)
    test_id =  db.Column(db.Integer, db.ForeignKey("test.id"), nullable=False)
    exercise_id =  db.Column(db.Integer, db.ForeignKey("exercise.id"), nullable=False)
    status = db.Column(db.Boolean, default=True, nullable=False)
    register_date = db.Column(db.DateTime, default=datetime.utcnow())
    test = db.relationship('Test', back_populates='exercises')
    exercise = db.relationship('Exercise')

class ExerciseTestSchema(Schema):
    exercise = fields.Nested(ExerciseSchema)
