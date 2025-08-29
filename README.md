# Telecom-Customer-Churn-Prediction
Customer Churn Prediction (Streamlit App)

This project predicts customer churn (whether a customer will leave or stay) using a Random Forest Classifier.
The model is trained on selected key features from telecom customer data, and a Streamlit dashboard allows users to input customer details and get a churn prediction instantly.

Features

Trains a churn prediction model on the following important features:

Total_Revenue

Contract

Total_Charges

Monthly_Charge

Tenure_in_Months

Age

Interactive Streamlit UI to input customer parameters

Real-time churn prediction with probability

Categorical features (like Contract) are automatically encoded

Project Structure
churn-prediction
│── train_model_selected.py       # Script to train model and save files
│── app_selected.py               # Streamlit app for churn prediction
│── rf_churn_model_selected.pkl   # Trained model (saved after training)
│── label_encoders_selected.pkl   # Label encoders for categorical features
│── feature_columns_selected.pkl  # List of selected features
│── README.md                     # Project documentation
│── Prediction_Data.xlsx          # Original dataset (not included here)
<img width="1453" height="807" alt="Screenshot 2025-08-29 231955" src="https://github.com/user-attachments/assets/eca91ef7-0af4-4fcd-b41f-bdd5a260dbdd" />

<img width="1441" height="623" alt="Screenshot 2025-08-29 232006" src="https://github.com/user-attachments/assets/18aff9b3-58e8-48e7-a641-d27e1c20bdb4" />

<img width="1423" height="786" alt="Screenshot 2025-08-29 232031" src="https://github.com/user-attachments/assets/aee9c536-1c60-42af-94e6-44cea898741b" />
Streamlit
<img width="1919" height="1128" alt="Screenshot 2025-08-29 231219" src="https://github.com/user-attachments/assets/d71ad041-5e12-49a0-876c-5f1d9e74c64b" />
