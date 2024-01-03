from flask_sqlalchemy import SQLAlchemy
from datetime import datetime



class User(db.Model):
    sno = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(200),nullable=False)
    email = db.Column(db.Integer,nullable=False)
    age = db.Column(db.Integer,nullable=False)
    password = db.Column(db.Integer,nullable=False)
    date_created = db.Column(db.DateTime,default=datetime.utcnow)
 
    def __repr__(self)->str:
        return f"{self.sno} - {self.username}"


print("database running!")