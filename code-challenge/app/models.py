from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import validates
db = SQLAlchemy()

class Hero(db.Model):
    __tablename__ = 'hero'

    id = db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String, unique=True, nullable=False)
    super_name=db.Column(db.String, unique=True, nullable=False)

    def __repr__(self):
        return f'Hero(id={self.id}, name={self.name},super_name={self.super_name})'



class Power(db.Model):
    __tablename__ = 'power'

    id = db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String, unique=True, nullable=False)
    description=db.Column(db.String, unique=True, nullable=False)


    
    def __repr__(self):
        return f'Power(id={self.id}, name={self.name},description={self.description})'
    
    @validates('description',)
    def validate_description(self,unique,value):
        if  not len(value)<20 :
            raise ValueError("Should be atleast 20 characters")
        return value
    

class HeroPower(db.Model):
    __tablename__ = 'heropower'

    strength = db.Column(db.Integer, primary_key=True)
    power_id=db.Column(db.Integer, db.ForeignKey('power.id'))
    hero_id=db.Column(db.Integer, db.ForeignKey('hero.id'))

#validations

    @validates('strength',)
    def validate_strength(self,unique,value):
             
            if not  'Strong' 'Weak' 'Average' in value:
                 raise ValueError("Name found please entre another name")
            return value
       
    
    def __repr__(self):
        return f'HeroPower(id={self.id}, power_id={self.power_id},hero_id={self.hero_id})'