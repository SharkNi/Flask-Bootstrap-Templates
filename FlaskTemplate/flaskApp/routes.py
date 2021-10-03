# Flask
from flask import render_template, redirect, url_for, request, session, flash, send_from_directory
from sqlalchemy import or_, and_
from werkzeug.security import generate_password_hash, check_password_hash
from flaskApp import app


@app.route('/', methods=['GET', 'POST'])
# dashboard index page
@app.route('/index', methods=['GET', 'POST'])
def index():
    return render_template('index.html')


# maps page
@app.route('/map', methods=['GET', 'POST'])
def map():
    return render_template('map.html')

# testing page
@app.route('/blank', methods=['GET', 'POST'])
def blank():
    return render_template('blank.html')


