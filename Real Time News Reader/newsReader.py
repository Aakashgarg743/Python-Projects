import requests
import json

def speak(str):
    from win32com.client import Dispatch
    speak = Dispatch('SAPI.SpVoice')
    speak.Speak(str)

def technology():
    speak("I am starting reading..")
    url = "https://newsapi.org/v2/top-headlines?country=in&category=technology&apiKey=daed16be5df64819a6aff4b31f1d8d2b"
    re = requests.get(url).text
    parsed = json.loads(re)
    new = parsed["articles"][:5]
    count = 1
    for i in new:
        print(i["title"])
        speak(i["title"])
        if count < len(new):
            count += 1
            speak("Next")
        else:
            print("\nThanks For Listening...")
            speak("Thanks For Listening...")

def sports():
    speak("I am starting reading..")
    url = "https://newsapi.org/v2/top-headlines?country=in&category=sports&apiKey=daed16be5df64819a6aff4b31f1d8d2b"
    re = requests.get(url).text
    parsed = json.loads(re)
    new = parsed["articles"][:5]
    count = 1
    for i in new:
        print(i["title"])
        speak(i["title"])
        if count < len(new):
            count += 1
            speak("Next")
        else:
            speak("Thanks For Listening")

def science():
    speak("I am starting reading..")
    url = "https://newsapi.org/v2/top-headlines?country=in&category=science&apiKey=daed16be5df64819a6aff4b31f1d8d2b"
    re = requests.get(url).text
    parsed = json.loads(re)
    new = parsed["articles"][:5]
    count = 1
    for i in new:
        print(i["title"])
        speak(i["title"])
        if count < len(new):
            count += 1
            speak("Next")
        else:
            speak("Thanks For Listening")


if __name__ == '__main__':
    user = input("Enter your name: \n")
    print(f"Welcome {user}. I am your news reader today.. \nIn what field you are interested to listen latest news of today")
    speak(f"Welcome {user}. I am your news reader today.. \nIn what field you are interested to listen latest news of today")
    print("Type-\n1. For Technology. \n2. For Science. \n3. For Sports")
    speak("Type-1 For Technology. 2. For Science. 3. For Sports")
    inpu = int(input("Enter here: \n"))
    if inpu == 1:
        technology()
    elif inpu == 2:
        science()
    elif inpu == 3:
        sports()
    else:
        print("You entered wrong input...")
        speak("You entered wrong input...")