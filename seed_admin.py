from src import create_app
from src.db import db
from src.models.user import User
from src.models.seller import Seller
from src.models.location import Location
from werkzeug.security import generate_password_hash
import os
from dotenv import load_dotenv

load_dotenv()

app = create_app()

with app.app_context():
     db.create_all()

     try:
          username       =    os.environ.get('ADMIN_USERNAME',"")
          password       =    os.environ.get('ADMIN_PASSWORD', "")
          password_hash  =    generate_password_hash(password)
          role           =    'admin'

          existing_admin = User.query.filter_by(username= username).first()

          if existing_admin:
               print("Admin already exists.")

          else:
               admin = User(username= username, password_hash= password_hash, role= "admin")
               db.session.add(admin)
               db.session.commit()
               print("Admin created successfully.")
               
     except Exception as e:
          print(e)