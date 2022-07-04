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

#Lauren
laurenExperience = ["Schloss Visual Reasoning Lab", "People and Robots Lab", "MLH Fellowship"]
laurenEducation = ["University of Wisconson-Madison"]
laurenHobbies = ["reading", "journaling", "running"]

#Ruchika
ruchikaExperience =["Fellow", "MLH Production Engineering Fellowship","Undergraduate Research Assistant,IUC","Math Tutor, Juni Learning"]
ruchikaEducation = ["University of Illinois at Urbana Champaign"]
ruchikaHobbies = ["drumming", "embroidery", "video games"]

#Sasha
sashaExperience = ["Fellow, MLH PE Fellowship", "Video Editor, McMaster Silhouette", "Make-Up Artist, Sephora"]
sashaEducation = ["McMaster University", "OCAD U"]
sashaHobbies = ["Photography", "Games", "Reading"]

@app.route('/home', methods=['GET', 'POST'])
def home():
    return render_template('homePage.html', title="Index Page", url=os.getenv("URL"))

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('homePage.html', title="Index Page", url=os.getenv("URL"))

@app.route('/sasha', methods=['GET', 'POST'])
def sasha():
    return render_template('sasha.html', title="Sasha Page", experience_list=sashaExperience, education_list=sashaEducation, hobby_list = sashaHobbies,url=os.getenv("URL"))

@app.route('/lauren', methods= ['POST', 'GET'])
def lauren():
    return render_template('lauren.html', title="Lauren",experience_list=laurenExperience, education_list=laurenEducation, hobby_list = laurenHobbies, url=os.getenv("URL"))

@app.route('/ruchika', methods= ['POST', 'GET'])
def ruchika():
    return render_template('ruchika.html', title="Ruchika Page", experience_list=ruchikaExperience, education_list=ruchikaEducation, hobby_list = ruchikaHobbies, url=os.getenv("URL"))

@app.route('/sample')
def template_test():
    return render_template('sample_page.html', name = name, experience_list=experience_list, education_list=education_list, hobby_list = hobby_list, url=os.getenv("URL"))

if __name__ == '__main__':
    app.run(debug=True)
