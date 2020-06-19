import os 
import json
import pandas as pd
import numpy
#from sklearn.externals import joblib
import joblib

s = pd.read_json('./parameters.json')
p = joblib.load("./model.pkl")
r = p.predict(s)
print (str(r))
