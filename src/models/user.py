from src.db import db

class User(db.Model):
     __tablename__  = 'users'
     __table_args__ = {'schema': 'master'}

     user_id        = db.Column(db.Integer, primary_key = True)

     username       = db.Column(db.String(100), unique = True, nullable = False)

     password_hash  = db.Column(db.String(255), nullable = False)

     role           = db.Column(db.String(20), default = 'Seller')

     seller_id      = db.Column(db.Integer, db.ForeignKey('master.sellers.seller_id'), nullable = True)

     def __repr__(self):
          return f"<User {self.username}>"