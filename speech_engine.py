import pyttsx3
from decouple import config
from datetime import datetime

# configure values of the vars in .env file
USERNAME = config('USER')
BOTNAME = config('BOTNAME')

# initialize engine with pyttsx3 module, w/ sapi5 MS Speech API
engine = pyttsx3.init('sapi5')

# set rate and volume
engine.setProperty('rate', 190)
engine.setProperty('volume', 1.0)

# getting the voices from API using getProperty method (Male voice)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

# Text to Speech Conversion
def speak(text):
    """Used to speak wtv text is passed to it"""

    engine.say(text)
    engine.runAndWait()

# Greeting the user depending on the time (hour)
def greet_user():
    """Greets the user according to the time"""

    hour = datetime.now().hour

    if (hour >= 6) and (hour < 12):
        speak(f"Good Morning {USERNAME}")
    elif (hour >= 12) and (hour < 16):
        speak(f"Good Afternoon {USERNAME}")
    elif (hour >= 16) and (hour < 19):
        speak(f"Good Evening {USERNAME}")
    speak(f"I am {BOTNAME}. How may I assist you?")