#!/bin/bash/env python 

import requests
import cid as c
from flask import Flask, render_template, request, url_for

app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html')
	
@app.route('/lookup', methods=['GET','POST'])
def lookup():
	if request.method == "POST":
		name = c.returnName(request.form['entry'])
		return render_template('results.html', name=name)
	else:
		return url_for('index')
	

if __name__=='__main__':
	app.run(debug=True)