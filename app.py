from flask import Flask, request, jsonify
from flask_cors import CORS
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from models import db, Reservation
from datetime import datetime
from dotenv import load_dotenv
import os

app = Flask(__name__)
CORS(app)

load_dotenv(".env.local")  # .env.localファイルを読み込む

app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DATABASE_URL") or os.getenv("LOCAL_DATABASE_URL")
print("Using DATABASE_URL:", app.config["SQLALCHEMY_DATABASE_URI"])
DATABASE_URL = app.config["SQLALCHEMY_DATABASE_URI"]
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
migrate = Migrate(app, db)

@app.route('/')
def index():
    return 'Flask API is running.'



@app.route('/')
def index():
    return 'Flask API is running.'


@app.route('/api/reserve', methods=['POST'])
def reserve():
    data = request.get_json()
    try:
        new_reservation = Reservation(
            name=data["name"],
            phone=data["phone"],
            city=data["city"],
            status=data["status"],
            menu=data["menu"],
            datetime=data["datetime"]
        )
        db.session.add(new_reservation)
        db.session.commit()
        return jsonify({"message": "予約が保存されました"}), 200

    except Exception as e:
        print("エラー:", e)
        return jsonify({"error": "予約の保存に失敗しました"}), 500

if __name__ == '__main__':
    app.run(debug=True)