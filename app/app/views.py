from app import app

from flask import render_template, request, redirect

from datetime import datetime

@app.template_filter("clean_date")
def clean_date(dt):
    return dt.strftime("%b %d, %Y")

@app.route("/")
def index():
    return render_template('public/index.html')

@app.route("/jinja")
def jinja():

    my_name = 'Matt'

    age = 29

    langs = ['Python', 'C++', 'Java', 'Lisp', 'Prolog', 'R', 'Matlab', 'SQL']

    friends = {
        'Elora': 28,
        'Phil': 52,
        'Greg': 24,
        'Meg': 75
    }

    colors = ('Red', 'Green')

    cool = True

    class GitRemote:
        def __init__(self, name, description, url):
            self.name = name
            self.description = description
            self.url = url

        def pull(self):
            return f'Pulling Repo {self.name}'

        def clone(self):
            return f'Cloning into {self.url}'

    my_remote = GitRemote(
        name='Flask Jinja',
        description='Template design tutorial',
        url='https://github.com/Matt-Lynn/jinja.git')

    def repeat(x, qty):
        return x * qty

    date = datetime.utcnow()

    my_html = '<h1>THIS IS HTML, WHOA</h1>'

    suspicious = '<script>alert("You got pwned!")</script>'

    return render_template(
        'public/jinja.html', my_name=my_name, age=age,
        langs=langs, friends=friends, colors=colors,
        cool=cool, GitRemote=GitRemote, repeat=repeat,
        my_remote=my_remote, date=date, my_html=my_html,
        suspicious=suspicious)

@app.route('/about')
def about():
    return render_template('public/about.html')


@app.route('/sign-up', methods=["GET", "POST"])
def sign_up():

    if request.method == "POST":

        req = request.form

        username = req['username']
        email = req['email']
        password = req['password']

        print(username, email, password)

        return redirect(request.url)


    return  render_template('public/sign_up.html')

users = {
    'LuminaryNutrition': {
        'name': 'Elora B',
        'bio': 'Creator of Luminary Nutrition',
        'twitter-handle': '@LuminaryNutrition'
    },
    'elonmusk': {
        'name': 'Elon Musk',
        'bio': 'Tech disruptor, investor, and engineer',
        'twitter-handle': '@elonmusk'
    }
}

@app.route('/profile/<username>')
def profile(username):

    user = None

    if username in users:
        user = users[username]

    return render_template('public/profile.html', user=user, username=username)

@app.route('/multiple/<foo>/<bar>/<baz>')
def multi(foo, bar, baz):
    return f'foo: {foo}, bar: {bar}, baz: {baz}'