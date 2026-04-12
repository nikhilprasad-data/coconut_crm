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

          demo_username       =    "demo_admin_11"
          demo_password       =    "demo_password"
          demo_password_hash  =    generate_password_hash(demo_password)
          demo_role           =    'admin'

          existing_user       =    User.query.filter_by(username= username).first()
          demo_existing_user  =    User.query.filter_by(username= demo_username).first()

          if existing_user:
               print("Admin already exists")
          else:
               admin     = User(username= username, password_hash= password_hash,  role= role)
               db.session.add(admin)
               db.session.commit()
               print("Admin created successfully")

          if demo_existing_user:
               print("Demo Admin already exists")
          else:
               demo_admin     = User(username= demo_username, password_hash= demo_password_hash,  role= demo_role)
               db.session.add(demo_admin)
               db.session.commit()
               print("Demo Admin created successfully")
               
     except Exception as e:
          print(e)