# train_model_selected.py
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
import joblib

# Load dataset
file_path = r"C:\Users\Ankur Bhardwaj\Desktop\p6\Prediction_Data.xlsx"
sheet_name = 'vw_ChurnData'
data = pd.read_excel(file_path, sheet_name=sheet_name)

# Drop unwanted columns
data = data.drop(['Customer_ID', 'Churn_Category', 'Churn_Reason'], axis=1)

# Columns to encode (we need Contract at least)
columns_to_encode = ['Contract']

label_encoders = {}
for col in columns_to_encode:
    le = LabelEncoder()
    data[col] = le.fit_transform(data[col])
    label_encoders[col] = le

# Encode target variable
data['Customer_Status'] = data['Customer_Status'].map({'Stayed': 0, 'Churned': 1})

# Select important features only
selected_features = [
    'Total_Revenue',
    'Contract',
    'Total_Charges',
    'Monthly_Charge',
    'Tenure_in_Months',
    'Age'
]

X = data[selected_features]
y = data['Customer_Status']

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train Random Forest
rf_model = RandomForestClassifier(n_estimators=100, random_state=42)
rf_model.fit(X_train, y_train)

# Save model + encoders + features
joblib.dump(rf_model, "rf_churn_model_selected.pkl")
joblib.dump(label_encoders, "label_encoders_selected.pkl")
joblib.dump(selected_features, "feature_columns_selected.pkl")

print("✅ Model trained only on selected features and saved successfully!")
