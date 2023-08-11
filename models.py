from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Data(db.Model):
    number = db.Column(db.Integer, primary_key=True)
    id= db.Column(db.String(20))
    gender=db.Column(db.String(10))
    age = db.Column(db.Integer)

    emo1_happiness = db.Column(db.Integer)
    emo1_joy = db.Column(db.Integer)
    emo1_boredom = db.Column(db.Integer)
    emo1_sadness = db.Column(db.Integer)
    emo1_irritation = db.Column(db.Integer)

    emo2_happiness = db.Column(db.Integer)
    emo2_joy = db.Column(db.Integer)
    emo2_boredom = db.Column(db.Integer)
    emo2_sadness = db.Column(db.Integer)
    emo2_irritation = db.Column(db.Integer)

    emo3_happiness = db.Column(db.Integer)
    emo3_joy = db.Column(db.Integer)
    emo3_boredom = db.Column(db.Integer)
    emo3_sadness = db.Column(db.Integer)
    emo3_irritation = db.Column(db.Integer)

    emo4_happiness = db.Column(db.Integer)
    emo4_joy = db.Column(db.Integer)
    emo4_boredom = db.Column(db.Integer)
    emo4_sadness = db.Column(db.Integer)
    emo4_irritation = db.Column(db.Integer)

    feedback = db.Column(db.String(200))