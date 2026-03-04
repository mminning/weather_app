import streamlit as st
import pandas as pd
import numpy as np

st.title("Forecast Weather App")
city = st.text_input("Enter a city and state", placeholder="Example: Chicago, IL", value=None)
days = st.slider("How many days?", min_value=1, max_value=5)
datatype = st.selectbox("Select type of forecast", ["Temperature", "Precipitation"],
                        index=None, placeholder="Select type of forecast")
if datatype != None and city != None:
    st.subheader(f"{datatype} for the next {days} days")
    st.write(f"*in {city}*")
