from flask import Flask,render_template,url_for,request, redirect, send_from_directory, session
from flask_migrate import Migrate
from forms import EmotionForm1
from forms import EmotionForm2
from forms import EmotionForm3
from forms import EmotionForm4
from forms import FeedbackForm
from forms import DemographicInfo
import os
import pymysql
from models import db, Data

pymysql.install_as_MySQLdb()

# Here is about configuration


def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('JAWSDB_URL') or 'sqlite:///test.db'
    app.config['SECRET_KEY'] = "iloveeurus"
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    # migrate = Migrate(app,db)

    # with app.app_context():
    #     db.drop_all()
    #     db.create_all()

    return app

app = create_app()


@app.route('/', methods=['GET', 'POST'])
def index():
    form = DemographicInfo()
    if form.validate_on_submit():
        data = form.data
        data.pop('csrf_token', None)
        session['index_data'] = data
        return redirect(url_for('emo1'))
    return render_template('index.html',form=form)

@app.route('/emo1', methods=['GET', 'POST'])
def emo1():
    form = EmotionForm1()
    if form.validate_on_submit():
        data = form.data
        data.pop('csrf_token', None)
        session['page1_data'] = data
        return redirect('q1')
    return render_template('emo1.html',form=form)


@app.route('/emo2', methods=['GET', 'POST'])
def emo2():
    form = EmotionForm2()
    if form.validate_on_submit():
        data = form.data
        data.pop('csrf_token', None)
        session['page2_data'] = data
        return redirect('q12')
    return render_template('emo2.html',form=form)

@app.route('/emo3', methods=['GET', 'POST'])
def emo3():
    form = EmotionForm3()
    if form.validate_on_submit():
        data = form.data
        data.pop('csrf_token', None)
        session['page3_data'] = data
        return redirect('q23')
    return render_template('emo3.html',form=form)


@app.route('/emo4', methods=['GET', 'POST'])
def emo4():
    form = EmotionForm4()
    if form.validate_on_submit():
        data = form.data
        data.pop('csrf_token', None)
        session['page4_data'] = data
        return redirect('emo_end')
    return render_template('emo4.html',form=form)

@app.route('/emo_end', methods=['GET', 'POST'])
def emo_end():
    form = FeedbackForm()
    if form.validate_on_submit():
        data = form.data
        data.pop('csrf_token', None)
        session['page_end_data'] = data

        index_data = session.get('index_data')
        page1_data = session.get('page1_data')
        page2_data = session.get('page2_data')
        page3_data = session.get('page3_data')
        page4_data = session.get('page4_data')
        page_end_data = session.get('page_end_data')
        
        combined_data = {**index_data, **page1_data, **page2_data, **page3_data, **page4_data, **page_end_data}
        data = Data(**combined_data)
        db.session.add(data)
        db.session.commit()

        return redirect('page_end')
    return render_template('emo_end.html',form=form)

# Q1
@app.route('/q1', methods=['GET', 'POST'])
def q1():
    if request.method == 'POST':
        answer = request.form['answer']
        if answer == 'A':
            result = 'correct'
        else:
            result = 'wrong'
        return render_template('q1r.html', result=result, answer=answer)
    return render_template('q1.html')

@app.route('/q1r')
def q1r():
    return render_template('q1r.html')

# Q2
@app.route('/q2', methods=['GET', 'POST'])
def q2():
    if request.method == 'POST':
        answer = request.form['answer']
        if answer == 'A':
            result = 'correct'
        else:
            result = 'wrong'
        return render_template('q2r.html', result=result, answer=answer)
    return render_template('q2.html')

@app.route('/q2r')
def q2r():
    return render_template('q2r.html')

# Q3
@app.route('/q3', methods=['GET', 'POST'])
def q3():
    if request.method == 'POST':
        answer = request.form['answer']
        if answer == 'B':
            result = 'correct'
        else:
            result = 'wrong'
        return render_template('q3r.html', result=result, answer=answer)
    return render_template('q3.html')

@app.route('/q3r')
def q3r():
    return render_template('q3r.html')

