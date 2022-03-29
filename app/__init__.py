from flask import Flask
import os

SECRET_KEY = os.urandom(32)

myobj = Flask(__name__)

myobj.config['SECRET_KEY'] = SECRET_KEY
from app import routes
