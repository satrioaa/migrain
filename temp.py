import pandas as pd
import numpy as np
import pickle

# Load the data
load_model = pickle.load(open('C:/Users/Tachiii/Documents/PERMODELAN SIMULASI/lab/satrioaa/migraine_trained_model.sav', 'rb'))

# predict data
data_to_test = [[44,3,5,1,1,3,1,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0]]

knn_predict_test = load_model.predict(data_to_test)[0]

print("KNN:", knn_predict_test)