# Q4
@app.route('/q4', methods=['GET', 'POST'])
def q4():
    if request.method == 'POST':
        answer = request.form['answer']
        if answer == 'A':
            result = 'correct'
        else:
            result = 'wrong'
        return render_template('q4r.html', result=result, answer=answer)
    return render_template('q4.html')

@app.route('/q4r')
def q4r():
    return render_template('q4r.html')

# Q5
@app.route('/q5', methods=['GET', 'POST'])
def q5():
    if request.method == 'POST':
        answer = request.form['answer']
        if answer == 'B':
            result = 'correct'
        else:
            result = 'wrong'
        return render_template('q5r.html', result=result, answer=answer)
    return render_template('q5.html')

@app.route('/q5r')
def q5r():
    return render_template('q5r.html')

# Q6
@app.route('/q6', methods=['GET', 'POST'])
def q6():
    if request.method == 'POST':
        answer = request.form['answer']
        if answer == 'B':
            result = 'correct'
        else:
            result = 'wrong'
        return render_template('q6r.html', result=result, answer=answer)
    return render_template('q6.html')

@app.route('/q6r')
def q6r():
    return render_template('q6r.html')

# Q7
@app.route('/q7', methods=['GET', 'POST'])
def q7():
    if request.method == 'POST':
        answer = request.form['answer']
        if answer == 'A':
            result = 'correct'
        else:
            result = 'wrong'
        return render_template('q7r.html', result=result, answer=answer)
    return render_template('q7.html')

@app.route('/q7r')
def q7r():
    return render_template('q7r.html')

# Q8
@app.route('/q8', methods=['GET', 'POST'])
def q8():
    if request.method == 'POST':
        answer = request.form['answer']
        if answer == 'B':
            result = 'correct'
        else:
            result = 'wrong'
        return render_template('q8r.html', result=result, answer=answer)
    return render_template('q8.html')

@app.route('/q8r')
def q8r():
    return render_template('q8r.html')

# Q9
@app.route('/q9', methods=['GET', 'POST'])
def q9():
    if request.method == 'POST':
        answer = request.form['answer']
        if answer == 'A':
            result = 'correct'
        else:
            result = 'wrong'
        return render_template('q9r.html', result=result, answer=answer)
    return render_template('q9.html')

@app.route('/q9r')
def q9r():
    return render_template('q9r.html')

# Q10
@app.route('/q10', methods=['GET', 'POST'])
def q10():
    if request.method == 'POST':
        answer = request.form['answer']
        if answer == 'B':
            result = 'correct'
        else:
            result = 'wrong'
        return render_template('q10r.html', result=result, answer=answer)
    return render_template('q10.html')

@app.route('/q10r')
def q10r():
    return render_template('q10r.html')

# Q11
@app.route('/q11', methods=['GET', 'POST'])
def q11():
    if request.method == 'POST':
        answer = request.form['answer']
        if answer == 'A':
            result = 'correct'
        else:
            result = 'wrong'
        return render_template('q11r.html', result=result, answer=answer)
    return render_template('q11.html')

@app.route('/q11r')
def q11r():
    return render_template('q11r.html')




# Q12
@app.route('/q12', methods=['GET', 'POST'])
def q12():
    if request.method == 'POST':
        answer = request.form['answer']
        if answer == 'A':
            result = 'correct'
        else:
            result = 'wrong'
        return render_template('q12r.html', result=result, answer=answer)
    return render_template('q12.html')

@app.route('/q12r')
def q12r():
    return render_template('q12r.html')

# Q13
@app.route('/q13', methods=['GET', 'POST'])
def q13():
    if request.method == 'POST':
        answer = request.form['answer']
        if answer == 'B':
            result = 'correct'
        else:
            result = 'wrong'
        return render_template('q13r.html', result=result, answer=answer)
    return render_template('q13.html')

@app.route('/q13r')
def q13r():
    return render_template('q13r.html')

# Q14
@app.route('/q14', methods=['GET', 'POST'])
def q14():
    if request.method == 'POST':
        answer = request.form['answer']
        if answer == 'A':
            result = 'correct'
        else:
            result = 'wrong'
        return render_template('q14r.html', result=result, answer=answer)
    return render_template('q14.html')

