from flask import Flask, render_template, url_for
from forms import RegistrationForm, LoginForm
app = Flask(__name__)

app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'

posts = [
    {
        'author': 'Ikeri Ebenezer',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'July 22, 2018'
    },
    {
        'author': 'Ikeri Naomi',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'July 23, 2018'
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
    return render_template('register.html', title='Register', form=form)


@app.route("/login")
def login():
    form = LoginForm()
    return render_template('login.html', title='Login', form=form)


if __name__ == "__main__":
    app.run(debug=True)
