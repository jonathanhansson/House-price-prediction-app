import streamlit as st
import time
import sys
sys.path.append('..')
from machine_learning.predict import predict_house_price

st.title("Prediction for house prices")

m2 = st.number_input("Square meters", min_value=20, max_value=200, value=50)
position = st.slider("Location (1-10. 1 is a terrible location, 10 is a fantastic one)", min_value=1, max_value=10, value=5)

if st.button("Predict price"):
    with st.spinner('Calculating... 🌀'):
        time.sleep(2)
        predicted_price = predict_house_price(m2, position)
        
    st.write(f"A reasonable price for this house could be: {predicted_price[0]:,.0f}SEK (Swedish kronor)")
