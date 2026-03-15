import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from backend import get_data


st.title("Forecast Weather App")
location = st.text_input("Enter a city and state", placeholder="Example: Chicago, IL", value=None)
city = location.partition(", ")[0]
state = location.partition(", ")[2]
days = st.slider("How many days?", min_value=1, max_value=5)
datatype = st.selectbox("Select type of forecast", ["Temperature", "Precipitation"],
                        index=None, placeholder="Select type of forecast")


if datatype != None and city != None:
    st.subheader(f"{datatype} for the next {days} days")
    st.write(f"*in {city}*")

    data = get_data(city, days, datatype)

    figure = px.line(x=dates, y=temperatures, labels={"x": "Date", "y": "Temperature"})
    st.plotly_chart(figure)
