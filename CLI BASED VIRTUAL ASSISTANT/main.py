import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib

from wikipedia.wikipedia import random

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def greet(str):
    print(f"Hi, {str}")
    speak(f"Hi {str}")

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")
    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   
    else:
        speak("Good Evening!")  
    speak("I am your assistant. Please tell me how may I help you")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"You said: {query}\n")
    except Exception as e:   
        print("Say that again please...")  
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('aakashgarg743@gmail.com', 'A@k@$#@Gm@1!.')
    server.sendmail('aakashgarg743@gmail.com', to, content)
    server.close()

if __name__ == "__main__":
    user = input("Enter your name here:\n")
    greet(user)
    wishMe()
    while True:
        query = takeCommand().lower()
        if 'wikipedia' in query:
            print("Searching...")
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            print("According To Wikipedia...")
            speak("According to Wikipedia...")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")

        elif 'open github' in query:
            webbrowser.open("github.com/aakashgarg743")
        
        elif 'open LinkedIn' in query:
            webbrowser.open("linkedin.com/aakashgarg743")

        elif 'play music' in query:
            import random
            music_dir = 'E:\\Songs'
            songs = os.listdir(music_dir)  
            # os.startfile(os.path.join(music_dir, songs[0]))
            os.startfile(os.path.join(music_dir, songs[random.randint(0, len(songs) - 1)]))

        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S") 
            print(f"Sir, the time is {strTime}") 
            speak(f"Sir, the time is {strTime}")

        elif 'open code' in query:
            codePath = "C:\\Users\\Aakash Garg\\AppData\\Local\\Programs\\Microsoft VS Code\\code.exe"
            os.startfile(codePath)

        elif 'email to bro' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "aakashgarg743@gmail.com"    
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry. I am not able to send this email at this time...")    

        elif 'quit' in query:
            speak("I am quitting sir.. Thanks a lot")
            quit()