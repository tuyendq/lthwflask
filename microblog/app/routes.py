from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Tuyen'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Ho chi minh!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movies is so cool!'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)