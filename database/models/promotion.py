import datetime
from db import db
class Promotion(db.model):
    __tablename__ = "promotion"
    id = db.Column(db.Integer, primary_key=True)
    promotion_year = db.Column(db.DateTime, nullable = False)
    students =  db.relationship(
        "Student", backref="promotion", secondary="promotion_student", lazy=True
    )
    status = db.Column(db.Boolean, default=True, nullable=False)
    register_date = db.Column(db.DateTime, default=datetime.utcnow())