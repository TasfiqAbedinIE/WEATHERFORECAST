import streamlit as st
import pandas as pd
import plotly.express as px

df = pd.read_csv("happy.csv")
print(df)

GDP = df["gdp"]
HAPPY = df["happiness"]
CORR = df["corruption"]

st.title("In Search for Happiness")
# place = st.text_input("Place: ")
# days = st.slider("Forecast Days: ", min_value=1, max_value=5, help="Select the number of forecasted days")
x_axis_option = st.selectbox("Select data for X Axis", ("GDP", 'Happiness', 'Corruption'))
Y_axis_option = st.selectbox("Select data for Y Axis", ("GDP", 'Happiness', 'Corruption'))

st.subheader(f'{x_axis_option} VS {Y_axis_option}')

match x_axis_option:
    case "GDP":
        X_axis = GDP
    case "Happiness":
        X_axis = HAPPY
    case "Corruption":
        X_axis = CORR
        
match Y_axis_option:
    case "GDP":
        Y_axis = GDP
    case "Happiness":
        Y_axis = HAPPY
    case "Corruption":
        Y_axis = CORR


figure = px.scatter(x=X_axis, y=Y_axis, labels={"x":x_axis_option, "y":Y_axis_option})
st.plotly_chart(figure)


