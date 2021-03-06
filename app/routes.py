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
			'author': {'username': 'Troll'},
			'body': 'The Avengers movie is the best'
	}
]
	return render_template('index.html', title='Home', user=user, post=posts)


# from flask import render_template, flash, redirect, url_for

# from app.forms import LoginForm
#

#

#
#
# @app.route('/login', methods=['GET', 'POST'])
#
# def login():
# 	form = LoginForm()
# 	if form.validate_on_submit():
# 		flash('Login requested for user {}, remember_me={}'.format(
# 			form.username.data, form.remember_me.data))
# 		return redirect(url_for('index'))
# 	return render_template('login.html', title='Sign in', form=form)
