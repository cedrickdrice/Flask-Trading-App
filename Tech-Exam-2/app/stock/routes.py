from app.stock import bp
from app.models.stock import Stock
from flask import jsonify

@bp.route('/stocks', methods=['GET'])
def get_stocks():
    stocks = Stock.query.all()
    data = [{'id': stock.id, 'name': stock.name, 'price': stock.price} for stock in stocks]    
    return jsonify({'code' : 200, 'stocks': data}), 200

@bp.route('/stock/<int:stock_id>', methods=['GET'])
def get_stock(stock_id):
    stock = Stock.query.filter(Stock.id == stock_id).first()
    
    if not stock:
        return jsonify({'code' : 400, 'message': 'Stock not found'}), 404
    
    return jsonify({'code' : 200, 'data': stock.json()}), 200
