# app.py
from flask import Flask, render_template, request
from registration import Registration

app = Flask(__name__)
app.config['SECRET_KEY'] = 'a very long string'

class Registration(Form):
    email = StringField("email", [validators.InputRequired ("Please enter your email"),  validators.Email('invalid email'), IsUnique])
    password = PasswordField('password',[validators.InputRequired ("please enter a password")])
    confirm_password = PasswordField("confirm password",[validators.InputRequired ("password"), validators.EqualTo("password",  "passwords must match")])

    submit = SubmitField("Submit")
@app.route('/')
def hello_form():
    return '<H1>Hello, Form!</H1>'


@app.route('/registration', methods=['GET', 'POST'])
def RegisterUser():
    form = Registration()
    if request.method == 'POST':
        if form.validate() == False:
            return render_template('registration.html', form=form)
        else:
            return render_template('success.html')
    elif request.method == 'GET':
        return render_template('registration.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)
