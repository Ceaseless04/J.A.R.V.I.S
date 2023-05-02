import requests
from functions.online_function import *
from functions.offline_function import *
from pprint import pprint
from speech_engine import *
from user_input import *

if __name__ == '__main__':
    greet_user()
    while True:
        query = take_user_input().lower()

        if 'open notepad' in query:
            open_notepad()
        elif 'open vs code' in query:
            open_vs_code()
        elif 'open calculator' in query:
            open_calc()
        elif 'ip address' in query:
            ip_address = find_my_ip()
            speak(f"Your IP Address is {ip_address}.\n For your convenience, I am printing it on the screen sir.")
            print(f'Your IP Address is {ip_address}')
        elif 'wikipedia' in query:
            speak("What do you want to search on Wikipedia, sir?")
            search_query = take_user_input().lower()
            results = searching_wiki(search_query)
            speak(f"According to Wikipedia, {results}")
            speak("For your convenience, I am printing it on the screen sir.")
            print(results)
        elif 'search on google' in query:
            speak("What do you want to search on Google, sir?")
            search_query = take_user_input().lower()
            results = searching_wiki(search_query)
            speak(f"According to Google, {results}")
            speak("For your convenience, I am printing it on the screen sir.")
            print(results)
        elif 'youtube' in query:
            speak("What do you want to play on Youtube, sir?")
            video = take_user_input().lower()
            play_youtube(video)
        elif 'joke' in query:
            speak(f"Hope you like this one")
            joke = get_random_joke()
            speak(joke)
            speak("For your convenience, I am printing it on the screen sir.")
            pprint(joke)
        elif 'advice' in query:
            speak(f"Here's an advice for you, sir")
            advice = get_random_advice()
            speak(advice)
            speak("For your convenience, I am printing it on the screen sir.")
            pprint(advice)
        elif 'trending movies' in query:
            speak(f"Some of the trending movies are: {get_trending_movies()}")
            speak("For your convenience, I am printing it on the screen sir.")
            print(*get_trending_movies(), sep='\n')
        elif 'news' in query:
            speak(f"I'm reading out the latest headings, sir")
            speak(get_news())
            speak("For your convenience, I am printing it on the screen sir.")
            print(*get_news(), sep='\n')
        elif 'weather' in query:
            ip_address = find_my_ip()
            city = requests.get(f"https://ipapi.co/{ip_address}/city/").text
            speak(f"Getting weather report for your city {city}")
            weather, temperature, feels_like = get_weather_report(city)
            speak(f"The current temperature is {temperature}, but it feels like {feels_like}")
            speak(f"Also, the weather report talks about {weather}")
            speak("For your convenience, I am printing it on the screen sir.")
            print(f"Description: {weather}\nTemperature: {temperature}\nFeels Like: {feels_like}")