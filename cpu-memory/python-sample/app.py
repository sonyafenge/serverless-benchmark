from flask import Flask

app = Flask(__name__)


@app.route('/<number>')
def my_view_func(number):
    return number