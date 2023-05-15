import datetime
from db import db
class Test(db.model):
    __tablename__ = "test"
    id = db.Column(db.Integer, primary_key=True)
    status = db.Column(db.Boolean, default=True, nullable=False)
    register_date = db.Column(db.DateTime, default=datetime.utcnow())