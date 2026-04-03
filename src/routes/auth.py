from flask import Blueprint, jsonify, request
from werkzeug.security import check_password_hash
from src.models.user import User
from flask_jwt_extended import create_access_token, jwt_required

auth_bp = Blueprint('auth', __name__, url_prefix='/api/auth')

@auth_bp.route('/test', methods=['GET'])
def test_auth():
     try:

          return jsonify({
                         "status"  : "success",
                         "message" : "auth route is working perfectly"
          }), 200
      
     except Exception as e:
          print(e)
          return jsonify({
                         "status"  : "error",
                         "message" : "Internal server error"
          }), 500

@auth_bp.route('/login/admin', methods= ['POST'])
def login_admin():
     try:
          data                = request.get_json()

          required_fields     = ["username", "password"]

          for field in required_fields:

               if not data.get(field) or not str(data.get(field)).strip():
                    return jsonify({
                              "status"  : "error",
                              "message" : f"{field}, is missing or empty. Please provide all the details"
                    }), 400


          username       = data.get("username").strip()
          password       = data.get("password").strip()

          existing_admin = User.query.filter_by(username= username, role= 'admin').first()

          if existing_admin and (check_password_hash(existing_admin.password_hash, password)) :

               access_token = create_access_token(identity= str(existing_admin.user_id))
               return jsonify({
                              "status"       : "success",
                              "message"      : f"sucessfully logged in as admin {username}",
                              "access_token" : access_token
               }), 200

          else:

               return jsonify({
                              "status"  : "error",
                              "message" : "Invalid username or password"
               }), 401
          
     except Exception as e:
          print(e)
          return jsonify({
                         "status" : "error",
                         "message" : "Internal server error"
          }), 500
     
@auth_bp.route('/login/seller', methods= ['POST'])
def login_seller():
     try:
          data = request.get_json()

          required_fields = ["username", "password"]

          for field in required_fields:

               if not (data.get(field)) or not (str(data.get(field)).strip()):
                    return jsonify({
                              "status"  : "error",
                              "message" : f"{field}, is missing or empty. Please provide all the details"
                    }), 400
               
          user_name = data.get("username").strip()
          password  = data.get("password").strip()

          existing_user = User.query.filter_by(username= user_name, role= 'Seller').first()

          if not existing_user:
               return jsonify({
                              "status"  : "error",
                              "message" : f"{user_name}, not exists."
               }), 404
               
          if not (check_password_hash(existing_user.password_hash, password)):
               return jsonify({
                              "status"  : "error",
                              "message" : "Invalid password"
               }), 401

          access_token = create_access_token(identity= str(existing_user.user_id))
          return jsonify({
                         "status"       : "success",
                         "message"      : f"sucessfully logged in as seller {user_name}",
                         "access_token" : access_token
               }), 200
          
     except Exception as e:
          print(e)
          return jsonify({
                         "status" : "error",
                         "message" : "Internal server error"
          }), 500

@auth_bp.route('/logout/admin', methods= ['POST'])
@jwt_required()
def logout_admin():
     try:
          return jsonify({
                         "status"       : "success",
                         "message"      : "Admin sucessfully logged out",
               }), 200
     
     except Exception as e:
          print(e)
          return jsonify({
                         "status" : "error",
                         "message" : "Internal server error"
          }), 500

@auth_bp.route('/logout/seller', methods= ['POST'])
@jwt_required()
def logout_seller():
     try:
          return jsonify({
                         "status"       : "success",
                         "message"      : "Seller sucessfully logged out",
               }), 200
     
     except Exception as e:
          print(e)
          return jsonify({
                         "status" : "error",
                         "message" : "Internal server error"
          }), 500