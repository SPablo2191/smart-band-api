from datetime import datetime
from database.db import db
from marshmallow import Schema, fields


class Exercise(db.Model):
    __tablename__ = "exercise"
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(100), nullable=False)
    status = db.Column(db.Boolean, default=True, nullable=False)
    register_date = db.Column(db.DateTime, default=datetime.utcnow())


class ExerciseSchema(Schema):
    id = fields.Integer()
    description = fields.String()
    status = fields.Boolean()
    register_date = fields.Date()


exercise_schema = ExerciseSchema()
exercises_schema = ExerciseSchema(many=True)
