import requests
import json
from plyer import notification
import time

def notifyMe(title, message):
    notification.notify(
        title = title,
        message = message,
        app_icon = "E:\Study\Python Projects\RealTime Covid-19 Notificaton System\covid.ico",
        timeout = 3
    )


if __name__=='__main__':
    url = "https://data.covid19india.org/data.json"
    r = requests.get(url).text
    parsed = json.loads(r)
    state = parsed["statewise"][1:6]
    for i in state:
        state = i["state"]
        stcode = i["statecode"]
        death = i["deaths"]
        recover = i["recovered"]
        confirm = i["confirmed"]
        active = i["active"]
        title = f"State: {state} - {stcode}\n"
        data = f"Active: {active}\nConfirmed: {confirm}\nRecovered: {recover}\nDeath: {death}"
        print(title,data)
        notifyMe(title, data)
        time.sleep(8)