from pdfminer.high_level import extract_text
from flask import Flask,render_template,request
import asyncio
import re
import json

#gemini
import pathlib
import textwrap
import google.generativeai as genai
from IPython.display import display
from IPython.display import Markdown

GOOGLE_API_KEY=""

genai.configure(api_key=GOOGLE_API_KEY)
model = genai.GenerativeModel('gemini-pro') 


app = Flask(__name__)

if __name__ == '__main__':
    app.run(debug=True)




@app.route("/",methods=['POST'])
async def deal():
    pdf_file = request.files['pdf_file']
    filename = pdf_file.filename

    # Save the PDF file asynchronously
    await save_pdf(filename, pdf_file)

    # Wait for the file saving to complete
    await asyncio.sleep(1)

    # Extract text from the saved PDF file
    text = extract_text('uploads/' + filename)
    print(text)

    # Generate response using Gemmi API
   
    response = model.generate_content(f"For the given data, generate 5 multiple-choice questions based on the content of the PDF. Provide the questions and answer options in raw JSON format. Each question should include the question text and four options. The data to be used for generating questions is as follows: {text} \n\nSample JSON format:\n```json\n{{ 'questions': [ {{'question': 'What is the capital of France?', 'options': ['London', 'Paris', 'Berlin', 'Rome'],'answer':'answer'}}, {{'question': 'Who wrote \'Romeo and Juliet\'?', 'options': ['William Shakespeare', 'Jane Austen', 'Charles Dickens', 'Leo Tolstoy'],'answer':'answer'}}, {{'question': 'What is the chemical symbol for water?', 'options': ['O2', 'H2O', 'CO2', 'NaCl'],'answer':'answer'}} ] }}\n```")
    json_string=response.text
    json_string=re.sub(r'^```json\s+', '', json_string)
    json_string = re.sub(r'\s+```$', '', json_string)
    response=json.loads(json_string)

    print(response['questions'])



    return render_template("chat.html", data=text, response=response['questions'])

async def save_pdf(filename, pdf_file):
    # Save the PDF file asynchronously
    with open('uploads/' + filename, 'wb') as f:
        pdf_file.save(f)


@app.route("/",methods=['GET'])
def dipl():
    return render_template("chat.html",data="",response="yet to cook")

