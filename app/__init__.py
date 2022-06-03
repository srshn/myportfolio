import os
from flask import Flask, render_template, request
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html', title="Index Page", url=os.getenv("URL"))

@app.route('/home', methods=['GET', 'POST'])
def home():
    if request.method=='POST':
        if request.form.get('homeButton') == "Home" :
            return render_template('index.html', title="Home Page", url=os.getenv("URL"))
        elif request.form.get('sashaPage') == "sasha" :
            return render_template('sasha.html', title="Sasha Page", url=os.getenv("URL"))
        elif request.form.get('laurenPage') == "lauren" :
            return render_template('lauren.html', title="Lauren Page", url=os.getenv("URL"))
        if request.form.get('ruchikaPage') == "ruchika" :
            return render_template('ruchika.html', title="Ruchika Page", url=os.getenv("URL"))
    elif request.method=='GET' :
        form=form
        return render_template('index.html', form=form)
        
    return render_template('index.html', title="The Home Page", url=os.getenv("URL"))

@app.route('/sasha', methods=['GET', 'POST'])
def sasha():
    if request.method == 'POST':
        if request.form.get('homeButton') == "Home" :
            return render_template('index.html', title="Home Page", url=os.getenv("URL"))
    elif request.method=='GET':
        form=form
        return render_template('sasha.html', title="Sasha Page", url=os.getenv("URL"))
   
    return render_template('sasha.html', title="Sasha Page", url=os.getenv("URL"))

@app.route('/lauren', methods= ['POST', 'GET'])
def lauren():
    if request.method == 'POST':
       if request.form.get('homeButton') == "Home" :
            return render_template('index.html', title="Home Page", url=os.getenv("URL"))
    elif request.method=='GET':
        form=form
        return render_template('lauren.html', title="Lauren Page", url=os.getenv("URL"))
    
    return render_template('lauren.html', title="Lauren Page", url=os.getenv("URL"))

@app.route('/ruchika', methods= ['POST', 'GET'])
def ruchika():
    if request.method == 'POST':
        if request.form.get('homeButton') == "Home" :
            return render_template('index.html', title="Home Page", url=os.getenv("URL"))
    elif request.method=='GET':
        form=form
        return render_template('ruchika.html', title="Ruchika Page", url=os.getenv("URL"))
    
    return render_template('ruchika.html', title="Ruchika Page", url=os.getenv("URL"))