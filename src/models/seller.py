from src.db import db

class Seller(db.Model):

     __tablename__  = 'sellers'
     __table_args__ = {'schema' : 'master'}

     seller_id      = db.Column(db.Integer, primary_key= True)

     seller_name    = db.Column(db.String(100), nullable= False )

     contact_number = db.Column(db.String(20), nullable= False)

     address_id     = db.Column(db.Integer, db.ForeignKey('master.locations.address_id'))

     def __repr__(self):
          return f"<Seller {self.seller_name}>"