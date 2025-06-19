from flask import Flask, url_for, redirect
from flask import render_template 
from flask import request  
import SQLAlchemy
from datetime import datetime


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///weshop.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Advert(db.Model):
   id = db.Column(db.Integer, primary_key=True)
   title = db.Column(db.String(100), nullable=False)
   intro = db.Column(db.Text(300), nullable=False)
   seller = db.Column(db.Text(50), nullable=False)
   
   def __repr__(self):
      return '<advert %r>'% self.id
   

@app.route('/home')
@app.route('/')
def home():
 return render_template('main.html') 

@app.route('/post', methods=['POST', 'GET'])
def post():
 if request.method == "POST":
  title = request.form['title']
  intro = request.form['intro']
  seller = request.form['seller']
  Advert = advert[title == title, intro == intro,  seller == seller]
  
  
  try:
    db.session.add(advert)
    db.session.commit
    return redirect('/home')
  except:
    return redirect('/error')
  pass
 else:
   return render_template('post.html')
 

@app.route('/login')
def login():
  return render_template('login.html')

@app.route('/rules')
def rules():
 return render_template('rules.html')

@app.route('/error')
def error():
  return render_template('error.html')

@app.route('/advert/<string:title>/<int:num>')
def advert(title, num):
 return render_template('advert.html')

@app.route('/user/<username>')
def show_user_profile(username):
 return  render_template('profile.html') + f'User:{username}'

with app.app_context(): 
    db.create_all() 

app.app_context().push() 

if __name__ == '__main__':
 app.run(debug = True)
