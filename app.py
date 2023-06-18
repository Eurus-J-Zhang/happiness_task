from flask import Flask,render_template,url_for,request, redirect, send_from_directory, session
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from flask_migrate import Migrate
# from form import EmotionForm
import csv
import os
import pymysql


from flask_wtf import FlaskForm
from wtforms import RadioField, SubmitField, StringField, IntegerField
from wtforms.validators import DataRequired, NumberRange

# Here is for Prolific ID and gender and age
class DemographicInfo(FlaskForm):
    id = StringField('Prolific ID', validators=[DataRequired()])
    gender = RadioField('Gender', choices=[('M','Male'),('F','Female'),('O','Others')], validators=[DataRequired()])
    age = IntegerField('Age', validators=[DataRequired(), NumberRange(min=18, max=80)])
    # submit = SubmitField('Submit')

# Here is the initial emotion check
class EmotionForm(FlaskForm):
    happiness_level = RadioField('Happiness*', choices=[('0', 'Opt0'),('1', 'Opt1'), ('2', 'Opt2'), 
                                               ('3', 'Opt3'), ('4', 'Opt4'), ('5', 'Opt5'),
                                               ('6', 'Opt6'), ('7', 'Opt7'), ('8', 'Opt8'),
                                               ('9', 'Opt9'), ('10', 'Opt10')], validators=[DataRequired()])
    pride_level = RadioField('Pride*', choices=[('0', 'Opt0'),('1', 'Opt1'), ('2', 'Opt2'), 
                                               ('3', 'Opt3'), ('4', 'Opt4'), ('5', 'Opt5'),
                                               ('6', 'Opt6'), ('7', 'Opt7'), ('8', 'Opt8'),
                                               ('9', 'Opt9'), ('10', 'Opt10')], validators=[DataRequired()])
    boredom_level = RadioField('Boredom*', choices=[('0', 'Opt0'),('1', 'Opt1'), ('2', 'Opt2'), 
                                               ('3', 'Opt3'), ('4', 'Opt4'), ('5', 'Opt5'),
                                               ('6', 'Opt6'), ('7', 'Opt7'), ('8', 'Opt8'),
                                               ('9', 'Opt9'), ('10', 'Opt10')], validators=[DataRequired()])
    
    sadness_level = RadioField('Sadness*', choices=[('0', 'Opt0'),('1', 'Opt1'), ('2', 'Opt2'), 
                                               ('3', 'Opt3'), ('4', 'Opt4'), ('5', 'Opt5'),
                                               ('6', 'Opt6'), ('7', 'Opt7'), ('8', 'Opt8'),
                                               ('9', 'Opt9'), ('10', 'Opt10')], validators=[DataRequired()])

    irritation_level = RadioField('Irritation*', choices=[('0', 'Opt0'),('1', 'Opt1'), ('2', 'Opt2'), 
                                               ('3', 'Opt3'), ('4', 'Opt4'), ('5', 'Opt5'),
                                               ('6', 'Opt6'), ('7', 'Opt7'), ('8', 'Opt8'),
                                               ('9', 'Opt9'), ('10', 'Opt10')], validators=[DataRequired()])  

pymysql.install_as_MySQLdb()

# Here is about configuration
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('JAWSDB_URL')or 'sqlite:///test.db'
app.config['SECRET_KEY'] = "iloveeurus"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# class Config(object):
#     SQLALCHEMY_DATABASE_URI = os.environ.get('JAWSDB_URL') or 'sqlite:///test.db'
#     SQLALCHEMY_TRACK_MODIFICATIONS = False

db = SQLAlchemy(app)
migrate = Migrate(app,db)

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    content = db.Column(db.String(200), nullable=False)
    date_created = db.Column(db.DateTime, default = datetime.utcnow)

    def __repr__(self):
        return '<Task %r>' % self.id
    
class Data(db.Model):
    number = db.Column(db.Integer, primary_key=True)
    id= db.Column(db.String(20))
    gender=db.Column(db.String(10))
    age = db.Column(db.Integer)
    happiness_level = db.Column(db.String(10))
    pride_level = db.Column(db.String(10))
    boredom_level = db.Column(db.String(10))
    sadness_level = db.Column(db.String(10))
    irritation_level = db.Column(db.String(10))


@app.route('/', methods=['GET', 'POST'])
def index():
    form = DemographicInfo()
    if form.validate_on_submit():
        data = form.data
        data.pop('csrf_token', None)
        session['index_data'] = data
        return redirect(url_for('page1'))
    return render_template('index.html',form=form)

@app.route('/page1', methods=['GET', 'POST'])
def page1():
    form = EmotionForm()
    if form.validate_on_submit():
        data = form.data
        data.pop('csrf_token', None)
        session['page1_data'] = data

        # session['page1_data'] = {'happiness_level': form.happiness_level.data, 'sadness_level': form.sadness_level.data}
        index_data = session.get('index_data')
        page1_data = session.get('page1_data')
        if index_data:
            combined_data = {**index_data, **page1_data}
        data = Data(**combined_data)
        db.session.add(data)
        db.session.commit()
        return redirect('page_end')
    return render_template('page1.html',form=form)

@app.route('/page_end')
def page_end():
    return render_template('page_end.html')


if __name__ == "__main__":
    # app.run(host='0.0.0.0')
    app.run(debug=True)
# If any errors, they'll pop up on the web page, and we can see. 
    