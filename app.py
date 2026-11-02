from flask import Flask , request,redirect,render_template_string
import string
import random
app=Flask(__name__)
URL_database={}
def_generate_short_url():
    character=string.ascii_letters+string.digits
    return "".join(random.choices(character,k=6))
@app.route('/',methods=['GET','POST'])
def home():
    short_url=""
    if request.method=='POST':
        original_url=request.form['URL']


