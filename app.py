from flask import Flask
from flask_sqlalchemy import SQLAlchemy
app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///database.db'
with app.app_context():
    db=SQLAlchemy(app)
class Post(db.Model):
    id=db.Column(db.integer,Primary_key=True)

@app.route('/')
def home():
    return'Hello world!'
@app.route('/info')
def info():
    return'this is a website written in flask'

app.run(debug=True)