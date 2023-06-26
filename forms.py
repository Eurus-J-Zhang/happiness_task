from flask_wtf import FlaskForm
from wtforms import RadioField, SubmitField, StringField, IntegerField
from wtforms.validators import DataRequired, NumberRange

# Here is for Prolific ID and gender and age
class DemographicInfo(FlaskForm):
    id = StringField('Prolific ID', validators=[DataRequired()])
    gender = RadioField('Gender', choices=[('M','Male'),('F','Female'),('O','Others')], validators=[DataRequired()])
    age = IntegerField('Age', validators=[DataRequired(), NumberRange(min=18, max=80)])
    # submit = SubmitField('Submit')

# Here is the first emotion check
class EmotionForm1(FlaskForm):
    emo1_happiness = RadioField('Happiness*', choices=[('0', 'Opt0'),('1', 'Opt1'), ('2', 'Opt2'), 
                                               ('3', 'Opt3'), ('4', 'Opt4'), ('5', 'Opt5'),
                                               ('6', 'Opt6'), ('7', 'Opt7'), ('8', 'Opt8'),
                                               ('9', 'Opt9'), ('10', 'Opt10')], validators=[DataRequired()])
    emo1_pride = RadioField('Pride*', choices=[('0', 'Opt0'),('1', 'Opt1'), ('2', 'Opt2'), 
                                               ('3', 'Opt3'), ('4', 'Opt4'), ('5', 'Opt5'),
                                               ('6', 'Opt6'), ('7', 'Opt7'), ('8', 'Opt8'),
                                               ('9', 'Opt9'), ('10', 'Opt10')], validators=[DataRequired()])
    emo1_boredom = RadioField('Boredom*', choices=[('0', 'Opt0'),('1', 'Opt1'), ('2', 'Opt2'), 
                                               ('3', 'Opt3'), ('4', 'Opt4'), ('5', 'Opt5'),
                                               ('6', 'Opt6'), ('7', 'Opt7'), ('8', 'Opt8'),
                                               ('9', 'Opt9'), ('10', 'Opt10')], validators=[DataRequired()])
    
    emo1_sadness = RadioField('Sadness*', choices=[('0', 'Opt0'),('1', 'Opt1'), ('2', 'Opt2'), 
                                               ('3', 'Opt3'), ('4', 'Opt4'), ('5', 'Opt5'),
                                               ('6', 'Opt6'), ('7', 'Opt7'), ('8', 'Opt8'),
                                               ('9', 'Opt9'), ('10', 'Opt10')], validators=[DataRequired()])

    emo1_irritation = RadioField('Irritation*', choices=[('0', 'Opt0'),('1', 'Opt1'), ('2', 'Opt2'), 
                                               ('3', 'Opt3'), ('4', 'Opt4'), ('5', 'Opt5'),
                                               ('6', 'Opt6'), ('7', 'Opt7'), ('8', 'Opt8'),
                                               ('9', 'Opt9'), ('10', 'Opt10')], validators=[DataRequired()])  
    
# Second emotion check 
class EmotionForm2(FlaskForm):
    emo2_happiness = RadioField('Happiness*', choices=[('0', 'Opt0'),('1', 'Opt1'), ('2', 'Opt2'), 
                                               ('3', 'Opt3'), ('4', 'Opt4'), ('5', 'Opt5'),
                                               ('6', 'Opt6'), ('7', 'Opt7'), ('8', 'Opt8'),
                                               ('9', 'Opt9'), ('10', 'Opt10')], validators=[DataRequired()])
    emo2_pride = RadioField('Pride*', choices=[('0', 'Opt0'),('1', 'Opt1'), ('2', 'Opt2'), 
                                               ('3', 'Opt3'), ('4', 'Opt4'), ('5', 'Opt5'),
                                               ('6', 'Opt6'), ('7', 'Opt7'), ('8', 'Opt8'),
                                               ('9', 'Opt9'), ('10', 'Opt10')], validators=[DataRequired()])
    emo2_boredom = RadioField('Boredom*', choices=[('0', 'Opt0'),('1', 'Opt1'), ('2', 'Opt2'), 
                                               ('3', 'Opt3'), ('4', 'Opt4'), ('5', 'Opt5'),
                                               ('6', 'Opt6'), ('7', 'Opt7'), ('8', 'Opt8'),
                                               ('9', 'Opt9'), ('10', 'Opt10')], validators=[DataRequired()])
    
    emo2_sadness = RadioField('Sadness*', choices=[('0', 'Opt0'),('1', 'Opt1'), ('2', 'Opt2'), 
                                               ('3', 'Opt3'), ('4', 'Opt4'), ('5', 'Opt5'),
                                               ('6', 'Opt6'), ('7', 'Opt7'), ('8', 'Opt8'),
                                               ('9', 'Opt9'), ('10', 'Opt10')], validators=[DataRequired()])

    emo2_irritation = RadioField('Irritation*', choices=[('0', 'Opt0'),('1', 'Opt1'), ('2', 'Opt2'), 
                                               ('3', 'Opt3'), ('4', 'Opt4'), ('5', 'Opt5'),
                                               ('6', 'Opt6'), ('7', 'Opt7'), ('8', 'Opt8'),
                                               ('9', 'Opt9'), ('10', 'Opt10')], validators=[DataRequired()])  
  

