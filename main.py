import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px


st.title("Forecast Weather App")
location = st.text_input("Enter a city and state", placeholder="Example: Chicago, IL", value=None)
if location:
    city = location.partition(", ")[0]
    state = location.partition(", ")[2]
days = st.slider("How many days?", min_value=1, max_value=5)
datatype = st.selectbox("Select type of forecast", ["Temperature", "Precipitation"],
                        index=None, placeholder="Select type of forecast")


if datatype != None and city != None:
    st.subheader(f"{datatype} for the next {days} days")
    st.write(f"*in {city}*")

    dates = ["1", "2", "3", "4", "5"]
    temperatures = ["40", "41", "42", "43", "44"]
    figure = px.line(x=dates[:days], y=temperatures[:days], labels={"x": "Date", "y": "Temperature"})
    st.plotly_chart(figure)
