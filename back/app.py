from flask import Flask
from flask_cors import CORS
import os
import socket
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
cors = CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://jrubics:mikimaus@dm1ncziw1eqaezi.chufvojjuy0q.eu-central-1.rds.amazonaws.com:5432/MyDatabase'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test1.db'
db = SQLAlchemy(app)

class VisitsModel(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    number = db.Column(db.Integer(), unique=False)

db.create_all()

@app.route("/")
def hello():
    num = 0
    try:
        visits = VisitsModel.query.filter_by(id=1).first()
        visits.number +=1
        db.session.commit()
        num = visits.number
    except:
        new = VisitsModel(id=1,number=1)
        db.session.add(new)
        db.session.commit()
        num = 1
    
    html = "<b>Visits: {num}</b>"
    return html.format(num=num)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)

