import streamlit as st

st.title("Chat Selector")

option = st.selectbox("Select Suitable file", ["Social Media Chat Analyzer", "Bank Data Analysis"])

if option == "Social Media Chat Analyzer":
    from app import app
    app()
elif option == "Bank Data Analysis":
    from bank import bank_app
    bank_app()