

from flask import Flask,request,jsonify
import numpy as np
import pickle

model = pickle.load(open('model.pkl','rb'))

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello world"

@app.route('/predict',methods=['POST'])
def predict():
    loc = request.form.get('loc')
    mintemp = request.form.get('mintemp')
    maxtemp = request.form.get('maxtemp')
    rainfall = request.form.get('rainfall')
    windgdir = request.form.get('windgdir')
    windgspeed = request.form.get('windgspeed')
    winddir9 = request.form.get('winddir9')
    winddir3 = request.form.get('winddir3')
    windspeed9 = request.form.get('windspeed9')
    windspeed3 = request.form.get('windspeed3')
    hum9 = request.form.get('hum9')
    hum3 = request.form.get('hum3')
    pressure9 = request.form.get('pressure9')
    pressure3 = request.form.get('pressure3')
    cloud9 = request.form.get('cloud9')
    cloud3 = request.form.get('cloud3')
    temp9 = request.form.get('temp9')
    temp3 = request.form.get('temp3')
    raintoday = request.form.get('raintoday')


    input_query = np.array([[loc,mintemp,maxtemp,rainfall,windgdir,windgspeed,winddir9,winddir3,windspeed9,windspeed3,hum9,hum3,pressure9,pressure3,cloud9,cloud3,temp9,temp3,raintoday]])

    result = model.predict(input_query)[0]


    return jsonify({'rainfalltom':str(result)})

if __name__ == '__main__':
    app.run(debug=True)
