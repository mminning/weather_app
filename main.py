import streamlit as st
import plotly.express as px
from weather_data import get_temperatures, get_precipitation

#GET USER INPUTS

st.title("Forecast Weather App")
location = st.text_input("Enter a city and state", placeholder="Example: Chicago, IL", value=None)
if location:
    city = location.partition(", ")[0]
    state = location.partition(", ")[2]
days = st.slider("How many days?", min_value=1, max_value=5)
datatype = st.selectbox("Select type of forecast", ["Temperature", "Precipitation"],
                        index=None, placeholder="Select type of forecast")


# RUN WEATHER DATA FUNCTIONS BASED ON USER INPUT
if datatype != None and city != None:
    st.subheader(f"{datatype} for the next {days} days")
    st.write(f"*in {city}*")
    try:

#TEMPERATURE
        if datatype == "Temperature":
            temp_data = get_temperatures(city, state, days)
            dates = []
            temperatures = []
            for date, temp in temp_data.items():
                dates.append(date)
                temperatures.append(temp)
            figure = px.area(x=dates, y=temperatures, labels={"x": "Date", "y": "Temperature"},
                        color_discrete_sequence=["red"], markers=True)

            st.plotly_chart(figure)

#PRECIPITATION
        if datatype == "Precipitation":
            prec_data = get_precipitation(city, state, days)
            dates = []
            precipitation = []
            for date, prec in prec_data.items():
                dates.append(date)
                precipitation.append(prec)
            figure = px.area(x=dates, y=precipitation, labels={"x": "Date", "y": "Precipitation (Percentage)"},
                            color_discrete_sequence=["blue"], markers=True)
            figure.update_layout(bargap=0)
            st.plotly_chart(figure)


    except AttributeError:
        pass
