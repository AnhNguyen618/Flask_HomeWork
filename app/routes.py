from flask import Flask
from flask import render_template
from flask import request
from flask import session
from flask import flash
from app import myhw_obj
from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms import SubmitField
from wtforms.validators import DataRequired

class SubmitForm(FlaskForm):
    city_name = StringField('City Name', validators=[DataRequired()])
    submit_button = SubmitField('Submit')

name = 'Lisa'
city_names = ["Paris","London","Rome","Tahiti"]

@myhw_obj.route('/', methods = ['GET','POST'])
def home():
    field = SubmitForm()
    if field.validate_on_submit():
        flash(f'{field.city_name.data}')

    return render_template('home.html',name = name, city_names = city_names, field = field)