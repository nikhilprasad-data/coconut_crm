from src.db import db

class Payment(db.Model):

     __tablename__  = 'payments'
     __table_args__ = {'schema' : 'finance'}

     payment_id     = db.Column(db.Integer, primary_key = True)

     seller_id	     = db.Column(db.Integer, db.ForeignKey('master.sellers.seller_id'))

     payment_date   = db.Column(db.Date, nullable = False)

     amount_paid    = db.Column(db.Numeric(12,2), nullable = False)

     payment_method = db.Column(db.String(50), nullable = False)


     def __repr__(self):
          return f"<Payment {self.payment_id}>"