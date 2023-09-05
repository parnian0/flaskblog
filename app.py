from flask import Flask
app=Flask(__name__)
@app.route('/')
def home():
    return'Hello world!'
@app.route('/info')
def info():
    return'this is a website written in flask'
    
app.run(debug=True)