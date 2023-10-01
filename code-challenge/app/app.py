#!/usr/bin/env python3

from flask import Flask, make_response
from flask_migrate import Migrate

from models import db, Hero,Power
from flask import Flask, request, make_response, jsonify
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db/app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

migrate = Migrate(app, db)

db.init_app(app)

@app.route('/')
def home():
    return 'These are my superheroes'


@app.route('/heroes', methods=['GET'])
def heroes():
    if request.method == 'GET':
        heroes = Hero.query.all()

        return make_response(
            jsonify([heroe.to_dict() for heroe in heroes]),
            200,
        )
    
@app.route('/powers', methods=['GET'])
def powers():
    if request.method == 'GET':
        powers = Power.query.all()

        return make_response(
            jsonify([power.to_dict() for power in powers]),
            200,
        )
   


if __name__ == '__main__':
    app.run(port=5555)
