from registerapp import app
from flask import render_template
@app.route('/')
@app.route('/index')
def index():
    return render_template('index.htm')


@app.route('/physics')
def physics():
    return render_template('includes/physics.htm')    

@app.route('/math')
def math():
    return render_template('includes/math.htm')        