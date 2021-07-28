from distutils import command
from multiprocessing.connection import Client
from turtle import listen
import pyttsx3
from pywikihow import HowTo
from PyQt5 import QtCore, QtGui, QtWidgets
import speech_recognition as sr
import webbrowser
from playsound import playsound
import requests
import pywhatkit
from tkinter import *
import tkinter as tk
import tkinter.font as font
from playsound import playsound
import datetime
from time import sleep
import pywhatkit as kit
import datetime
import re
from pywikihow import search_wikihow
#import pyaudio

#----------------------------------------------------------variables----------------------------------------------------------
Name = 'Leah'


engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[3].id)
engine.setProperty('rate', 150)

def speak(str):
    engine.say(str)
    engine.runAndWait()

speak(f"Allow me to introduce myself i'm {Name} an artificial intelligent am i'm here to assist you in a variety of tasks as best i can. 24 hours a day seven days a week importing all preferences from home interface")
speak("systems are fully operational")
print ("systems are fully operational")

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

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning Sir")

    elif hour>=12 and hour<18:
        speak("Good Afternoon Sir")

    else:
        speak("Good Evening Sir")


if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower() #
        #all the commands
        if "how are you" in query:
            speak("I'm fine sir, how can i help you ?")

        #music
        elif 'playlist' in query:
         webbrowser.open('https://open.spotify.com/playlist/3lwxBt2TvSSInoudjG7bPX?si=e3dc99c9d2be4e53%27%27')
