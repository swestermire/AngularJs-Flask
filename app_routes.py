from __init__ import app
from flask import render_template, url_for, redirect

@app.route('/')
@app.route('/home')
def home():
    return render_template('/index.html')