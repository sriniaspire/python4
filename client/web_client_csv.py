import streamlit as st
import pandas as pd
import requests

API_URL = "http://localhost:8000/expenses"

st.title("Upload Expense CSV")

uploaded_file = st.file_uploader("Upload CSV", type="csv")

if uploaded_file:
    df = pd.read_csv(uploaded_file)

    st.dataframe(df)

    if st.button("Upload to API"):
        for _, row in df.iterrows():
            data = {
                "Date": row["Date"],
                "Description": row["Description"],
                "Amount": float(row["Amount"]),
                "Category": row["Category"],
                "Notes": row["Notes"]
            }

            requests.post(API_URL, json=data)

        st.success("Expenses uploaded successfully!")