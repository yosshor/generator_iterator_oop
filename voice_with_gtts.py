"""
@author: Yossi
"""

import pyaudio
import os
from gtts import gTTS
import time
import playsound
import speech_recognition as sr


def speak(text):
    tts = gTTS(text = text, lang = 'en')
    filename = 'vo1e.mp3'
    tts.save(filename)
    playsound.playsound(filename)



def get_audio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
        said = ""
        
        try :
            said = r.recognize_google(audio)
            print(said)
        except Exception as e:
            print("Extention : " + str(e))
            
    return said

    
speak("hello yossi ")

get_audio()

text = get_audio()

if "hello" in text:
    speak("hello, how are you")
if "what is your name" in text:
    speak("MY name is Tim")

from gtts import gTTS
import os
tts = gTTS(text="first time i'm using a package in next.py course", lang='en')
tts.save("welcome.mp3") 
os.system("mpg321 welcome.mp3")


