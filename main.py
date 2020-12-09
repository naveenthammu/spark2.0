import speech_recognition as sr
import pyttsx3
import datetime
import wolframalpha
app_key='JYYAJ7-L69A4E2AGU'
client = wolframalpha.Client(app_key)



engine= pyttsx3.init()
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
speak("this is spark 2 point o at your service sir")
def listing():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)
        text = r.recognize_google(audio)
        print(text)
        speak("recognized voice"+ text)
listing()
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>= 0 and hour<=12:
        speak("Good Morning Sir !")
    elif hour>= 12 and hour<16:
        speak("Good Afternoon sir")
    elif hour>=17 and hour<19:
        speak("good Evening sir")
    else:
        speak("Good eveningSir ")
wishMe()
def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        speak("what do you like to do sir")
        print("Listening...")
        audio = r.listen(source)
        text = r.recognize_google(audio)
        speak("recognize voice"+text)
        print(text)
        if "tell me a joke" in text:
            speak("hell is sweeter than licking some bitchs pussy")
        if "tell about yourself" in text:
            speak("this is spark 2 point o and what do you want know about me sir ")
            speak("how can help you sir")
        if "even or odd" in text:
            num = text.split()
            for i in num:
                if i.isdigit():
                    x = int(i)
                    if x % 2 == 0:
                        speak(x)
                        speak("is a even number")
                    else:
                        speak(x)
                        speak("is a odd number")

        if "spell" in text:
            word = text.split()
            for i in range(len(word)):
                if word == "spell":
                    word[i+1]
                    for j in word:
                        speak(j)
        if "query" in text:
            speak('what is your query sir!')
            #query= print(input('query:'))
            res = client.query()
            output = next(res.result).text
            speak(res)
            speak(output)
take_command()