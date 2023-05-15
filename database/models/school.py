import datetime
from db import db
class School(db.model):
    __tablename__ = "school"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    status = db.Column(db.Boolean, default=True, nullable=False)
    registerDate = db.Column(db.DateTime, default=datetime.utcnow())