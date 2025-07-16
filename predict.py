#Import library
import streamlit as st
import pandas as pd
import numpy as np
import json
from utils import replaceBMI
import pickle 

with open('BestRFR.pkl', 'rb') as file_1:
    model = pickle.load(file_1)

def run():

    with st.form('Riwayat Calon Nasabah'):
        st.write('## Form Prediksi Harga Premi')
        age = st.number_input('Usia', min_value = 0)
        diabetes = st.radio("Apakah Anda Memiliki Penyakit Diabetes?",["Yes", "No"])
        blood_pressure_problems = st.radio("Apakah Anda Memiliki Masalah Tekanan Darah?",["Yes", "No"])
        any_transplants = st.radio("Apakah Anda Memiliki Riwayat Transplantasi?",["Yes", "No"])
        any_chronic_diseases = st.radio("Apakah Memiliki Riwayat Penyakit Kronis?",["Yes", "No"])
        height = st.number_input('Tinggi Badan', min_value = 0)
        weight = st.number_input('Berat Badan', min_value = 0)
        known_allergies = st.radio("Apakah Anda Memiliki Alergi?",["Yes", "No"])
        history_of_cancer_in_family = st.radio("Apakah Keluarga Anda Memiliki Riwayat Penyakit Kanker?",["Yes", "No"])
        number_of_major_surgeries = st.selectbox("Berapa Kali Anda Pernah Melakukan Operasi Besar?",["1", "2", "3", "Lebih Dari 4"])
    
        submit = st.form_submit_button()

    data_inf = {
        'Age': age,
        'Diabetes': diabetes,
        'BloodPressureProblems': blood_pressure_problems,
        'AnyTransplants': any_transplants,
        'AnyChronicDiseases': any_chronic_diseases,
        'Height': height,
        'Weight': weight,
        'KnownAllergies': known_allergies,
        'HistoryOfCancerInFamily': history_of_cancer_in_family,
        'NumberOfMajorSurgeries': number_of_major_surgeries,
    }

    data_inf = pd.DataFrame([data_inf])

    if submit:
        prediction = model.predict(data_inf)
        st.write(f'## Prediksi Harga Premi(Annual): ${prediction[0]:,.0f}')

if __name__ == '__main__':
    run()