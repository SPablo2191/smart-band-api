from datetime import datetime
from database.db import db
from marshmallow import Schema, fields


class School(db.Model):
    __tablename__ = "school"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    status = db.Column(db.Boolean, default=True, nullable=False)
    register_date = db.Column(db.DateTime, default=datetime.utcnow())


class SchoolSchema(Schema):
    id = fields.Integer()
    name = fields.String()
    status = fields.Boolean()
    register_date = fields.Date()


school_schema = SchoolSchema()
schools_schema = SchoolSchema(many=True)
