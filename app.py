# app_selected.py
import streamlit as st
import pandas as pd
import joblib

# Load model and encoders
rf_model = joblib.load("rf_churn_model_selected.pkl")
label_encoders = joblib.load("label_encoders_selected.pkl")
feature_columns = joblib.load("feature_columns_selected.pkl")

st.set_page_config(page_title="Churn Prediction", layout="centered")
st.title("🔮 Customer Churn Prediction")

st.write("Enter customer details to predict churn:")

# Input form (only selected features)
input_data = {}
for col in feature_columns:
    if col in label_encoders:  # categorical
        input_data[col] = st.selectbox(f"{col}", label_encoders[col].classes_)
    else:  # numerical
        input_data[col] = st.number_input(f"{col}", value=0.0)

# Predict
if st.button("Predict Churn"):
    df = pd.DataFrame([input_data])

    # Encode categorical
    for col in label_encoders:
        if col in df.columns:
            df[col] = label_encoders[col].transform(df[col])

    pred = rf_model.predict(df)[0]
    proba = rf_model.predict_proba(df)[0][1]

    if pred == 1:
        st.error(f"🚨 Customer likely to CHURN! (Probability: {proba:.2f})")
    else:
        st.success(f"✅ Customer likely to STAY. (Probability: {proba:.2f})")
