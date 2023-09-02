import streamlit as st
import plotly.express as px
from backend import get_data

images = {
    "Clear": "images/clear.png",
    "Clouds": "images/cloud.png",
    "Rain": "images/rain.png",
    "Snow": "images/snow.png",
}

# Graphics user interface
st.title("Weather forecast for next date")
place = st.text_input("Place: ")
days = st.slider("Forecast Days: ", min_value=1, max_value=5, help="Select the number of forecasted days")
option = st.selectbox("Select data to view", ("Temperature", 'Sky'))

st.subheader(f'{option} for the next {days} days in {place}')


if place:
    # Get the temp data
    try:
        filtered_data = get_data(place, days)


        # dates, temp = get_data(days)

        if option == "Temperature":
            temp = [dict["main"]["temp"]/10 for dict in filtered_data]
            dates = [dict["dt_txt"] for dict in filtered_data]
            # Create the graph
            figure = px.line(x=dates, y=temp, labels={"x":"Date", "y":"Temperature (C)"})
            st.plotly_chart(figure)

        if option == "Sky":
            sky_condition = [dict["weather"][0]["main"] for dict in filtered_data]
            print(sky_condition)
            image_paths = [images[condition] for condition in sky_condition]
            st.image(image_paths, width=115)
    except KeyError:
        st.write("Place doesn't exist")