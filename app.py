# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
from flask import Flask, render_template, request
import jsonify
import requests
import pickle
import numpy as np
import sklearn
from sklearn.preprocessing import StandardScaler
app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))
@app.route('/',methods=['GET'])
def Home():
    return render_template('index.html')


standard_to = StandardScaler()
@app.route("/predict", methods=['POST'])
def predict():
    if request.method == 'POST':
        Acousticness = float(request.form['Acousticness'])
        Danceability=float(request.form['Danceability'])
        Energy=float(request.form['Energy'])
        Instrumentalness=float(request.form['Instrumentalness'])
        Liveness=float(request.form['Liveness'])
        Speechiness=float(request.form['Speechiness'])
        Tempo=float(request.form['Tempo'])
        Valence=float(request.form['Valence'])
        prediction=model.predict([[Acousticness,Danceability,Energy,Instrumentalness,Liveness,Speechiness,Tempo,Valence]])
        if prediction=="Rock":
            return render_template('index.html',prediction_texts=prediction)
        else:
            return render_template('index.html',prediction_texts=prediction)
    else:
        return render_template('index.html')

if __name__=="__main__":
    app.run(debug=True)


