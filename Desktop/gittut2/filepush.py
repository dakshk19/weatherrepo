import requests
import json
from dotenv import load_dotenv
import os

load_dotenv('.env')

COMPLETEURL = os.getenv("completeurl")
URL = os.getenv("url")
CHATID = os.getenv("chatid")
URL2 = os.getenv("url2")

completeurl = f"{COMPLETEURL}"
response = requests.get(completeurl)

data = response.json()

weather_condition = data['weather'][0]['main'].lower()
temperature = round(data['main']['temp'] - 273.15, 2)
humidity = data['main']['humidity']
city = data['name']

if "rain" in weather_condition or "thunderstorm" in weather_condition:
    umbrella_message = "Hey Sahil.. It might rain today. You gotta carry your umbrella ☔"
else:
    umbrella_message = "Hey Sahil.. No rain expected today. No need to carry your umbrella 😊"


message = f"City = {city}, Temperature = {temperature}°C, Humidity = {humidity}%\n{umbrella_message}"


def send_msg():
    url = f"{URL}"
    data = {"chat_id": CHATID, "text": message}
    response = requests.post(url, data=data)
    print(response.json())

send_msg()

def get_time():
    global message
    url2 = f"{URL2}"
    response = requests.get(url2)

    data2 = response.json()
    message += " , time = " + str(data2['time']['hour']) + ":" + str(data2['time']['minute'])

get_time()

#filepush

