from src.db import db

class Location(db.Model):

     __tablename__  = 'locations'
     __table_args__ = {'schema' : 'master'}

     address_id     = db.Column(db.Integer, primary_key= True)

     city           = db.Column(db.String(100), nullable= False)

     state          = db.Column(db.String(100), nullable= False)

     def __repr__(self):
          return f"<State {self.state}>"