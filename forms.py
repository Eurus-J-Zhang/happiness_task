from flask_wtf import FlaskForm
from wtforms import RadioField, SubmitField, StringField, IntegerField
from wtforms.validators import DataRequired, NumberRange
from wtforms.widgets import TextArea

# Here is for Prolific ID and gender and age
class DemographicInfo(FlaskForm):
    id = StringField('Prolific ID', validators=[DataRequired()])
    gender = RadioField('Gender', choices=[('M','Male'),('F','Female'),('O','Others')], validators=[DataRequired()])
    age = IntegerField('Age', validators=[DataRequired(), NumberRange(min=18, max=80)])

eleven_point_scale = [(str(i), f'Opt{i}') for i in range(11)]

# Here is the first emotion check
class EmotionForm1(FlaskForm):
    emo1_happiness = RadioField('Happiness', choices=[('0', 'Opt0'),('1', 'Opt1'), ('2', 'Opt2'), 
                                ('3', 'Opt3'), ('4', 'Opt4'), ('5', 'Opt5'),('6', 'Opt6'), ('7', 'Opt7'), 
                                ('8', 'Opt8'), ('9', 'Opt9'), ('10', 'Opt10')], validators=[DataRequired()])
    emo1_joy = RadioField('Joy', choices=eleven_point_scale, validators=[DataRequired()])
    emo1_boredom = RadioField('Boredom', choices=eleven_point_scale, validators=[DataRequired()])
    emo1_sadness = RadioField('Sadness', choices=eleven_point_scale, validators=[DataRequired()])
    emo1_irritation = RadioField('Irritation', choices=eleven_point_scale, validators=[DataRequired()])  
    
# Second emotion check 
class EmotionForm2(FlaskForm):
    emo2_happiness = RadioField('Happiness', choices=eleven_point_scale, validators=[DataRequired()])
    emo2_joy = RadioField('Joy', choices=eleven_point_scale, validators=[DataRequired()])
    emo2_boredom = RadioField('Boredom', choices=eleven_point_scale, validators=[DataRequired()])
    emo2_sadness = RadioField('Sadness', choices=eleven_point_scale, validators=[DataRequired()])
    emo2_irritation = RadioField('Irritation', choices=eleven_point_scale, validators=[DataRequired()])  
  

# Third emotion check
class EmotionForm3(FlaskForm):
    emo3_happiness = RadioField('Happiness', choices=eleven_point_scale, validators=[DataRequired()])
    emo3_joy = RadioField('Joy', choices=eleven_point_scale, validators=[DataRequired()])
    emo3_boredom = RadioField('Boredom', choices=eleven_point_scale, validators=[DataRequired()])
    emo3_sadness = RadioField('Sadness', choices=eleven_point_scale, validators=[DataRequired()])
    emo3_irritation = RadioField('Irritation', choices=eleven_point_scale, validators=[DataRequired()])  
  

# Forth emotion check
class EmotionForm4(FlaskForm):
    emo4_happiness = RadioField('Happiness', choices=eleven_point_scale, validators=[DataRequired()])
    emo4_joy = RadioField('Joy', choices=eleven_point_scale, validators=[DataRequired()])
    emo4_boredom = RadioField('Boredom', choices=eleven_point_scale, validators=[DataRequired()])
    emo4_sadness = RadioField('Sadness', choices=eleven_point_scale, validators=[DataRequired()])
    emo4_irritation = RadioField('Irritation', choices=eleven_point_scale, validators=[DataRequired()])  
  
# Feedback collecting 
class FeedbackForm(FlaskForm):
    feedback = StringField('',validators=[DataRequired()],widget=TextArea())