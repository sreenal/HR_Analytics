from flask import Flask,request, url_for, redirect, render_template 
import pickle 
import pandas as pd 
import joblib 
app = Flask(__name__)
model=joblib.load(open("model.pkl","rb"))
scale=joblib.load(open("scale.pkl","rb"))
le_edu=joblib.load(open("le_edu.pkl","rb"))
le_gen=joblib.load(open("le_gen.pkl","rb"))
le_rech=joblib.load(open("le_rech.pkl","rb"))
le_reg=joblib.load(open("le_reg.pkl","rb"))
le_dept=joblib.load(open("le_dept.pkl","rb"))
@app.route("/") 
def hello_world(): 
    return render_template('index.html')
    
if __name__ == '__main__': 
    app.run(debug=True)

