import streamlit as st
import pandas as pd
from datetime import datetime, timedelta

# App Header
st.set_page_config(page_title="Smart Delivery Estimator", layout="centered")
st.title("🛍️ Smart Delivery Estimator")
st.markdown("Welcome! Predict delivery time based on your order details.")
st.markdown("**Built by Param Jani**")

# User Inputs
category = st.selectbox("Select Product Type", ["Electronics", "Books", "Clothing", "Furniture", "Toys"])
city = st.text_input("Enter Destination City")
shipping = st.radio("Choose Shipping Option", ["Standard", "Express", "Same-day"])

# Custom Logic for Delivery Days Estimation
def estimate_days(cat, method):
    product_days = {
        "Electronics": 5,
        "Books": 3,
        "Clothing": 4,
        "Furniture": 7,
        "Toys": 2
    }
    method_adjustment = {"Standard": 0, "Express": -1, "Same-day": -2}
    raw_days = product_days.get(cat, 5) + method_adjustment.get(method, 0)
    return max(1, raw_days)

# Button to Show Prediction
if st.button("Estimate Delivery Time"):
    estimated_days = estimate_days(category, shipping)
    estimated_date = datetime.now() + timedelta(days=estimated_days)
    st.success(f"Estimated Delivery Duration: {estimated_days} days")
    st.info(f"Expected Arrival Date: **{estimated_date.strftime('%A, %d %B %Y')}**")

# Dynamic Chart Section
st.subheader("📊 Comparison: Delivery Time Across Categories")
all_methods = ["Standard", "Express", "Same-day"]
delivery_data = {
    prod: [estimate_days(prod, ship) for ship in all_methods]
    for prod in ["Electronics", "Books", "Clothing", "Furniture", "Toys"]
}
df_chart = pd.DataFrame(delivery_data, index=all_methods)

st.line_chart(df_chart)

# Footer
st.markdown("---")
st.markdown("📌 *Smart delivery estimator developed as part of learning project by Param Jani*")
