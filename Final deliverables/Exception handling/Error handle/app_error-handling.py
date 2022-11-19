import numpy as np
from flask import Flask, request, jsonify, render_template
import joblib
import requests

app = Flask(__name__)
model = joblib.load('Power_Prediction.sav')


@app.route('/')
def home():
    return render_template('intro.html')


@app.route('/predict')
def predict():
    return render_template('predict.html')


@app.route('/windapi',methods=['POST'])
def windapi():
    city=request.form.get('city')
    apikey="36c0639c05e38cd003ddea74d69b8822"
    url="http://api.openweathermap.org/data/2.5/weather?q="+city+"&appid="+apikey
    resp = requests.get(url)
    resp=resp.json()
    temp = str((resp["main"]["temp"])-273.15) +" °C"
    humid = str(resp["main"]["humidity"])+" %"
    pressure = str(resp["main"]["pressure"])+" mmHG"
    speed = str((resp["wind"]["speed"])*3.6)+" Km/s"
    return render_template('predict.html', temp=temp, humid=humid, pressure=pressure,speed=speed)   
@app.route('/y_predict',methods=['POST'])

#File: 404.html, server location: 
@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")

# try/except logic that is a part of Python. If the try doesn't work, then we're catching all errors to the except statement,
#So now we have a new file that we're referencing, 500.html. We pass one variable through, and that is the error.
@app.route('/slashboard/')
def slashboard():
    try:
        return render_template("dashboard.html", TOPIC_DICT = shamwow)
    except Exception as e:
	    return render_template("500.html", error = str(e))
		
        
def y_predict():
    '''
    For rendering results on HTML GUI
    '''
    x_test = [[float(x) for x in request.form.values()]]
    prediction = model.predict(x_test)
    print(prediction)
    output = prediction[0]
    return render_template('predict.html', prediction_text='The energy predicted is {:.2f} KWh'.format(output))


if __name__ == "__main__":
    app.run(debug=False)
