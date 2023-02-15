import numpy as np
from flask import Flask , request , render_template
import joblib
input_features =[]
app = Flask(__name__)
model = joblib.load("model2_1.pkl")


@app.route('/')
def home():
    return render_template("index1.html")


@app.route('/predict', methods =['POST'])
def predict():
  if request.method=="POST":
        x1 = float(request.form["value1"])
        x2 = float(request.form["value2"])
        x3 = float(request.form["value3"])
        if str(request.form["value4"])=="petrol":
          x4=0
        if str(request.form["value4"])=="diesel":
          x4=1
        if str(request.form["value4"])=="cng":
          x4=2
        if str(request.form["value5"])=="dealer":
          x5=0
        if str(request.form["value5"])=="individual":
          x5=1
        if str(request.form["value6"])=="manual":
          x6=0
        if str(request.form["value6"])=="automatic":
          x6=0
        x7 = float(request.form["value7"])
        input_features.append(x1)
        input_features.append(x2)
        input_features.append(x3)
        input_features.append(x4)
        input_features.append(x5)
        input_features.append(x6)
        input_features.append(x7)
        features= [np.array(input_features)]
        prediction = model.predict(features)  
        output = round(prediction[0],2)
        return render_template('index1.html',prediction_text=f"Price of the car ={output}Lakh")


if __name__=="__main__":
    app.run(debug=True)
