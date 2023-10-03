#!/usr/bin/env python3

from flask import Flask, make_response
from flask_migrate import Migrate

from models import db, Hero,Power,HeroPower
from flask import Flask, request, make_response, jsonify
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///Superheroes.db'
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



@app.route('/heroes/<int:id>')
def hero_by_id(id):
    hero = Hero.query.get(id)
    if hero:
        hero_dict = {
            "id": hero.id,
            "name": hero.name,
            "super_name": hero.super_name

        }
        return jsonify(hero_dict), 200
    else:
        return jsonify({"error": "Hero not found"}), 404
    

    
@app.route('/powers', methods=['GET'])
def powers():
    if request.method == 'GET':
        powers = Power.query.all()

        return make_response(
            jsonify([power.to_dict() for power in powers]),
            200,
        )
   
@app.route('/powers/<int:id>')
def powers_by_id(id):
    power = Power.query.get(id)
    if not power:
        power_dict = {
            "id": power.id,
            "name": power.name,
            "description": power.description

        }
        return jsonify(power_dict), 200
    #else:
        #return jsonify({"error": "Power not found"}), 404
    elif request.method == 'PATCH':
        data = request.get_json()
        if "description" in data:
            power.description= data["Updated description"]
       
        db.session.commit()
        restaurant_dict = {
            "id": power.id,
            "name":power.name,
            "description":power.description
        }
        return jsonify(restaurant_dict), 200
    else:
        return jsonify({"error":"Validation errors"})
    



@app.route('/hero_powers', methods=['POST'])
def create_hero_power():
    data = request.get_json()

    if not all(key in data for key in ("strength", "power_id", "hero_id")):
        return jsonify({"errors": ["validation errors.include all keys"]}), 400
    #strength=data["strength"]
    hero_id = data["hero_id"]
    power_id = data["power_id"]

    hero = Hero.query.get(hero_id)
    power = Power.query.get(power_id)
    
    if not hero or not power:
        return jsonify({"errors": ["validation errors pizza and restaurant don't exist"]}), 400

    hero_powers = HeroPower(
        strength=data["strength"],
        hero_id=data["hero_id"],
        power_id=data["power_id"]
    )
    db.session.add(hero_powers)
    db.session.commit()

    power_data = {
        "id": power.id,
        "name": power.name,
        "description": power.description
    }

    return jsonify(power_data), 201
    

if __name__ == '__main__':
    app.run(port=5555)
