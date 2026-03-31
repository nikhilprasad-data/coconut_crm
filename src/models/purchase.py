from src.db import db

class Purchase(db.Model):

     __tablename__  = 'purchases'
     __table_args__ = {'schema'  : 'finance'}

     
     purchase_id    = db.Column(db.Integer, primary_key= True)

     seller_id      = db.Column(db.Integer, db.ForeignKey('master.sellers.seller_id'))

     purchase_date  = db.Column(db.Date, nullable = False)

     total_bags     = db.Column(db.Integer, nullable= False)

     waste_pieces   = db.Column(db.Integer, default = 0)

     rate_per_piece = db.Column(db.Numeric(10,2), nullable = False)

     def __repr__(self):
          return f"<Purchase {self.purchase_id}>"



