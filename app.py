from flask import Flask
from flask_restful import  Api
from opskit_api.resources.helloworld import HelloWorld 

app = Flask(__name__)
api = Api(app)

api.add_resource(HelloWorld, '/')


