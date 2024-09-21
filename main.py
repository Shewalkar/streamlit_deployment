print("Working 1")
import streamlit as st
import pickle

print("Working 2")

model_pickle = open("./classifier.pkl", "rb")
clf = pickle.load(model_pickle)
# Set the page configuration
st.set_page_config(page_title="Loan Eligibility Form", page_icon="💸", layout="centered")

print("Working 3")

# Apply custom CSS for a colorful theme
st.markdown(
    """
    <style>
    
    body {
        background-color: black;
        color: white; /* Dark grey text for readability */
    }
    .stApp {
    background-color: #c2b9bd;
    
    }
    .reportview-container {
        background-color: #ffffff; /* White background for the main content area */
        color: #333333; /* Dark grey text for readability */
    }
    .sidebar .sidebar-content {
        background-color: #ffebcd; /* Blanched almond background for the sidebar */
        color: #333333; /* Dark grey text for readability */
    }
    .stButton>button {
        background-color: #4CAF50; /* Green background for the button */
        color: white; /* White text on the button */
    }
    .stSelectbox>div>div>div {
        background-color: #f5f5dc; /* Beige background for the select boxes */
    }
    .stNumberInput>div>div>div {
        background-color: #f5f5dc; /* Beige background for the number inputs */
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Set up the title and description
st.title("Loan Eligibility Form")
st.write("Please fill out the details below:")

print("Working 4")

# Create input fields for the form
gender = st.selectbox("Gender", ["Male", "Female", "Other"])
married = st.selectbox("Married", ["Yes", "No"])
applicant_income = st.number_input("Applicant Income", min_value=0, step=1000)
loan_amount = st.number_input("Loan Amount", min_value=0, step=500)
credit_history = st.selectbox("Credit History", ["Yes", "No"])

print("Working 5")

#Preprocessing the Input to feed to the Model
if gender == 'Male':
    gender = 1
else:
    gender = 0

if married == 'Married':
    married = 1
else:
    married = 0

if credit_history == 'Yes':
    credit_history = 1
else:
    credit_history = 0

print("Working 6")

# Display the entered information
st.write("## Summary")
st.write(f"**Gender:** {gender}")
st.write(f"**Married:** {married}")
st.write(f"**Applicant Income:** {applicant_income}")
st.write(f"**Loan Amount:** {loan_amount}")
st.write(f"**Credit History:** {credit_history}")

# Add some interactivity with a button
if st.button('Submit'):
    st.write("Thank you for submitting your details!")
    st.write(f"Debug zero: Checking the input {gender,married,applicant_income,loan_amount,credit_history}")
