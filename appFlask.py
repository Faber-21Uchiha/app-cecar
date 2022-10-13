import pandas as pd
import numpy as np
import sklearn
import joblib
from flask import Flask, app, render_template, request
app=Flask(__name__)
#definir ruta a la pagina de inicio
#@app.route('/')
#def index():
#  return render_template('index.html')
#se define ruta que se activara cuando se presiona el boton enviar del formulario
@app.route('/prediccion',methods=["GET POST"])
def predict():
  if request.method=='POST':
    try:
        var_1=float (request.form ['var_1'])
        var_2=float (request . torm ['var_2'])

        pred_args=[ var_1,var_2]
        pred_arr=np.array (pred_args)
        preds=pred_arr.reshape(1, -1)
        modelo=open ("./modelo .pkl", "rb")
        modelo_Clas=joblib. Load (modelo)
        prediccion_modelo=modelo_Clas.predict (preds)
        prediccion_modelo=round (float (prediccion_modelo) ,2)
        if prediccion_modelo==1.0:
          prediccion_modelo = "Aprueba"
        else:
          prediccion_modelo = "No aprueba"
    except ValueError:
      return "Por favor entra nombre válidos"
    return render_template ('prediccion.html',prediccion=prediccion_modelo)
    if __name__=='__main__':
      app.run(debung=True)