# Third emotion check

class EmotionForm3(FlaskForm):
    emo3_happiness = RadioField('Happiness*', choices=[('0', 'Opt0'),('1', 'Opt1'), ('2', 'Opt2'), 
                                               ('3', 'Opt3'), ('4', 'Opt4'), ('5', 'Opt5'),
                                               ('6', 'Opt6'), ('7', 'Opt7'), ('8', 'Opt8'),
                                               ('9', 'Opt9'), ('10', 'Opt10')], validators=[DataRequired()])
    emo3_pride = RadioField('Pride*', choices=[('0', 'Opt0'),('1', 'Opt1'), ('2', 'Opt2'), 
                                               ('3', 'Opt3'), ('4', 'Opt4'), ('5', 'Opt5'),
                                               ('6', 'Opt6'), ('7', 'Opt7'), ('8', 'Opt8'),
                                               ('9', 'Opt9'), ('10', 'Opt10')], validators=[DataRequired()])
    emo3_boredom = RadioField('Boredom*', choices=[('0', 'Opt0'),('1', 'Opt1'), ('2', 'Opt2'), 
                                               ('3', 'Opt3'), ('4', 'Opt4'), ('5', 'Opt5'),
                                               ('6', 'Opt6'), ('7', 'Opt7'), ('8', 'Opt8'),
                                               ('9', 'Opt9'), ('10', 'Opt10')], validators=[DataRequired()])
    
    emo3_sadness = RadioField('Sadness*', choices=[('0', 'Opt0'),('1', 'Opt1'), ('2', 'Opt2'), 
                                               ('3', 'Opt3'), ('4', 'Opt4'), ('5', 'Opt5'),
                                               ('6', 'Opt6'), ('7', 'Opt7'), ('8', 'Opt8'),
                                               ('9', 'Opt9'), ('10', 'Opt10')], validators=[DataRequired()])

    emo3_irritation = RadioField('Irritation*', choices=[('0', 'Opt0'),('1', 'Opt1'), ('2', 'Opt2'), 
                                               ('3', 'Opt3'), ('4', 'Opt4'), ('5', 'Opt5'),
                                               ('6', 'Opt6'), ('7', 'Opt7'), ('8', 'Opt8'),
                                               ('9', 'Opt9'), ('10', 'Opt10')], validators=[DataRequired()])  
  

# Forth emotion check

class EmotionForm4(FlaskForm):
    emo4_happiness = RadioField('Happiness*', choices=[('0', 'Opt0'),('1', 'Opt1'), ('2', 'Opt2'), 
                                               ('3', 'Opt3'), ('4', 'Opt4'), ('5', 'Opt5'),
                                               ('6', 'Opt6'), ('7', 'Opt7'), ('8', 'Opt8'),
                                               ('9', 'Opt9'), ('10', 'Opt10')], validators=[DataRequired()])
    emo4_pride = RadioField('Pride*', choices=[('0', 'Opt0'),('1', 'Opt1'), ('2', 'Opt2'), 
                                               ('3', 'Opt3'), ('4', 'Opt4'), ('5', 'Opt5'),
                                               ('6', 'Opt6'), ('7', 'Opt7'), ('8', 'Opt8'),
                                               ('9', 'Opt9'), ('10', 'Opt10')], validators=[DataRequired()])
    emo4_boredom = RadioField('Boredom*', choices=[('0', 'Opt0'),('1', 'Opt1'), ('2', 'Opt2'), 
                                               ('3', 'Opt3'), ('4', 'Opt4'), ('5', 'Opt5'),
                                               ('6', 'Opt6'), ('7', 'Opt7'), ('8', 'Opt8'),
                                               ('9', 'Opt9'), ('10', 'Opt10')], validators=[DataRequired()])
    
    emo4_sadness = RadioField('Sadness*', choices=[('0', 'Opt0'),('1', 'Opt1'), ('2', 'Opt2'), 
                                               ('3', 'Opt3'), ('4', 'Opt4'), ('5', 'Opt5'),
                                               ('6', 'Opt6'), ('7', 'Opt7'), ('8', 'Opt8'),
                                               ('9', 'Opt9'), ('10', 'Opt10')], validators=[DataRequired()])

    emo4_irritation = RadioField('Irritation*', choices=[('0', 'Opt0'),('1', 'Opt1'), ('2', 'Opt2'), 
                                               ('3', 'Opt3'), ('4', 'Opt4'), ('5', 'Opt5'),
                                               ('6', 'Opt6'), ('7', 'Opt7'), ('8', 'Opt8'),
                                               ('9', 'Opt9'), ('10', 'Opt10')], validators=[DataRequired()])  
  