# import the Flask class from the flask module
from flask import Flask, render_template, redirect, url_for, request
import database
from flask import Flask, render_template, flash, request
from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField

# create the application object
app = Flask(__name__)
app = Flask(__name__)
app.config.from_object(__name__)
app.config['SECRET_KEY'] = '7d441f27d441f27567d441f2b6176a'

class ReusableForm(Form):
    name = TextField('Name:', validators=[validators.required()])
    phone= TextField('fNumber:', validators=[validators.required(), validators.Length(min=6, max=35)])
    age = TextField('age', validators=[validators.required(), validators.Length(min=3, max=35)])
    '''dob = TextField('dob', validators=[validators.required(), validators.Length(min=3, max=35)])
    bpl = TextField('bpl', validators=[validators.required(), validators.Length(min=3, max=35)])
    martial = TextField('martial', validators=[validators.required(), validators.Length(min=3, max=35)])'''


@app.route("/form", methods=['GET', 'POST'])
def hello():
    form = ReusableForm(request.form)
    if request.method == 'POST':
        name=request.form['name']
        age=request.form['age']
        phone=request.form['phone']
        print (name, " ", age, " ", phone)
        database.Inserter("daaa.db","test",(name,age,phone))

        if form.validate():
            # Save the comment here.
            flash('Thanks for registration ' + name)
        else:
            flash('Error: All the form fields are required. ')

    return render_template('hello.html', form=form)

@app.route('/')
def home():
    return render_template('home.html', error=69)  # r69eturn a string
@app.route('/admin')
def admin():
    return render_template('admin.html', error=error)
@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'Invalid Credentials. Please try again.'
        else:
            return redirect(url_for('admin'))
    return render_template('login.html', error=error)

# start the server with the 'run()' method
if __name__ == '__main__':
    app.run(debug=True)
