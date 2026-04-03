from flask import Blueprint, jsonify
from flask_jwt_extended import get_jwt_identity,jwt_required
from src.models.payment import Payment
from src.models.seller import Seller
from src.models.user import User

payment_bp = Blueprint('payment', __name__, url_prefix='/api/payment')

@payment_bp.route('/data/<int:seller_id>',methods=['GET'])
@jwt_required()
def get_payment(seller_id):
     try:
          current_identity = int(get_jwt_identity())
          current_user = User.query.filter_by(user_id= current_identity).first()

          if not current_user:
               return jsonify({
                              "status"  : "error",
                              "message" : "User not found"
               }), 404
          
          if current_user.role == 'Seller':
               if current_user.seller_id != seller_id:
                    return jsonify({
                                   "status" : "error",
                                   "message" : "Access Denied. You can't see other seller's payments"
                    }), 403
          
          existing_seller = Seller.query.get(seller_id)

          if not existing_seller:
               return jsonify({
                              "status" : "error",
                              "message" : f"{seller_id}, seller id not exists"
                    }), 404
          
          seller_dict = {
                         "seller_id"              : existing_seller.seller_id,
                         "seller_name"            : existing_seller.seller_name,
                         "seller_contact_number"  : existing_seller.contact_number
          }
          payment_list = []

          all_payment = Payment.query.filter_by(seller_id= existing_seller.seller_id).all()

          for payment in all_payment:

               payment_dict = {
                              "payment_id"        : payment.payment_id,
                              "payment_date"      : str(payment.payment_date),
                              "amount_paid"       : round(float(payment.amount_paid),2),
                              "payment_method"    : payment.payment_method}
               
               payment_list.append(payment_dict)

          return jsonify({
                         "status"       : "success",
                         "seller_data"  : seller_dict,
                         "payment"      : payment_list
          }),200
     
     except Exception as e:
          print(e)
          return jsonify({
                         "status"  : "error",
                         "message" : "Internal server error"
          }), 500