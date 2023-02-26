from sweater import db


class Todos(db.Model):
	id = db.Column(db.Integer, primary_key = True)
	name = db.Column(db.String(128),nullable = False)
	successful =db.Column(db.Boolean)
	author = db.Column(db.String(128),nullable = False)

	def __init__(self,name,successful,author):
		self.name = name
		self.successful = successful
		self.author = author

	def __rept__(self):
		return f'id:{self.id} | name:{self.name} | successful:{self.successful} | author:{self.author}'



class Users(db.Model):
	id = db.Column(db.Integer, primary_key = True)
	login = db.Column(db.String(128),nullable = False)
	password =db.Column(db.String(128),nullable = False)

	def __init__(self,login,password):
		self.login = login
		self.password = password

	def __rept__(self):
		return f'id:{self.id} | login:{self.login} | password:{self.password}'



class Posts(db.Model):
	id = db.Column(db.Integer, primary_key = True)
	title = db.Column(db.String(128),nullable = False)
	text = db.Column(db.String(128),nullable = False)
	author =db.Column(db.String(128),nullable = False)

	def __init__(self,title,text,author):
		self.title = title
		self.text = text
		self.author = author

	def __rept__(self):
		return f'id:{self.id} | title:{self.title} | text:{self.text} | author:{self.author}'