from flask import Flask, request
from io import BytesIO, StringIO
from pyresparser import ResumeParser
import urllib.parse
import base64
# import nltk
# nltk.download('stopwords')
import spacy
nlp= spacy.load('en_core_web_sm')

app = Flask("resume")

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route('/pdfparser', methods=['GET', 'POST'])
def hello():
    # data = ResumeParser('C:/Users/NivedithaJ/Documents/resume/Rajesh Karia.pdf').get_extracted_data()
   
    if request.method == 'POST':
        #get the data via blob
        resume = request.get_data()
        # get data via query params
        # resume = request.args.get('resume')
        # print(resume)
        fileReader= BytesIO(resume)
        fileReader.name="resume.pdf"
        data = ResumeParser(fileReader).get_extracted_data()
        print(data)
        return '<div>'+str(data)+'</div>'
    else:
        return '<div>No file sent use a post request</div>'