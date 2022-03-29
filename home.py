from flask import Flask
from flask import render_template
from flask import request
from flask import session
from flask import abort
from flask import flash
import os


app_obj = Flask(__name__)

app_obj.config['DEBUG'] =True

name = 'Lisa'

city_names = ["Paris","London","Rome","Tahiti"]

@app_obj.route('/')
def home():
    return f'''<html>
    <head>
        <title>Homework 3 - Flask </title>
    </head>
    <body>
        <h1>Welcome {name}!</h1>
        <p>
            <a href ="www.google.com">not google</a>
        <ul>
            <li>{city_names[0]}</li>
            <li>{city_names[1]}</li>
            <li>{city_names[2]}</li>
            <li>{city_names[3]}</li>
        </ul>
        </p>
    </body>
</html>'''

#app_obj.run()


