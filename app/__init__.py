import os
from flask import Flask, render_template, request
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)

name = "Name"
experience_list = ["Experience 1", "Experience 2", "Experience 3"]
education_list = ["Education 1"]
hobby_list = ["Hobby 1", "Hobby 2", "Hobby 3", "Hobby 4"]

# Example for one person
# name = "Lauren Ciha"
# experience_list = ["Schloss Visual Reasoning Lab", "People and Robots Lab", "MLH Fellowship!"]
# education_list = ["University of Wisconsin-Madison"]
# hobby_list = ["reading", "journaling", "running"]

@app.route('/')
def index():
    return render_template('index.html', title="MLH Fellow", url=os.getenv("URL"))

@app.route('/home')
def home():
    return render_template('home.html', title="Home Page", url=os.getenv("URL"))

@app.route('/sample')
def template_test():
    return render_template('sample_page.html', name = name, experience_list=experience_list, education_list=education_list, hobby_list = hobby_list, url=os.getenv("URL"))


if __name__ == '__main__':
    app.run(debug=True)
