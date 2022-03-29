from flask import Flask
from flask import render_template
from flask import request
from flask import session
from flask import flash
from app import myobj
from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms import SubmitField
from wtforms.validators import DataRequired

class SubmitForm(FlaskForm):
    cityname = StringField('City Name', validators=[DataRequired()])
    submitButton = SubmitField('Submit')

name = 'Lisa'
city_names = ["Paris","London","Rome","Tahiti"]

@myobj.route('/', methods = ['GET','POST'])
def home():
    form = SubmitForm()
    if form.validate_on_submit():
        flash(f'{form.cityname.data}')

    return render_template('home.html', names = name, city_name = city_names, field = form)



