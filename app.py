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
        acousticness = float(request.form.get('acousticness'))
        danceability=float(request.form.get('danceability'))
        energy=float(request.form.get('energy'))
        instrumentalness=float(request.form.get('instrumentalness'))
        liveness=float(request.form.get('liveness'))
        speechiness=float(request.form.get('speechiness'))
        tempo=float(request.form.get('tempo'))
        valence=float(request.form.get('valence'))
        prediction=model.predict([[acousticness,danceability,energy,instrumentalness,liveness,speechiness,tempo,valence]]).tolist()[0]
        if prediction=="Rock":
            return render_template('index.html',prediction_texts="You are a ROCK Music Lover")
        else:
            return render_template('index.html',prediction_texts="You are a Hip-Hop Music Lover")
    else:
        return render_template('index.html')

if __name__=="__main__":
    app.run(debug=True)


