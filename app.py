#from typing_extensions import Required
import os
from flask import Flask
import flask_restful as restful
from flask_restful import Api
from flask_jwt import JWT
from security import authenticate, identity
from resources.user import UserRegister
from resources.item import Item, ItemList
from resources.store import Store, StoreList



app = Flask(__name__)
# We are disabling Flask-SQLAlchemy modification tracer but it does not turn off 
#SQLAlchemy modification tracker
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL') #'sqlite:///noman.db'(use this as second argument for local development)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'jose'
api = Api(app)

#This will allow app to creare database and table when first requets arrive

jwt = JWT(app, authenticate, identity) # /auth

api.add_resource(Store, '/store/<string:name>')
api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')
api.add_resource(StoreList, '/stores') 
api.add_resource(UserRegister, '/register')

if __name__ =='__main__': #This statement makes it explicit run not implicit
    from db import db
    db.init_app(app)
    app.run(port=5000, debug=True)