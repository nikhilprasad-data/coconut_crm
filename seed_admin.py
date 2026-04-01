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
          username       =    os.environ.get('ADMIN_USERNAME')
          password       =    os.environ.get('ADMIN_PASSWORD')
          password_hash  =    generate_password_hash(password)
          role           =    'admin'

          existing_user  = User.query.filter_by(role= 'admin').first()

          if existing_user:
               print("Admin already exists")
          else:
               admin = User(username= username, password_hash= password_hash, role= role)
               db.session.add(admin)
               db.session.commit()
               print("Admin created successfully")

     except Exception as e:
          print(e)