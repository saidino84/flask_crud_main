from flask import Flask,jsonify,flash
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow  import Marshmallow
import os

app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.secret_key=os.urandom(12).hex()
print(os.urandom(12).hex())
db = SQLAlchemy(app)
ma = Marshmallow(app)
class User(db.Model):
    id =  db.Column(db.Integer, primary_key=True)
    name =db.Column(db.String(50))
    def __repr__(self):
        return f'User(id={id} name={name} rewards={self.rewards})'

    def to_json(self):
        return {'id':self.id, 'name':self.name}


class Reward(db.Model):
    id =db.Column(db.Integer, primary_key=True)
    reward_name = db.Column(db.String(250))
    user_id =db.Column(db.Integer, db.ForeignKey('user.id'))
    user =db.relationship('User', backref='rewards')

    def __repr__(self):
        return 'Reward(id={id} , rewnme={reward_name}, user_id={user_id})'

class UserSchema(ma.ModelSchema):
    class Meta:
        model= User

class Reward(ma.ModelSchema):
    class Meta:
        model = Reward

@app.route('/')
def get_first():
    user=User.query.first()
    user_schema=UserSchema()
    output=user_schema.dumo(User).data
    return jsonify({'user':output})

# todo obtendo user auto serializavel sem ajuda de Marshmallow
@app.route('/first',methods=['GET'])
def index():
    user =User.query.first()
    print(user.to_json())
    return jsonify(user.to_json())
@app.route('/flash')
def makeflash():
    flash('This is flas messa')
    return 'Flasings'




if __name__=='__main__':
    app.run(debug=True, host='0.0.0.0')

