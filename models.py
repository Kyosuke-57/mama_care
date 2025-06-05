from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Reservation(db.Model):
    __tablename__ = 'reservations'  # 明示的にテーブル名を指定してもOK
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    phone = db.Column(db.String(20), nullable=False)
    city = db.Column(db.String(100), nullable=False)
    status = db.Column(db.String(100), nullable=False)
    menu = db.Column(db.Text, nullable=False)
    datetime = db.Column(db.String(50), nullable=False)