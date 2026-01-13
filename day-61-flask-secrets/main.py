from flask import Flask
from flask import render_template
from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.fields.simple import PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length
from flask_bootstrap import Bootstrap, Bootstrap5
from flask import Flask
import os
from dotenv import load_dotenv
'''
Red underlines? Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''
load_dotenv()
class LoginForm(FlaskForm):

    email=StringField(label='Email',validators=[DataRequired(),Email()])
    password=PasswordField(label='Password',
                           validators=[DataRequired(),Length(min=8)])
    submit=SubmitField(label='Log In')

app = Flask(__name__)
app.secret_key =os.getenv('SECRET_KEY')
bootstrap = Bootstrap5(app)
@app.route("/")
def home():
    return render_template('index.html')
@app.route("/login", methods=['GET', 'POST'])

def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data=="admin@gmail.com" and form.password.data=="12345678":
            # print(f"Email : {form.email.data}")
            # print(f"Password : {form.password.data}")
            return render_template('success.html')
        else:
            return render_template('denied.html')
    return render_template('login.html',form=form)

if __name__ == '__main__':
    app.run(debug=True)
