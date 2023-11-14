import streamlit as st
import numpy as np
import tensorflow as tf

# Load the trained model
model = tf.keras.models.load_model('TrainedModel.h5')

def main():
    st.title('Churn Prediction')

    # Adding user input elements
    tenure = st.number_input('Tenure:', value=1)
    monthly_charges = st.number_input('Monthly Charges:', value=1.0)
    internet_service = st.selectbox('Internet Service:', ['Fiber Optic', 'DSL', 'No'])
    online_security = st.selectbox('Online Security:', ['No', 'Yes', 'No Internet Service'])
    device_protection = st.selectbox('Device Protection:', ['No', 'Yes', 'No Internet Service'])
    tech_support = st.selectbox('Tech Support:', ['No', 'Yes', 'No Internet Service'])
    streaming_tv = st.selectbox('Streaming TV:', ['No', 'Yes', 'No Internet Service'])
    streaming_movies = st.selectbox('Streaming Movies:', ['No', 'Yes', 'No Internet Service'])
    contract = st.selectbox('Contract:', ['Month-to-Month', 'One Year', 'Two Year'])
    payment_method = st.selectbox('Payment Method:', ['Electronic Check', 'Mailed Check', 'Bank Transfer (Automatic)', 'Credit Card (Automatic)'])

    # Process user input and make predictions
    if st.button('Predict'):
        # Convert categorical variables to binary indicators
        internet_service_fiber = 1 if internet_service == 'Fiber Optic' else 0
        internet_service_dsl = 1 if internet_service == 'DSL' else 0
        online_security_no = 1 if online_security == 'No' else 0
        device_protection_no_internet = 1 if device_protection == 'No Internet Service' else 0
        tech_support_no = 1 if tech_support == 'No' else 0
        tech_support_no_internet = 1 if tech_support == 'No Internet Service' else 0
        streaming_tv_no_internet = 1 if streaming_tv == 'No Internet Service' else 0
        streaming_movies_no_internet = 1 if streaming_movies == 'No Internet Service' else 0
        contract_monthly = 1 if contract == 'Month-to-Month' else 0
        contract_two_year = 1 if contract == 'Two Year' else 0
        payment_electronic_check = 1 if payment_method == 'Electronic Check' else 0

        # Prepare input array for prediction
        input_data =[
            tenure,
            monthly_charges,
            internet_service_fiber,
            online_security_no,
            device_protection_no_internet,
            tech_support_no,
            tech_support_no_internet,
            streaming_tv_no_internet,
            streaming_movies_no_internet,
            contract_monthly,
            contract_two_year,
            payment_electronic_check
]

        input_array = np.array(input_data).reshape(1, 12)

        # Make predictions
        predictions = model.predict(input_array)

        # Display predictions
        if predictions > 0.5:
            result = "Customer Churn Occurs"
        
        else:
            result = "No Churn Occurs"

        st.write('Predicted Result:', result)
        st.write('Prediction value:', predictions)

if __name__ == '__main__':
    main()
