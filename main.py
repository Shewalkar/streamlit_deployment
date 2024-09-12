import streamlit as st

# Set the page configuration
st.set_page_config(page_title="Loan Eligibility Form", page_icon="💸", layout="centered")

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

# Create input fields for the form
gender = st.selectbox("Gender", ["Male", "Female", "Other"])
married = st.selectbox("Married", ["Yes", "No"])
applicant_income = st.number_input("Applicant Income", min_value=0, step=1000)
loan_amount = st.number_input("Loan Amount", min_value=0, step=500)
credit_history = st.selectbox("Credit History", ["Good", "Bad"])

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
