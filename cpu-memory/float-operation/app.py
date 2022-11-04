import math
from time import time
from flask import Flask, request

app = Flask(__name__)

def float_operation(number):
    start = time()
    for i in range(0, int(number)):
        sin_i = math.sin(i)
        cos_i = math.cos(i)
        sqrt_i = math.sqrt(i)
    latency = time() - start
    return str(latency)

@app.route('/float-operation', methods=['GET'])
def function_handler():
    number = request.args.get('number', 1)
    latency = float_operation(number)
    #print(number)
    #print(str(latency))
    return "latency : " + str(latency)
