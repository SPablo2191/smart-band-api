from datetime import datetime
from database.db import db
from marshmallow import Schema, fields
from .student import StudentSchema
class Promotion(db.Model):
    __tablename__ = "promotion"
    id = db.Column(db.Integer, primary_key=True)
    promotion_year = db.Column(db.DateTime, nullable=False)
    students = db.relationship(
        "Student", backref="promotion", secondary="promotion_student", lazy=True
    )
    status = db.Column(db.Boolean, default=True, nullable=False)
    class_id = db.Column(db.Integer, db.ForeignKey("class.id"), nullable=False)
    prom_class = db.relationship("Class", backref="promotion", uselist=False)
    register_date = db.Column(db.DateTime, default=datetime.utcnow())


class PromotionSchema(Schema):
    id = fields.Integer()
    promotion_year = fields.Date()
    status = fields.Boolean()
    register_date = fields.Date()
    students = fields.Nested()


promotion_schema = PromotionSchema()
promotions_schema = PromotionSchema(many=True)