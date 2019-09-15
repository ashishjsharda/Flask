'''
Created on Sep 15, 2019
Getting Started with Flask
@author: asharda
'''
    

from flask import Flask
app=Flask(__name__)
@app.route('/')
def hello_world():
    return "Hello World"

@app.route('/hello')
def hello_nex():
    return "Well another Hello"

if __name__=='__main__':
    app.run()
