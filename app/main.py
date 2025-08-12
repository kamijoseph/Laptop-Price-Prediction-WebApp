
import streamlit as st
import pickle
import pandas as pd

# loading the model
def load_model():
    with open("notebook/models.sav", "rb") as f:
        return pickle.load(f)
    
model = load_model()

# pages title
st.title("Laptop Price WebApp")
st.divider()

# inputs
brand = st.selectbox("Brand", options=["Dell", "HP", "Apple", "Lenovo", "Asus"])
processor_speed = st.number_input("Processor Speed (GHz)", min_value=1.0, max_value=5.0, value=2.5, step=0.1)
ram_size = st.number_input("RAM Size (GB)", min_value=4, max_value=64, value=16, step=4)
storage_capacity = st.number_input("Storage Capacity (GB)", min_value=128, max_value=2000, value=512, step=128)
screen_size = st.number_input("Screen Size (inches)", min_value=10.0, max_value=20.0, value=15.6, step=0.1)
weight = st.number_input("Weight (kg)", min_value=1.0, max_value=5.0, value=2.5, step=0.1)

# Prepare input data as DataFrame
input_data = pd.DataFrame({
    "Brand": [brand],
    "Processor_Speed": [processor_speed],
    "RAM_Size": [ram_size],
    "Storage_Capacity": [storage_capacity],
    "Screen_Size": [screen_size],
    "Weight": [weight]
})

# button to run the predictor
if st.button("Predict Price"):
    prediction = model.predict(input_data)[0]
    st.success(f"Predicted Laptop Price: ${prediction:,.2f}")

# dones