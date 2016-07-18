# coding: utf-8
import os
import leancloud
from datetime import datetime

from flask import Flask
from flask import request
from flask import redirect
from flask import render_template
from flask import url_for
from werkzeug import secure_filename
from StringIO import StringIO

app = Flask(__name__)

app.jinja_env.variable_start_string = '{{{'
app.jinja_env.variable_end_string = '}}}'
ALLOWED_EXTENSIONS = set(['amr', 'mp3', 'wav'])

@app.route('/')
def index():
    return index2()#redirect(url_for('login.index'))


@app.route('/index2')
def index2():
    return render_template('index2.html')


@app.route('/time')
def time():
    return str(datetime.now())

@app.route('/login', methods=['POST','GET'])
def login():
    print "login : ",request
    user = request.form['user']
    passwd  = request.form['passwd']
    print "login : ",request,user,passwd
    return """ {"result":"Success"}"""

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

@app.route("/upload", methods=['POST','GET'])
def upload():
    print "Upload called",request
    if request.method == 'POST':
        file_r = request.files['file']
        print "Uploader : ",file_r,type(file_r),file_r.filename
        if file_r and allowed_file(file_r.filename):
            filename = secure_filename(file_r.filename)
            lean_file = leancloud.File(filename, StringIO(file_r.stream.read()))
            lean_file.save()
            print lean_file.id
            print lean_file.url
            #file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return """ {"result":"Success","url":\""""+lean_file.url+"""\"}"""
    return """ {"result":"Failed"}"""