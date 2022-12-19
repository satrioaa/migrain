import numpy as np
import pandas as pd
import pickle
import streamlit as st

load_model = pickle.load(open('migraine_trained_model.sav' ,'rb'))

def migrain_prediction(data_to_test):
    knn_predict_test = load_model.predict(data_to_test)[0]
    print("KNN:", knn_predict_test)
    return knn_predict_test

def main():
    st.title("Migrain Prediction")

    st.write("This is a web app to predict whether a person has migrain or not")

    st.write("Please fill the form below")

    global Age,Duration,Frequency,Location,Character,Intensity,Nausea,Vomit,Phonophobia,Photophobia,Visual,Sensory,Dysphasia,Dysarthria,Vertigo,Tinnitus,Hypoacusis,Diplopia,Defect,Ataxia,Conscience,Paresthesia,DPF

    Age = st.number_input("Age", min_value=0, max_value=100, value=0)
    Duration = st.number_input("Duration", min_value=0, max_value=10, value=0)
    Frequency = st.number_input("Frequency", min_value=0, max_value=10, value=0)
    Location = st.number_input("Location", min_value=0, max_value=10, value=0)
    Character = st.number_input("Character", min_value=0, max_value=10, value=0)
    Intensity = st.number_input("Intensity", min_value=0, max_value=10, value=0)
    Nausea = st.number_input("Nausea", min_value=0, max_value=10, value=0)
    Vomit = st.number_input("Vomit", min_value=0, max_value=10, value=0)
    Phonophobia = st.number_input("Phonophobia", min_value=0, max_value=10, value=0)
    Photophobia = st.number_input("Photophobia", min_value=0, max_value=10, value=0)
    Visual = st.number_input("Visual", min_value=0, max_value=10, value=0)
    Sensory = st.number_input("Sensory", min_value=0, max_value=10, value=0)
    Dysphasia = st.number_input("Dysphasia", min_value=0, max_value=10, value=0)
    Dysarthria = st.number_input("Dysarthria", min_value=0, max_value=10, value=0)
    Vertigo = st.number_input("Vertigo", min_value=0, max_value=10, value=0)
    Tinnitus = st.number_input("Tinnitus", min_value=0, max_value=10, value=0)
    Hypoacusis = st.number_input("Hypoacusis", min_value=0, max_value=10, value=0)
    Diplopia = st.number_input("Diplopia", min_value=0, max_value=10, value=0)
    Defect = st.number_input("Defect", min_value=0, max_value=10, value=0)
    Ataxia = st.number_input("Ataxia", min_value=0, max_value=10, value=0)
    Conscience = st.number_input("Conscience", min_value=0, max_value=10, value=0)
    Paresthesia = st.number_input("Paresthesia", min_value=0, max_value=10, value=0)
    DPF = st.number_input("DPF", min_value=0, max_value=10, value=0)
    
    migrain = ''

    if st.button("Predict"):
        migrain = migrain_prediction([[Age,Duration,Frequency,Location,Character,Intensity,Nausea,Vomit,Phonophobia,Photophobia,Visual,Sensory,Dysphasia,Dysarthria,Vertigo,Tinnitus,Hypoacusis,Diplopia,Defect,Ataxia,Conscience,Paresthesia,DPF]])
        st.success(migrain)


if __name__ == '__main__':
    main()   

