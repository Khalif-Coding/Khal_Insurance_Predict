import eda
import predict
import about
import streamlit as st

option = st.sidebar.selectbox(
    "Pilih Page:",
    ("Exploratory Data Analysis", "Check Harga Premi Anda", "About")
)

if option == "Check Harga Premi Anda":
    predict.run()
elif option == "Exploratory Data Analysis":
    eda.run()
elif option == "About":
    about.run()
