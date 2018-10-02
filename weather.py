import urllib
import json
import datetime

user_id = "" # Not needed
api_id = "115d7627cf1dc308de3ae6111e2b33fd"
zip_code = 30070
units = "imperial"


def fetch_weather_data(zip_code):
    request_url = "http//api.openweathermap.org/data/2.5/weather?zip=" + str(zip_code) + "&units=" + units + "&appid=" + api_id

    try:
        url = urllib.urlopen(request_url)
        response = url.read().decode('utf-8')
        api_dict = json.loads(response)
        url.close()

        print_details(api_dict)
    except:
        print("Error: Could not fetch weather data. Check the API key and zip code.")   


def print_details(api_dict):
    location_name = api_dict["name"]
    current_temperature = api_dict["main"]["temp"]
    atmospheric_pressure = api_dict["main"]["pressure"]
    wind_speed = api_dict["wind"]["speed"]
    wind_direction = api_dict["wind"]["deg"]
    epoch_time = api_dict["dt"]
    formatted_date = datetime.datetime.fromtimestamp(epoch_time).strftime('%c')
    return_code = api_dict["cod"]

    if return_code == 200: #checks if the return code returns successful (200 is successful), and if not, it displays the error.
        print("Name: " + location_name)
        print("Current Temperature: " + str(current_temperature) + " degrees Fahrenheit")
        print("Atmospheric Pressure: " + str(atmospheric_pressure) + " hPa")
        print("Wind Speed: " + str(wind_speed) + " mph")
        print("Wind Direction: " + str(wind_direction))
        print("Time of Report: " + formatted_date)
    else:
        print("Something went wrong.")

if __name__ == "__main__":
    fetch_weather_data(zip_code)