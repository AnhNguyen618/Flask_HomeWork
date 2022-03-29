from flask import Flask
from app import routes
import os


SECRET_KEY = os.urandom(32)

myobj = Flask(__name__)

myobj.config['SECRET_KEY'] = SECRET_KEY

