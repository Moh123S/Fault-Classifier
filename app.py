import streamlit as st
import joblib
import numpy as np

# 1. Model Load karna
model = joblib.load('models/bearing_model.pkl')

st.title("🏭 Industrial AI: Machine Health Monitor")
st.write("Real-time Vibration Analysis for Predictive Maintenance")

# 2. Sidebar for Inputs
st.sidebar.header("Sensor Inputs")
rms = st.sidebar.slider("Vibration RMS (Energy)", 0.0, 5.0, 1.0)
kurtosis = st.sidebar.slider("Kurtosis (Spikiness/Cracks)", 0.0, 20.0, 3.0)
peak = st.sidebar.slider("Peak Amplitude", 0.0, 10.0, 2.0)

# 3. Prediction Logic
features = np.array([[rms, kurtosis, peak]])
prediction = model.predict(features)

# 4. Display Result
st.subheader("Machine Status")
if prediction[0] == 0:
    st.success("✅ HEALTHY: Machine is running within normal parameters.")
else:
    st.error("🚨 FAULTY: High probability of Bearing Crack detected!")
    st.warning("Action Recommended: Schedule maintenance for Bearing Replacement.")

# 5. Dashboard Visual
st.info(f"Input Data -> RMS: {rms} | Kurtosis: {kurtosis} | Peak: {peak}")