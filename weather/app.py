import streamlit as st
import pickle
import numpy as np
import sklearn
# Load the pickled model
with open('weather_prediction_model.pkl', 'rb') as file:
    model = pickle.load(file)

# Set the title of the web app
st.title("Weather Prediction Web App")

# Create user inputs for the features based on your dataset
st.header("Enter Weather Data")
precipitation = st.number_input("Precipitation (mm)", min_value=0.0, step=0.1)
temp_max = st.number_input("Max Temperature (°C)", min_value=-50.0, max_value=50.0, step=0.1)
temp_min = st.number_input("Min Temperature (°C)", min_value=-50.0, max_value=50.0, step=0.1)
wind = st.number_input("Wind Speed (km/h)", min_value=0.0, max_value=200.0, step=0.1)

# When the user clicks the Predict button
if st.button("Predict Weather"):
    # Prepare the input data for prediction
    input_data = np.array([[precipitation, temp_max, temp_min, wind]])

    # Make a prediction using the loaded model
    prediction = model.predict(input_data)[0]

    # Display the prediction
    if prediction == 1:
        st.success("The model predicts: Rainy weather")
    else:
        st.success("The model predicts: Clear weather")
