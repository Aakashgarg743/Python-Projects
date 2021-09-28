import speech_recognition as sr
from PyDictionary import PyDictionary

def speak(str):
    from win32com.client import Dispatch
    speak = Dispatch('Sapi.SpVoice')
    speak.Speak(str)

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 0.8
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"You said: {query}\n")
    except Exception as e:
        print("Say that again please...")
        return "None"
    return query

def dictionary(query):
    dictionary = PyDictionary()
    result = dictionary.meaning(query)
    for k, v in result.items():
        for i in v:
            print(i)
            speak(i)

if __name__=='__main__':
    print("Welcome...\n")
    speak("Hi, I am your personal dictionary...")
    print("Please tell me your name to verify you...\n")
    speak("Please tell me your name to verify you...")
    li = ["bro", "manish", "nakul"]
    while True:
        query = takeCommand().lower()
        if query in li:
            print("Ok, Verified")
            speak("Ok, You are verified...\n")
            query = takeCommand().lower()
            if 'mode' in query or 'mod' in query:
                speak("Please tell me a word to get the meaning...")
                query = takeCommand().lower()
                if 'search' in query:
                    print("Searching...\n")
                    speak("Searching...")
                    query = query.replace("search", "")
                    dictionary(query)
                    speak("Tell me your name...")
            elif 'quit' in query:
                print("Quitting Sir...")
                speak("Quitting Sir..")
                quit()
            elif 'hindi' in query:
                speak("Tell me a word to translate in hindi...")
                query = takeCommand().lower()
                if 'search' in query:
                    print("Searching...\n")
                    speak("Searching...")
                    query = query.replace("search", "")
                    dictionary = PyDictionary()
                    speak(dictionary.translate(query, "hi"))
                    print(dictionary.translate(query, "hi"))
                    speak("Tell me your name....")
        else:
            print("You are a fraud person...")
            speak("You are a fraud person..")
            quit()