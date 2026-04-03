from flask import Blueprint, jsonify
from flask_jwt_extended import jwt_required,get_jwt_identity
from src.models.seller import Seller
from src.models.purchase import Purchase
from src.models.user import User

purchase_bp = Blueprint('purchase', __name__, url_prefix='/api/purchase')

@purchase_bp.route('/data/<int:seller_id>', methods= ['GET'])
@jwt_required()
def get_purchase(seller_id):
     try:
          current_user_identity = get_jwt_identity()
          current_user          = User.query.filter_by(user_id= int(current_user_identity)).first()

          if not current_user:
               return jsonify({
                              "status" : "error",
                              "message": "User not forund"
               }), 404
          
          if current_user.role == 'Seller':
               if current_user.seller_id != seller_id:
                    return jsonify({
                              "status" : "error",
                              "message": "Access Denied. You can't see other seller's purchase."
                    }), 403
                    
          existing_seller     = Seller.query.get(seller_id)
          if not existing_seller:
               return jsonify({
                              "status" : "error",
                              "message": f"{seller_id} seller id, not exists"
               }), 404
          
          seller_dict  = {
                              "seller_id"              : existing_seller.seller_id,
                              "seller_name"            : existing_seller.seller_name,
                              "seller_contact_number"  : existing_seller.contact_number}

          all_purchase = Purchase.query.filter_by(seller_id= seller_id).all()

          purchase_list = []

          for purchase in all_purchase:
               purchase_dict = {
                                   "purchase_id"       : purchase.purchase_id,
                                   "purchase_date"     : str(purchase.purchase_date),
                                   "total_bags"        : purchase.total_bags,
                                   "waste_pieces"      : purchase.waste_pieces,
                                   "rate_per_piece"    : float(purchase.rate_per_piece),
                                   "total_amount"      : round(float(((purchase.total_bags * 30) - purchase.waste_pieces)*purchase.rate_per_piece),2)}
               
               purchase_list.append(purchase_dict)

          return jsonify({
                         "status"       : "success",
                         "seller_data"  : seller_dict,
                         "purchase_data": purchase_list
          }), 200
     
     except Exception as e:
          print(e)
          return jsonify({
                         "status"  : "error",
                         "message" : "Internal server error"
          }), 500