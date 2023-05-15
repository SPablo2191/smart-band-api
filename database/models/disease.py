import datetime
from db import db
class Disease(db.model):
    __tablename__ = "disease"
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(100), nullable=False)
    status = db.Column(db.Boolean, default=True, nullable=False)
    registerDate = db.Column(db.DateTime, default=datetime.utcnow())