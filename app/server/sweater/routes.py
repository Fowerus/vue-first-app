from flask import url_for, request, redirect,session,jsonify
from werkzeug.security import check_password_hash, generate_password_hash
from sweater import app, db
from sweater.models import Todos,Users,Posts

import traceback


#Todo's functions
@app.route('/getTodos',methods = ['GET', 'POST'])
def getTodos():
	if request.method == "POST":
		data = request.get_json(force = True)
		todos = Todos.query.filter_by(author = data).all()
		todos_list = []
		for i in todos:
			todos_list.append({'id':i.id, 'name':i.name, 'successful': i.successful})
		return jsonify(todos_list)
	return jsonify('There were some problems on the server')


@app.route('/changeCondition', methods =['GET', 'POST'])
def changeCondition():
	if request.method == 'POST':
		data = request.get_json(force = True)
		this_todo = Todos.query.get(data)
		this_todo.successful = not this_todo.successful

		try:
			db.session.commit()
		except:
			return jsonify('There were some problems on the server')

		return jsonify(['1'])

	return jsonify('There were some problems on the server')


@app.route('/addNewTodos', methods=['GET','POST'])
def addNewTodos():
	if request.method == 'POST':
		data = request.get_json(force=True)
		all_todos = Todos.query.filter_by(name = data.get('todo_name'), author = data.get('current_user')).first()
		if not all_todos:
			new_todo = Todos(name = data.get('todo_name'), successful = False, author = data.get('current_user'))
			try:
				db.session.add(new_todo)
				db.session.commit()
			except:
				return jsonify('There were some problems on the server')

			return jsonify({'new_id':Todos.query.filter_by(name = data.get('todo_name'), author = data.get('current_user')).first().id})

		return jsonify('You already have this todo')

	return jsonify('There were some problems on the server')


@app.route('/removeItem',methods = ['GET', 'POST'])
def removeItem():
	if request.method == 'POST':
		data = request.get_json(force=True)
		this_todo = Todos.query.get(data)
		try:
			db.session.delete(this_todo)
			db.session.commit()
		except:
			return jsonify('There were some problems on the server')

		return jsonify(['1'])
	return jsonify('There were some problems on the server')


#sing in/up functions
@app.route('/sing_up',methods = ['GET', 'POST'])
def singUp():
	if request.method == 'POST':
		data = request.get_json(force = True)
		if not Users.query.filter_by(login = data.get('login')).first():
			new_user = Users(login = data.get('login'), password = generate_password_hash(data.get('password')))
			try:
				db.session.add(new_user)
				db.session.commit()
			except:
				return jsonify('There were some problems on the server')

			return jsonify('Register successful')

		return jsonify('This login is not avaible')

	return jsonify('There were some problems on the server')


@app.route('/sing_in',methods = ['GET', 'POST'])
def singIn():
	if request.method == 'POST':
		data = request.get_json(force = True)
		this_user = Users.query.filter_by(login = data.get('login')).first()
		if this_user:
			if check_password_hash(this_user.password,data.get('password')):
				return jsonify({'current_user':this_user.login})
		return jsonify('Incorrect login or password')

	return jsonify('There were some problems on the server')


#Post's functions
@app.route('/getPosts', methods = ['POST', 'GET'])
def getPosts():
	if request.method == 'POST':
		posts = Posts.query.all()
		posts_list = []
		for i in posts:
			posts_list.append({'id':i.id, 'title':i.title, 'text': i.text, 'author':i.author})
		return jsonify(posts_list)
	return jsonify('There were some problems on the server')


@app.route('/addNewPost', methods = ['GET', 'POST'])
def addNewPost():
	if request.method == 'POST':
		data = request.get_json(force = True)
		this_post = Posts.query.filter_by(title = data.get('title'),author = data.get('author')).first()

		if not this_post:
			new_post = Posts(title = data.get('title'), text = data.get('text'), author = data.get('author'))

			try:
				db.session.add(new_post)
				db.session.commit()
			except:
				return jsonify('There were some problems on the server')

			return jsonify({'new_id':Posts.query.filter_by(title = data.get('title'), text = data.get('text'), author = data.get('author')).first().id})

		else:
			return jsonify('You already have similar post')


#Account's functions
@app.route('/changeLogPas', methods = ['GET','POST'])
def changeLogPas():
	if request.method == 'POST':
		data = request.get_json(force = True)

		current_user = Users.query.filter_by(login = data.get('currentUser')).first()
		check_new_login = Users.query.filter_by(login = data.get('newLogin')).first()

		if current_user and check_password_hash(current_user.password,data.get('curPassword')):

			#Check login
			if len(data.get('newLogin')) != 0:
				if not check_new_login:
					current_user.login = data.get('newLogin')

					all_user_post = Posts.query.filter_by(author = data.get('currentUser')).all()
					for post in all_user_post:
						post.author = data.get('newLogin')

					try:
						db.session.commit()
					except:
						return jsonify('There were some problems on the server')

				else:
					return jsonify({'Error':'This login is not avaible'})

			#Check password
			if len(data.get('newPassword')) != 0:
				if data.get('newPassword') == data.get('newRepPassword'):
					current_user.password = generate_password_hash(data.get('newPassword'))
				else:
					return jsonify({'Error':'Passwords are not equal'})

			try:
				db.session.commit()
			except:
				return jsonify({'Error':'There are some errors on the server'})


			if len(data.get('newLogin')) != 0:
				return jsonify({'current_user':data.get('newLogin')})

			return jsonify('')

		return jsonify({'Error':'Write correct password'})