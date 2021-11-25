from flask import Flask,jsonify
import pickle
import numpy as np

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello World"

@app.route('/predict',methods=['GET'])
def predict():
    pkl_file=open('model1.pkl', 'rb')
    mydict2 = pickle.load(pkl_file)
    pkl_file.close( )

    return jsonify({"Result": mydict2})

@app.route('/predict1',methods=['GET'])
def predict1():
    pkl1_file=open('model2.pkl', 'rb')
    mydict3=pickle.load(pkl1_file)
    pkl1_file.close( )

    return jsonify({"Result1": mydict3})

if __name__ == '__main__':
    app.run(debug=True)