@app.route('/q14r')
def q14r():
    return render_template('q14r.html')

# Q15
@app.route('/q15', methods=['GET', 'POST'])
def q15():
    if request.method == 'POST':
        answer = request.form['answer']
        if answer == 'B':
            result = 'correct'
        else:
            result = 'wrong'
        return render_template('q15r.html', result=result, answer=answer)
    return render_template('q15.html')

@app.route('/q15r')
def q15r():
    return render_template('q15r.html')

# Q16
@app.route('/q16', methods=['GET', 'POST'])
def q16():
    if request.method == 'POST':
        answer = request.form['answer']
        if answer == 'B':
            result = 'correct'
        else:
            result = 'wrong'
        return render_template('q16r.html', result=result, answer=answer)
    return render_template('q16.html')

@app.route('/q16r')
def q16r():
    return render_template('q16r.html')

# Q17
@app.route('/q17', methods=['GET', 'POST'])
def q17():
    if request.method == 'POST':
        answer = request.form['answer']
        if answer == 'B':
            result = 'correct'
        else:
            result = 'wrong'
        return render_template('q17r.html', result=result, answer=answer)
    return render_template('q17.html')

@app.route('/q17r')
def q17r():
    return render_template('q17r.html')


# Q18
@app.route('/q18', methods=['GET', 'POST'])
def q18():
    if request.method == 'POST':
        answer = request.form['answer']
        if answer == 'B':
            result = 'correct'
        else:
            result = 'wrong'
        return render_template('q18r.html', result=result, answer=answer)
    return render_template('q18.html')

@app.route('/q18r')
def q18r():
    return render_template('q18r.html')

# Q19
@app.route('/q19', methods=['GET', 'POST'])
def q19():
    if request.method == 'POST':
        answer = request.form['answer']
        if answer == 'A':
            result = 'correct'
        else:
            result = 'wrong'
        return render_template('q19r.html', result=result, answer=answer)
    return render_template('q19.html')

@app.route('/q19r')
def q19r():
    return render_template('q19r.html')

# Q20
@app.route('/q20', methods=['GET', 'POST'])
def q20():
    if request.method == 'POST':
        answer = request.form['answer']
        if answer == 'B':
            result = 'correct'
        else:
            result = 'wrong'
        return render_template('q20r.html', result=result, answer=answer)
    return render_template('q20.html')

@app.route('/q20r')
def q20r():
    return render_template('q20r.html')

# Q21
@app.route('/q21', methods=['GET', 'POST'])
def q21():
    if request.method == 'POST':
        answer = request.form['answer']
        if answer == 'B':
            result = 'correct'
        else:
            result = 'wrong'
        return render_template('q21r.html', result=result, answer=answer)
    return render_template('q21.html')

@app.route('/q21r')
def q21r():
    return render_template('q21r.html')

# Q22
@app.route('/q22', methods=['GET', 'POST'])
def q22():
    if request.method == 'POST':
        answer = request.form['answer']
        if answer == 'A':
            result = 'correct'
        else:
            result = 'wrong'
        return render_template('q22r.html', result=result, answer=answer)
    return render_template('q22.html')

@app.route('/q22r')
def q22r():
    return render_template('q22r.html')

# Q23
@app.route('/q23', methods=['GET', 'POST'])
def q23():
    if request.method == 'POST':
        answer = request.form['answer']
        if answer == 'A':
            result = 'correct'
        else:
            result = 'wrong'
        return render_template('q23r.html', result=result, answer=answer)
    return render_template('q23.html')

@app.route('/q23r')
def q23r():
    return render_template('q23r.html')

# Q24
@app.route('/q24', methods=['GET', 'POST'])
def q24():
    if request.method == 'POST':
        answer = request.form['answer']
        if answer == 'A':
            result = 'correct'
        else:
            result = 'wrong'
        return render_template('q24r.html', result=result, answer=answer)
    return render_template('q24.html')

@app.route('/q24r')
def q24r():
    return render_template('q24r.html')

