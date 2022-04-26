from flask import Flask, render_template
from app import app

@app.route('/')
def index():
    name = 'Albright'
    return render_template('index.html', name=name)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/services')
def services():
    return render_template('services.html')
