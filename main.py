import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from weather_data import get_temperatures


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

    if datatype == "Temperature":
        temp_data = get_temperatures(city, state, days)
        dates = []
        temperatures = []
        for date, temp in temp_data.items():
            dates.append(date)
            temperatures.append(temp)
    figure = px.bar(x=dates, y=temperatures, labels={"x": "Date", "y": "Temperature"}, color_discrete_sequence=["red"])
    st.plotly_chart(figure)
