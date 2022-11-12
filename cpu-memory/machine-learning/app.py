#!/usr/bin/python3
# tain.py
# Xavier Vasques 13/04/2021

import platform; print(platform.platform())
import sys; print("Python", sys.version)
import numpy; print("NumPy", numpy.__version__)
import scipy; print("SciPy", scipy.__version__)

import os
import shutil
from time import time
import numpy as np
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.neural_network import MLPClassifier
import pandas as pd
from joblib import dump
from sklearn import preprocessing

from flask import Flask, request

app = Flask(__name__)

def train(traincsv_path):

    # Load directory paths for persisting model

    MODEL_PATH_LDA = os.path.join('/tmp/', 'clf_lda.joblib')
    MODEL_PATH_NN = os.path.join('/tmp/', 'clf_nn.joblib')
      
    # Load, read and normalize training data
    data_train = pd.read_csv(traincsv_path)

    start = time()
        
    y_train = data_train['# Letter'].values
    X_train = data_train.drop(data_train.loc[:, 'Line':'# Letter'].columns, axis = 1)

    print("Shape of the training data")
    print(X_train.shape)
    print(y_train.shape)
        
    # Data normalization (0,1)
    X_train = preprocessing.normalize(X_train, norm='l2')
    
    # Models training
    
    # Linear Discrimant Analysis (Default parameters)
    clf_lda = LinearDiscriminantAnalysis()
    clf_lda.fit(X_train, y_train)
    
    # Save model
    from joblib import dump
    dump(clf_lda, MODEL_PATH_LDA)
        
    # Neural Networks multi-layer perceptron (MLP) algorithm
    clf_NN = MLPClassifier(solver='adam', activation='relu', alpha=0.0001, hidden_layer_sizes=(500,), random_state=0, max_iter=1000)
    clf_NN.fit(X_train, y_train)
       
    # Secord model
    from joblib import dump, load
    dump(clf_NN, MODEL_PATH_NN)
    latency = time() - start
    return latency, MODEL_PATH_NN, MODEL_PATH_LDA
        
@app.route('/ml', methods=['GET'])
def function_handler():
    traincsv_path = request.args.get('train','/app/csv/train.csv')
    latency, output_path_nn, output_path_lda = train(traincsv_path)
    print(output_path_nn)
    print(output_path_lda)
    return "latency : " + str(latency)