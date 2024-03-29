from datetime import datetime
from database.db import db
from marshmallow import Schema, fields

class Class(db.Model):
    __tablename__ = "class"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    status = db.Column(db.Boolean, default=True, nullable=False)
    register_date = db.Column(db.DateTime, default=datetime.utcnow())
    school_id = db.Column(db.Integer, db.ForeignKey("school.id"), nullable=False)
    school = db.relationship("School", backref="class", uselist=False)


class ClassSchema(Schema):
    id = fields.Integer()
    name = fields.String()
    status = fields.Boolean()
    register_date = fields.Date()


class_schema = ClassSchema()
classes_schema = ClassSchema(many=True)
