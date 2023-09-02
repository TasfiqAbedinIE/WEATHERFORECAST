import requests

API_KEY = "5e2bd1702cab01b490388ce0154427d1"


def get_data(place, forecast_days):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_KEY}"
    response = requests.get(url)
    content = response.json()
    filtered_data = content["list"]

    np_values = 8 * forecast_days
    filtered_data = filtered_data[:np_values]

    return filtered_data


if __name__ == "__main__":
    print(get_data(place="dhaka", forecast_days=2))