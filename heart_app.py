import pickle
import streamlit as st

# Load the saved model
heart_disease_model = pickle.load(open('trained_model.sav', 'rb'))

# Page selection (assuming a simple sidebar for navigation)
st.sidebar.title("Navigation")
page = st.sidebar.selectbox("Select a page", ["Heart Disease Prediction"])

# Heart Disease Prediction Page
if page == "Heart Disease Prediction":

    # Page title
    st.title('Heart Disease Prediction using ML')

    # Input fields
    col1, col2, col3 = st.columns(3)

    with col1:
        age = st.text_input('Age')
    with col2:
        sex = st.text_input('Sex')
    with col3:
        cp = st.text_input('Chest Pain types')
    with col1:
        trestbps = st.text_input('Resting Blood Pressure')
    with col2:
        chol = st.text_input('Serum Cholestoral in mg/dl')
    with col3:
        fbs = st.text_input('Fasting Blood Sugar > 120 mg/dl')
    with col1:
        restecg = st.text_input('Resting Electrocardiographic results')
    with col2:
        thalach = st.text_input('Maximum Heart Rate achieved')
    with col3:
        exang = st.text_input('Exercise Induced Angina')
    with col1:
        oldpeak = st.text_input('ST depression induced by exercise')
    with col2:
        slope = st.text_input('Slope of the peak exercise ST segment')
    with col3:
        ca = st.text_input('Major vessels colored by flourosopy')
    with col1:
        thal = st.text_input('thal: 0 = normal; 1 = fixed defect; 2 = reversable defect')

    # Code for Prediction
    heart_diagnosis = ''

    # Creating a button for Prediction
    if st.button('Heart Disease Test Result'):
        try:
            # Convert inputs to appropriate data types
            input_data = [
                int(age), int(sex), int(cp), int(trestbps), int(chol), int(fbs), int(restecg),
                int(thalach), int(exang), float(oldpeak), int(slope), int(ca), int(thal)
            ]

            # Perform prediction
            heart_prediction = heart_disease_model.predict([input_data])

            if heart_prediction[0] == 1:
                heart_diagnosis = 'The person is having heart disease'
            else:
                heart_diagnosis = 'The person does not have any heart disease'
        except ValueError:
            heart_diagnosis = 'Please enter valid input values'

    st.success(heart_diagnosis)
