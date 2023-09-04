import datetime
from flask import Flask
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from pymongo.mongo_client import MongoClient
from .basepydanticmodels import *

app=Flask(__name__)
app.secret_key = "oneassuretest"
jwt = JWTManager(app) # initialize JWTManager
app.config['JWT_SECRET_KEY'] = '38dd56f56d405e02ec0ba4be4607eaab'
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = datetime.timedelta(days=1) # define the life span of the token
CORS(app)

uri = "mongodb+srv://harshnaicker:harshnaicker@oneassure-insurancerate.bqtjybf.mongodb.net/?retryWrites=true&w=majority"

# Create a new client and connect to the server
client = MongoClient(uri)
db = client.OneAssure

insurance_rates_collection = db['InsuranceRates']
users_collection = db['Users']
purchases_collection = db['Purchases']

from OneAssureInsurance.core.views import core
from OneAssureInsurance.users.views import users

app.register_blueprint(core)
app.register_blueprint(users)