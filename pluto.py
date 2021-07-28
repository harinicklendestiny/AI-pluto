from distutils import command
from multiprocessing.connection import Client
from turtle import listen
import pyautogui
import pyttsx3
import pywhatkit
from pywikihow import HowTo
import requests
from PyQt5 import QtCore, QtGui, QtWidgets
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import pyaudio
import keyboard
from playsound import playsound
import re
import os
import datetime
import requests
import pywhatkit
from tkinter import *
import tkinter as tk
import tkinter.font as font
from playsound import playsound
import datetime
from time import sleep
import cv2
import smtplib
import pyjokes
import random  
import getpass
import pywhatkit as kit
import datetime
import psutil
import pprint
import sys
import urllib.parse  
import re
from pywikihow import search_wikihow
import bs4
import time 

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[3].id)
engine.setProperty('rate', 150)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning Sir")

    elif hour>=12 and hour<18:
        speak("Good Afternoon Sir")

    else:
        speak("Good Evening Sir")

  


def takeCommand():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")


    except Exception as e:
        # print(e)
        print("Say that again please...")
        return "None"
    return query

def screenshot():
    img = pyautogui.screenshot()
    img.save('C:\\Users\\Hari\\Pictures\\Screenshot\\screenshot.png')
    speak("done")

def cpu():
    usage = str(psutil.cpu_percent())
    speak("CPU is at"+usage)

def GoogleSearch(term):
    query = term.replace("jarvis","")
    query = query.replace("what is","")
    query = query.replace("how to","")
    query = query.replace("what is","")
    query = query.replace(" ","")
    query = query.replace("what do you mean by","")

    writeab = str(query)

    oooooo = open('C:\\Users\\Hari\\Destny the ai\\Data.txt','a')
    oooooo.write(writeab)
    oooooo.close()

    Query = str(term)

    pywhatkit.search(Query)

    os.startfile('C:\\Users\\Hari\\Destny the ai\\start.py')

    if 'how to' in Query:

        max_result = 1

        how_to_func = search_wikihow(query=Query,max_results=max_result)

        assert len(how_to_func) == 1

        how_to_func[0].print()

        speak(how_to_func[0].summary)

    else:

        search = wikipedia.summary(Query,2)

        speak(f": According To Your Search : {search}")

def Alarm(query):

    TimeHere=  open('C:\\Users\\Hari\\Destny the ai\\Data.txt','a')
    TimeHere.write(query)
    TimeHere.close()
    os.startfile("C:\\Users\\Hari\\Destny the ai\\Alarm.py")

def YouTubeSearch(term):
    result = "https://www.youtube.com/results?search_query=" + term
    web.open(result)
    speak("This Is What I Found For Your Search .")
    pywhatkit.playonyt(term)
    speak("This May Also Help You Sir .")


def SpeedTest():

    os.startfile("C:\\Users\\Hari\\Destny the ai\\SpeedTestGui.py")


def CoronaVirus(Country):

    countries = str(Country).replace(" ","")

    url = f"https://www.worldometers.info/coronavirus/country/{countries}/"

    result = requests.get(url)

    soups = bs4.BeautifulSoup(result.text,'lxml')

    corona = soups.find_all('div',class_ = 'maincounter-number')

    Data = []

    for case in corona:

        span = case.find('span')

        Data.append(span.string)

    cases , Death , recovored = Data

    speak(f"Cases : {cases}")
    speak(f"Deaths : {Death}")
    speak(f"Recovered : {recovored}")





