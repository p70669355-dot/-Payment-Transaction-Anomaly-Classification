
import streamlit as st

st.set_page_config(
    page_title="Payment Transaction Risk Intelligence",
    page_icon="💳",
    layout="wide"
)

st.title("💳 Payment Transaction Risk Intelligence")
st.subheader("Payment Transaction Anomaly Classification")

st.write(
    "An ML-based system for classifying payment transactions "
    "as routine or anomalous."
)

st.success("Application started successfully!")
