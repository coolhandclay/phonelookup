#!/bin/bash/env python 

import requests
import cid as c
from flask import Flask, render_template, request, url_for

app = Flask(__name__)

@app.route('/')
def index():
	return "Hello World"
	
@app.route('/lookup', methods=['POST'])
def lookup():
	name = c.returnName(request.form['entry'])

@app.route('/results')
def results():
	return "Results go here"
	

if __name__=='__main__':
	app.run()