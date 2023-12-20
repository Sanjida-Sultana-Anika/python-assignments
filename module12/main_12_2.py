import requests


def kelvin_to_celsius(kelvin):
    return kelvin - 273.15


url = "https://api.openweathermap.org/data/2.5/weather"

api_key = "0c7e2ab7198d8fda3292aa99ec6a1209"

user_input = input("Enter your municipality: ")

querystring = {
    "q": user_input,
    "appid": api_key
}

try:
    response = requests.get(url, params=querystring)
    data = response.json()

    if response.status_code == 200:
        weather_description = data["weather"][0]["description"]
        temperature_kelvin = data["main"]["temp"]
        temperature_celsius = kelvin_to_celsius(temperature_kelvin)

        print(f"Weather in {user_input}: {weather_description}")
        print(f"Temperature: {temperature_celsius:.2f} °C")
    else:
        print(f"Error: {data['message']}")

except Exception as e:
    print(f"An error occurred: {e}")