# Q25
@app.route('/q25', methods=['GET', 'POST'])
def q25():
    if request.method == 'POST':
        answer = request.form['answer']
        if answer == 'A':
            result = 'correct'
        else:
            result = 'wrong'
        return render_template('q25r.html', result=result, answer=answer)
    return render_template('q25.html')

@app.route('/q25r')
def q25r():
    return render_template('q25r.html')

# Q26
@app.route('/q26', methods=['GET', 'POST'])
def q26():
    if request.method == 'POST':
        answer = request.form['answer']
        if answer == 'A':
            result = 'correct'
        else:
            result = 'wrong'
        return render_template('q26r.html', result=result, answer=answer)
    return render_template('q26.html')

@app.route('/q26r')
def q26r():
    return render_template('q26r.html')

# Q27
@app.route('/q27', methods=['GET', 'POST'])
def q27():
    if request.method == 'POST':
        answer = request.form['answer']
        if answer == 'A':
            result = 'correct'
        else:
            result = 'wrong'
        return render_template('q27r.html', result=result, answer=answer)
    return render_template('q27.html')

@app.route('/q27r')
def q27r():
    return render_template('q27r.html')

# Q28
@app.route('/q28', methods=['GET', 'POST'])
def q28():
    if request.method == 'POST':
        answer = request.form['answer']
        if answer == 'B':
            result = 'correct'
        else:
            result = 'wrong'
        return render_template('q28r.html', result=result, answer=answer)
    return render_template('q28.html')

@app.route('/q28r')
def q28r():
    return render_template('q28r.html')

# Q29
@app.route('/q29', methods=['GET', 'POST'])
def q29():
    if request.method == 'POST':
        answer = request.form['answer']
        if answer == 'B':
            result = 'correct'
        else:
            result = 'wrong'
        return render_template('q29r.html', result=result, answer=answer)
    return render_template('q29.html')

@app.route('/q29r')
def q29r():
    return render_template('q29r.html')

# Q30
@app.route('/q30', methods=['GET', 'POST'])
def q30():
    if request.method == 'POST':
        answer = request.form['answer']
        if answer == 'A':
            result = 'correct'
        else:
            result = 'wrong'
        return render_template('q30r.html', result=result, answer=answer)
    return render_template('q30.html')

@app.route('/q30r')
def q30r():
    return render_template('q30r.html')

# Q31
@app.route('/q31', methods=['GET', 'POST'])
def q31():
    if request.method == 'POST':
        answer = request.form['answer']
        if answer == 'B':
            result = 'correct'
        else:
            result = 'wrong'
        return render_template('q31r.html', result=result, answer=answer)
    return render_template('q31.html')

@app.route('/q31r')
def q31r():
    return render_template('q31r.html')

# Q32
@app.route('/q32', methods=['GET', 'POST'])
def q32():
    if request.method == 'POST':
        answer = request.form['answer']
        if answer == 'A':
            result = 'correct'
        else:
            result = 'wrong'
        return render_template('q32r.html', result=result, answer=answer)
    return render_template('q32.html')

@app.route('/q32r')
def q32r():
    return render_template('q32r.html')

# Q33
@app.route('/q33', methods=['GET', 'POST'])
def q33():
    if request.method == 'POST':
        answer = request.form['answer']
        if answer == 'B':
            result = 'correct'
        else:
            result = 'wrong'
        return render_template('q33r.html', result=result, answer=answer)
    return render_template('q33.html')

@app.route('/q33r')
def q33r():
    return render_template('q33r.html')

# Q34
@app.route('/q34', methods=['GET', 'POST'])
def q34():
    if request.method == 'POST':
        answer = request.form['answer']
        if answer == 'B':
            result = 'correct'
        else:
            result = 'wrong'
        return render_template('q34r.html', result=result, answer=answer)
    return render_template('q34.html')

@app.route('/q34r')
def q34r():
    return render_template('q34r.html')



@app.route('/page_end')
def page_end():
    return render_template('page_end.html')


if __name__ == "__main__":
    app.run(debug=True)
    