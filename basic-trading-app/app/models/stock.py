from app import db

class Stock(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True)
    price = db.Column(db.Float)

    def json(self):
        return {
            'id': self.id,
            'name': self.name,
            'price': self.price
        }