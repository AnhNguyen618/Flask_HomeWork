from flask import Flask
import os

SECRET_KEY = os.urandom(32)

myhw_obj = Flask(__name__)

myhw_obj.config['SECRET_KEY'] = SECRET_KEY
from app import routes
