from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm
app = Flask(__name__)
app.config['SECRET_KEY'] = '5SsJNMeQUtwMRgdon8oKqyfV9IPfOGeNiLxP1chNkZS4A4zBdT7qTdDgITZZHhB0XVdxFlb0ggMDvzJhqLLoz1AQbWG2gJmNbGKw2TvqFqzPcDucxpsA99HeaPXf4xzvWqi7GgBa0IXx2ws4WHueHJhmT57tw6BhKe2KYYTiVN1KxAK5Y0scUpQ2MLHprIRwgOKVtuIrnDg4Jha72JPFK5OURZo1X0KXIWgrsbiFrL4M5cFdDJ7pwrHAahqOkUPw86C6SBVAMObcWo457ix2U85Tc2gKMWkHzauRqakNI9ZQJUxlEFLfYrj4M6pn1Gt8CQ5lxXZQR91kS8DXghfFDswH1ifhqFfmLXC7FJQWOL3g32x1kSIhgV7nFWLxvuxrKyP0monGZP3gewWy86GI0Ea3p2X1Faco36EgJej5vJQoWnxZEwb1x9ieQkguzScvf2epdn5t3mNYvREXXF5XfIE0DHVjNEdtGE9Ag4htF1fh89CY1I8M'

posts = [
    {
        'author': 'Lev',
        'title': 'Lua Remote Event',
        'content': 'There are diffrent ways too use remote events. You can send them from Server --> Local or Local --> Server. Depending on your needs. Local --> Server has a few downs, it could be exploited by someone in jecting a script that fires the Remote from the Local Side',
        'date_posted': '10/29/2021'
    },
    {
        'author': 'Lev',
        'title': 'OnClick Function',
        'content': 'If its a Button then you can use an onlick function on it. What this does is when you click on the button it runs the function thats inside of it.',
        'date_posted': '10/29/2021'
    },
    {
        'author': 'Lev',
        'title': 'OnJoin Function',
        'content': 'This function will wait until a player has joined. And when someone does join it fires and does what ever is inside of it. This  works only in server scripts.',
        'date_posted': '10/30/2021'
    }
]


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)


@app.route("/about")
def about():
    return render_template('about.html', title='About')


@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', title='Login', form=form)


if __name__ == '__main__':
    app.run(debug=True)