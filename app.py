from flask import Flask,render_template,url_for,request, redirect, send_from_directory
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from flask_migrate import Migrate
# from form import EmotionForm
import csv
import os

from flask_wtf import FlaskForm
from wtforms import RadioField, SubmitField

class EmotionForm(FlaskForm):
    happy_level = RadioField('Happy', choices=[('0', 'Option 0'),('1', 'Option 1'), ('2', 'Option 2'), ('3', 'Option 3'), ('4', 'Option 4'), ('5', 'Option 5')])
    sad_level = RadioField('Sad', choices=[ ('0', 'Option 0'), ('1', 'Option 1'), ('2', 'Option 2'), ('3', 'Option 3'), ('4', 'Option 4'), ('5', 'Option 5')])
    submit = SubmitField('Submit')



app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
# app.config['SECRET_KEY'] = "iloveeurus"
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

class Config(object):
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///test.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

db = SQLAlchemy(app)
migrate = Migrate(app,db)

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    content = db.Column(db.String(200), nullable=False)
    date_created = db.Column(db.DateTime, default = datetime.utcnow)

    def __repr__(self):
        return '<Task %r>' % self.id
    
class Data(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    happy_level = db.Column(db.String(10))
    sad_level = db.Column(db.String(10))

@app.route('/', methods=['GET', 'POST'])
# Here is something about URL
def index():
    form = EmotionForm()

    if form.validate_on_submit():
        data = Data(happy_level=form.happy_level.data, sad_level=form.sad_level.data)
        db.session.add(data)
        db.session.commit()
        # with open ("form_data.csv", "a", newline="") as file:
        #     writer = csv.writer(file)
        #     writer.writerow(['Happiness','Sadness'])
        #     writer.writerow([form.data['happy_level'], form.data['sad_level']])
        return redirect('/')
        # return "Hello"
    # Todo: need to change to the next page with url_for()
        # happy_level = form.happy_level.data
        # sad_level = form.sad_level.data
    return render_template('index.html',form=form)


if __name__ == "__main__":
    # app.run(host='0.0.0.0')
    app.run(debug=True)
# If any errors, they'll pop up on the web page, and we can see. 
    