import os
from flask import Flask, render_template, request
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html', title="MLH Fellow", url=os.getenv("URL"))

@app.route('/home', methods=['GET', 'POST'])
def home():
    if request.method=='POST':
        if request.form.get('homeButton') == "Home" :
            return render_template('index.html', title="Home Page", url=os.getenv("URL"))
        elif request.method=='GET' :
            form=form
            return render_template('sasha.html', form=form)
        
    return render_template('sasha.html', title="MLH Fellow", url=os.getenv("URL"))

@app.route('/sasha', methods=['GET', 'POST'])
def sasha():
    if request.method == 'POST':
        if request.form.get('homeButton') == "Home" :
            return render_template('index.html', title="Home Page", url=os.getenv("URL"))
        elif request.method=='GET':
            form=form
            return render_template('sasha.html', title="MLH Fellow", url=os.getenv("URL"))
   
    return render_template('sasha.html', title="MLH Fellow", url=os.getenv("URL"))

@app.route('/lauren', methods= ['POST', 'GET'])
def lauren():
    if request.method == 'POST':
        if request.form.get('homeButton') == "Home" :
            return render_template('index.html', title="Home Page", url=os.getenv("URL"))
        elif request.method=='GET':
            form=form
            return render_template('lauren.html', title="MLH Fellow", url=os.getenv("URL"))