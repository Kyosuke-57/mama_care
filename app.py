from flask import Flask, request, jsonify
from flask_cors import CORS
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Reservation
from datetime import datetime
import os


app = Flask(__name__)
CORS(app)
app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DATABASE_URL") or "postgresql://mama_care_user:hukasigi7@localhost/mamacare_db"
DATABASE_URL = app.config["SQLALCHEMY_DATABASE_URI"]

# SQLAlchemyセットアップ
engine = create_engine(DATABASE_URL, echo=True)
Base.metadata.create_all(engine)  # テーブル作成
Session = sessionmaker(bind=engine)

@app.route('/api/reserve', methods=['POST'])
def reserve():
    data = request.get_json()
    name = data.get('name')
    date = data.get('date')
    message = data.get('message')

    try:
        # 日付を文字列からDate型に変換
        date_obj = datetime.strptime(date, "%Y-%m-%d").date()

        # 新しい予約データの作成
        new_reservation = Reservation(name=name, date=date_obj, message=message)

        # データベースに保存
        session = Session()
        session.add(new_reservation)
        session.commit()
        session.close()

        return jsonify({'message': '予約を受け付けました！'}), 200
    except Exception as e:
        print("エラー:", e)
        return jsonify({'message': 'エラーが発生しました'}), 500

if __name__ == '__main__':
    app.run(debug=True)