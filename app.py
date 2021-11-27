from flask import Flask,jsonify
import pickle
import numpy as np

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello World"

@app.route('/predict',methods=['GET'])
def predict():
    pkl_file=open('model.pkl', 'rb')
    mydict = pickle.load(pkl_file)
    pkl_file.close( )

    return jsonify({"Result": mydict})

@app.route('/predict1',methods=['GET'])
def predict1():
    pkl1_file=open('model1.pkl', 'rb')
    mydict1=pickle.load(pkl1_file)
    pkl1_file.close( )

    return jsonify({"Result1": mydict1})

@app.route('/predict2',methods=['GET'])
def predict2():
    pkl2_file=open('model2.pkl', 'rb')
    mydict2=pickle.load(pkl2_file)
    pkl2_file.close( )

    return jsonify({"Result2": mydict2})

@app.route('/predict3',methods=['GET'])
def predict3():
    pkl3_file=open('model3.pkl', 'rb')
    mydict3=pickle.load(pkl3_file)
    pkl3_file.close( )

    return jsonify({"Result3": mydict3})

@app.route('/predict4',methods=['GET'])
def predict4():
    pkl4_file=open('model4.pkl', 'rb')
    mydict4=pickle.load(pkl4_file)
    pkl4_file.close( )

    return jsonify({"Result4": mydict4})

@app.route('/predict5',methods=['GET'])
def predict5():
    pkl5_file=open('model5.pkl', 'rb')
    mydict5=pickle.load(pkl5_file)
    pkl5_file.close( )

    return jsonify({"Result5": mydict5})

if __name__ == '__main__':
    app.run(debug=True)




