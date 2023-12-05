from app.order import bp
from app import db
from app.models.order import Order
from app.models.stock import Stock
from flask import request, jsonify

from app.user.service import AuthService
from app.order.schema.create_order_schema import CreateOrderSchema

@bp.route('/order', methods=['POST'])
def create_order():
    
    create_order_schema = CreateOrderSchema()
    errors = create_order_schema.validate(request.json)
    
    if errors:
        return {'message' : errors}, 400    
    
    data = request.json    
    
    stock = Stock.query.filter_by(id=data['stock_id']).first()
    if stock is None:
        return {'code': 400, 'message': 'Stock not found'}        

    auth_user = AuthService.get_auth_user(request)
    order = Order(stock_id=data['stock_id'], user_id=auth_user['user']['id'], quantity=data['quantity'], price=data['price'])

    db.session.add(order)
    
    try:
        db.session.commit()
        return jsonify({'code' : 200, 'message': 'Order placed successfully'}), 201
    except Exception as e:
        return {'code': 400, 'message': str(e)}
    
@bp.route('/portfolio', methods=['GET'])
@bp.route('/portfolio/<int:stock_id>', methods=['GET'])
def get_portfolio(stock_id=None):
    auth_user = AuthService.get_auth_user(request)
    if stock_id:    
        stock = Stock.query.filter_by(id=stock_id).first()
        if stock is None:
            return {'code': 400, 'message': 'Stock not found'}        
        
        orders = Order.query.filter_by(user_id=auth_user['user']['id'], stock_id=stock_id).all()
        json_stock = stock.json()
        total_value = sum(order.quantity * order.price for order in orders)        

        return jsonify({
            'name' : auth_user['user']['username'], 
            'stock': json_stock['name'],
            'total_orders' : len(orders),
            'total_investment': total_value
        })
    else:
        orders = Order.query.filter_by(user_id=auth_user['user']['id']).all()
        total_value = sum(order.quantity * order.price for order in orders)       
        return jsonify({
            'name' : auth_user['user']['username'], 
            'total_orders' : len(orders),
            'total_investment': total_value
        })
