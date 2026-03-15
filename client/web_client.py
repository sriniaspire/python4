import streamlit as st
import requests

API_URL = "http://localhost:8000/expenses"

st.title("Add Expense")

amount = st.number_input("Amount")
description = st.text_input("Description")
category = st.text_input("Category")
date = st.date_input("Date")

if st.button("Submit"):
    data = {
        "Description": description,
        "Amount": amount,
        "Category": category,
        "Date": str(date),
        "Id": 4
    }
    print (data)
    requests.post(API_URL, json=data)
    st.success("Expense Added!")