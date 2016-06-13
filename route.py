#!/bin/bash/env python 

import requests
import cid as c
import fullcontact as fc
from flask import Flask, render_template, request, url_for

app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html')
	
@app.route('/lookup', methods=['GET','POST'])
def lookup():
	if request.method == "POST":
		# Try OpenCnam first
		print "Trying OpenCnam"
		name = c.returnName(request.form['entry'])
		# If OpenCnam doesn't return any results, Try Fullcontact
		if name != "":
			return render_template('results.html', name=name)
		elif name == "":
			print "Trying Fullcontact"
			fcname = fc.getName(request.form['entry'])
			if fcname == "":
				print "No results"
				return "There are no results"
			else:
				return render_template('results.html', name=fcname)
	else:
		return url_for('index')
	

if __name__=='__main__':
	app.run(debug=True)