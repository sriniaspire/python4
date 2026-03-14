import streamlit as st
import requests

API_URL = "http://localhost:8000/expenses"

st.title("Add Expense")

amount = st.number_input("Amount")
description = st.text_input("Description")
category = st.text_input("Category")

if st.button("Submit"):
    data = {
        "Description": description,
        "Amount": amount,
        "Category": category,
        "Date": "2026-03-13",
        "Id": 4
    }
    print (data)
    requests.post(API_URL, json=data)
    st.success("Expense Added!")