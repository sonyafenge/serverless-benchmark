from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def function_handler():
    return "Hello World!"                                                      
