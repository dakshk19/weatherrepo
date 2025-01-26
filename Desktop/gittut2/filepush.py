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

message = "city = " + str(data['name']) + " , temperature = " + str(round(data['main']['temp'] - 273.15, 2)) + " *c" + " , humidity = " + str(data['main']['humidity'])

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