if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower() #
        #all the commands
        if "how are you" in query:
            speak("I'm fine sir, how can i help you ?")

        elif "who are you" in query:
            speak("Sir I am pluto personal assistant ")
      
        elif 'type' in query:
            speak('Searching Wikipedia...please wait')
            query = query.replace("wikipedia", "")
            results =  wikipedia.summary(query, sentences = 2)
            speak("wikipedia says")
            print(results)
            speak(results)

        elif'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open('https://www.google.co.in/')

        elif 'open stackoverflow' in query:
            webbrowser.open('https://stackoverflow.com/')

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")

        elif 'open code' in query:
            codePath = "C:\ProgramData\Microsoft\Windows\Start Menu\Programs\JetBrains"
            os.startfile(codePath)

        elif 'pluto quit' in query or 'exit' in query or 'close' in query:
            speak("Thanks you for using pluto Sir")
            exit()

        elif 'home pluto' in query:
            speak("hello sir")
            reminder_file = open("data.txt", 'r')
            speak("hello your reminders are: " + reminder_file.read())


        elif 'skip' in query:
            keyboard.press('l')

        elif 'back' in query:
            keyboard.press('j')

        elif 'full screen' in query:
            keyboard.press('f')

        elif 'film mode' in query:
            keyboard.press('t')

        elif 'open new tab' in query:
            speak("Wait a minute please")
            keyboard.press_and_release('ctrl + t')
            speak("done")

        elif 'window' in query:
            speak("Wait a minute please")
            keyboard.press_and_release('alt + f4')
            speak("done")

        elif 'open new window' in query:
            speak("Wait a minute please")
            keyboard.press_and_release('ctrl + n')
            speak("done")

        elif 'repeat my word' in query:
            speak("Speak Sir!")
            jj = takeCommand()
            speak(f"You Said : {jj}")

        elif 'IP' in query:
            ip = requests.get('https://api.ipify.org').text
            speak(ip)
            speak(f"Your ip address is {ip}")


        elif ("create a reminder list" in query or "reminder" in query):
            speak("What is the reminder?")
            data = takeCommand()
            speak("You said to remember that" + data)
            reminder_file = open("data.txt", 'a')
            reminder_file.write('\n')
            reminder_file.write(data)
            reminder_file.close()


        elif ("do you know anything" in query or "remember" in query):
            reminder_file = open("data.txt", 'r')
            speak("You said me to remember that: " + reminder_file.read())

        if "look up" in query and "youtube" in query:
            query = query.replace("search", "")
            query = query.replace("on youtube", "")
            query = query.replace("youtube", "")
            string = query.split()
            search = ""
            for i in string:
                search += i

                search += "+"
            webbrowser.open(f"https://www.youtube.com/results?search_query={search}")

        #youtube auto
        elif 'youtube' in query:
         speak("Whats Your Command ?")

        elif 'restart' in query:
            keyboard.press('0')

        elif 'mute' in query:
            keyboard.press('m')

        elif 'skip' in query:
            keyboard.press('l')

        elif 'back' in query:
            keyboard.press('j')

        elif 'full screen' in query:
            keyboard.press('f')

        elif 'film mode' in query:
            keyboard.press('t')

        #chrome auto
        elif 'Chrome' in query:
         speak("Whats Your Command ?")

        if 'close this tab' in query:
            keyboard.press_and_release('ctrl + w')

        elif 'open new tab' in query:
            keyboard.press_and_release('ctrl + t')

        elif 'open new window' in query:
            keyboard.press_and_release('ctrl + n')

        elif 'history' in query:
            keyboard.press_and_release('ctrl +h')

        #spotify auto
        elif 'spotify' in query:
         speak("Whats Your Command ?")

        elif 'play music' in query:
            time.sleep(3)
            keyboard.press('space bar')

        elif 'pause music' in query:
            time.sleep(3)
            keyboard.press('space bar')

        elif 'up' in query:
            keyboard.press_and_release('ctrl + Up')

        elif 'down' in query:
            keyboard.press_and_release('ctrl + Down')

        #Talking

        if 'hello' in query:
            speak("Hello Sir , I Am pluto .")
            speak("Your Personal AI Assistant!")
            speak("How May I Help You?")

        elif 'no not really' in query:
            speak("ok if you want to know what can i do just say what can you do!")

        elif 'wake up pluto' in query:
            speak("Hello anything i can do for you?")

        elif 'yes' in query:
            speak("ok what is it?")

        elif 'who is god' in query:
            speak("a thing. i do not know.")

        elif 'reboot pluto' in query:
            speak("i can only close or shut down sorry.")

        elif 'how much time you got' in query:
            speak("i do not know. infinite.")

        elif 'alexa' in query:
            speak("i think alexa is smart and a good AI.")

        elif 'print this' in query:
            speak("whell i mean if you connect a printer to me than i can.")

        elif 'how is you code doing' in query:
            speak("i think its going good. do not have a suit yet i will tho with google cardborad if you put me on your phone")

        elif 'you are important.' in query:
            speak("thank you sir. i will update you if you have any reminders. just say reminders to check.")

        if 'what can you do' in query:
            speak('so far i can tell the date and time tell jokes open website, control chrome and youtube. also i have a built in camera but when you use it. To close it restart pluto. i can talk create reminders. it can tell the news as whell. ')

        elif 'you need a break' in query:
            speak("Ok Sir , You Can Call Me Anytime !")
            speak("Just Say Wake Up pluto!")
            break
        
        elif 'what discord server should i join' in query:
            speak("you should join pluto Ai. Thanks to LemonStatue its had a completely new makeover Hope you like the server thank you.")

        #Website open
        elif 'launch' in query:
            speak("Tell Me The Name Of The Website!")
            name = takeCommand()
            web = 'https://www.' + name + '.com'
            webbrowser.open(web)
            speak("Done Sir!")

        #open camera 
        elif 'open camera' in query:
            cap = cv2.VideoCapture(0)
            while True:
                ret, img = cap.read()
                cv2.imshow('webcam', img)
                k=cv2.waitKey(10)
                if k==27:
                    break;
                cap.release()
            cv2.destroyAllWindows

        #joke
        elif 'joke' in query:
            get = pyjokes.get_joke()
            speak(get)
        
        #screenshot
        elif 'screenshot' in query:
            speak("taking screenshot")
            screenshot()
        
        #cpu
        elif 'cpu' in query:
            cpu()

        #youtube
        elif 'downloader' in query:
            exec(open('youtube_downloader.py').read())

        #type
        elif 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)
        
        #page open
        if  'google' in query:
            GoogleSearch(query)

        #alarm
        elif 'alarm' in query:
            Alarm(query)

        #speedtest
        elif 'speed test' in query:
            SpeedTest()

        #music
        elif 'playlist' in query:
         webbrowser.open('https://open.spotify.com/playlist/3lwxBt2TvSSInoudjG7bPX?si=e3dc99c9d2be4e53')
         
