from models import db
from app import app  # Flaskアプリのインスタンスをimport

with app.app_context():
    db.create_all()
    print("Reservation テーブルを作成しました。")