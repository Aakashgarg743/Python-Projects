import requests
import json
from plyer import notification
import time

def notifyMe(title, message):
    notification.notify(
        title = title,
        message = message,
        app_icon = "E:\Study\Python Projects\RealTime Weather App\cloud.ico",
        timeout = 3
    )

def noida():
    url = "https://api.weatherapi.com/v1/current.json?key=615b10a6b01843af9c1140621212709&q=Noida&aqi=yes"
    r = requests.get(url).text
    parsed = json.loads(r)
    state = parsed["location"]
    curr = parsed["current"]
    name = state["name"]
    region = state["region"]
    title = f"City: {name} - {region}\n"
    temp_c = curr["temp_c"]
    humidity = curr["humidity"]
    wind = curr["wind_kph"]
    data = f"Temperature: {temp_c}\nHumidity: {humidity}\nWind Speed: {wind}kph"
    print(title,data)
    notifyMe(title, data)
    time.sleep(8)

def hapur():
    url = "https://api.weatherapi.com/v1/current.json?key=615b10a6b01843af9c1140621212709&q=Hapur&aqi=yes"
    r = requests.get(url).text
    parsed = json.loads(r)
    state = parsed["location"]
    curr = parsed["current"]
    name = state["name"]
    region = state["region"]
    title = f"City: {name} - {region}\n"
    temp_c = curr["temp_c"]
    humidity = curr["humidity"]
    wind = curr["wind_kph"]
    data = f"Temperature: {temp_c}\nHumidity: {humidity}\nWind Speed: {wind}kph"
    print(title,data)
    notifyMe(title, data)
    time.sleep(8)

def ghaziabad():
    url = "https://api.weatherapi.com/v1/current.json?key=615b10a6b01843af9c1140621212709&q=Ghaziabad&aqi=yes"
    r = requests.get(url).text
    parsed = json.loads(r)
    state = parsed["location"]
    curr = parsed["current"]
    name = state["name"]
    region = state["region"]
    title = f"City: {name} - {region}\n"
    temp_c = curr["temp_c"]
    humidity = curr["humidity"]
    wind = curr["wind_kph"]
    data = f"Temperature: {temp_c}\nHumidity: {humidity}\nWind Speed: {wind}kph"
    print(title,data)
    notifyMe(title, data)
    time.sleep(8)

def jammu():
    url = "https://api.weatherapi.com/v1/current.json?key=615b10a6b01843af9c1140621212709&q=jammu&aqi=yes"
    r = requests.get(url).text
    parsed = json.loads(r)
    state = parsed["location"]
    curr = parsed["current"]
    name = state["name"]
    region = state["region"]
    title = f"City: {name} - {region}\n"
    temp_c = curr["temp_c"]
    humidity = curr["humidity"]
    wind = curr["wind_kph"]
    data = f"Temperature: {temp_c}\nHumidity: {humidity}\nWind Speed: {wind}kph"
    print(title,data)
    notifyMe(title, data)
    time.sleep(8)

if __name__=='__main__':
    noida()
    hapur()
    ghaziabad()
    jammu()