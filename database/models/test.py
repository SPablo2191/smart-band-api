from datetime import datetime
from database.db import db
from marshmallow import Schema, fields
from .status_test import StatusTestSchema
class Test(db.Model):
    __tablename__ = "test"
    id = db.Column(db.Integer, primary_key=True)
    status = db.Column(db.Boolean, default=True, nullable=False)
    register_date = db.Column(db.DateTime, default=datetime.utcnow())
    status_test_id = db.Column(db.Integer, db.ForeignKey("statusTest.id"), unique=True)
    promotion_id = db.Column(db.Integer, db.ForeignKey("promotion.id"), unique=True)
    teacher_id = db.Column(db.Integer, db.ForeignKey("teacher.id"), nullable=False)
    # teacher = db.relationship("Teacher", backref="test", uselist=False)
    status_test = db.relationship("StatusTest", backref="test", uselist=False)
    promotion = db.relationship("Promotion", backref="test", uselist=False)
    exercises = db.relationship(
        "Exercise", backref="test", secondary="exercise_test", lazy=True
    )

class TestSchema(Schema):
    id = fields.Integer()
    status = fields.Boolean()
    register_date = fields.Date()
    status_test = fields.Nested(StatusTestSchema, many=True)


test_schema = TestSchema()
tests_schema = TestSchema(many=True)