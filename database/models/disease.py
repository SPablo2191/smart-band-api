from datetime import datetime
from database.db import db
from marshmallow import Schema, fields


class Disease(db.Model):
    __tablename__ = "disease"
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(100), nullable=False)
    status = db.Column(db.Boolean, default=True, nullable=False)
    register_date = db.Column(db.DateTime, default=datetime.utcnow())
    students = db.relationship("DiseaseStudent", back_populates="disease")

class DiseaseSchema(Schema):
    id = fields.Integer()
    description = fields.String()
    status = fields.Boolean()
    register_date = fields.Date()


disease_schema = DiseaseSchema()
diseases_schema = DiseaseSchema(many=True)


