# Importing libraries
import streamlit as st
import pickle
# import sklearn

# Load the model
with open("./classifier.pkl", "rb") as model_file:
    clf = pickle.load(model_file)

# Set the page configuration
st.set_page_config(page_title="Loan Eligibility Form", page_icon="💸", layout="centered")

# Apply custom CSS for a colorful theme
st.markdown(
    """
    <style>
    body {
        background-color: #2c3e50; /* Dark slate blue background */
        color: #ecf0f1; /* Light grey text for readability */
    }
    .stApp {
        background-color: #34495e; /* Slightly lighter slate blue for main area */
    }
    .reportview-container {
        background-color: #ffffff; /* White background for the main content area */
        color: #000000; /* Black text for general content */
    }
    .sidebar .sidebar-content {
        background-color: #ecf0f1; /* Light grey background for the sidebar */
        color: #2c3e50; /* Dark slate text for readability */
    }
    .stButton>button {
        background-color: #27ae60; /* Green background for the button */
        color: white; /* White text on the button */
        border: none; /* Remove default border */
        border-radius: 4px; /* Rounded corners */
    }
    .stButton>button:hover {
        background-color: #2ecc71; /* Lighter green on hover */
    }
    .stSelectbox>div>div>div, .stTextInput>div>div>input {
        background-color: #ecf0f1; /* Light grey background for select boxes and text inputs */
        border-radius: 4px; /* Rounded corners */
        color: #000000; /* Black text in select boxes and text inputs */
    }
    .stNumberInput>div>div>div {
        background-color: #ecf0f1; /* Light grey background for number inputs */
        border-radius: 4px; /* Rounded corners */
    }
    .stNumberInput>div>div>input {
        color: #000000; /* Black text for number inputs */
    }
    .stMarkdown h1, .stMarkdown h2, .stMarkdown h3 {
        color: #e74c3c; /* Red text for headers */
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Set up the title and description
st.title("Loan Eligibility Form")
st.write("Please fill out the details below to check your loan eligibility:")

# Create input fields for the form
gender = st.selectbox("Gender", ["Male", "Female"])
married = st.selectbox("Married", ["Yes", "No"])
applicant_income = st.number_input("Applicant Income", min_value=0, step=1000)
loan_amount = st.number_input("Loan Amount", min_value=0, step=500)
credit_history = st.selectbox("Credit History", ["Yes", "No"])

# Preprocess inputs
gender = 1 if gender == "Male" else 0
married = 1 if married == "Yes" else 0
credit_history = 1 if credit_history == "Yes" else 0

# Predict loan eligibility
result = clf.predict([[gender, married, applicant_income, loan_amount, credit_history]])
status = "Approved" if result == 1 else "Rejected"

# Display the entered information
st.write("## Summary")
st.write(f"**Gender:** {'Male' if gender == 1 else 'Female'}")
st.write(f"**Married:** {'Yes' if married == 1 else 'No'}")
st.write(f"**Applicant Income:** ${applicant_income:,.0f}")
st.write(f"**Loan Amount:** ${loan_amount:,.0f}")
st.write(f"**Credit History:** {'Yes' if credit_history == 1 else 'No'}")

# Add some interactivity with a button
if st.button('Submit'):
    st.write(f"## Loan Status: {status}")
    # Debugging information (optional)
    # st.write(f"Preprocessed inputs are: {gender, married, applicant_income, loan_amount, credit_history}")
