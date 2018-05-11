from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
	user = {'username': 'Andrew'}
	posts = [
	{
		'author': {'username': 'John'},
		'body': 'Beautiful day in Moscow!'
	},
	{
		'author': {'username': 'Susan'},
		'body': 'The Avengers movie pssed me off'
	},
        {
                'author': {'username': 'Susan'},
                'body': 'The Avengers movie pssed me off'
        },
        {
                'author': {'username': 'Susan'},
                'body': 'The Avengers movie pssed me off'
        }
]
	return render_template('index.html', title='Home', user=user, posts=posts)
