from app import db

class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    stock_id = db.Column(db.Integer, db.ForeignKey('stock.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    quantity = db.Column(db.Integer)
    price = db.Column(db.Float)

    def json(self):
        return {
            'id': self.id,
            'stock_id': self.stock_id,
            'quantity': self.quantity,
            'price': self.price
        }