# Importing methods from installing modules
import requests
import wikipedia
import pywhatkit as kit
from decouple import config

# finding my own ip address
def find_my_ip():
    ip_address = requests.get('https://api64.ipify.org/?format=json').json()
    return ip_address["ip"]

# searching on wikipedia
def searching_wiki(query):
    results = wikipedia.summary(query, sentences=2)
    return results

# playing videos on YT
def play_youtube(video):
    kit.playonyt(video)

# other optin for searching: Chromium
def search_chromium(query):
    kit.search(query)

# current news headlines
NEWS_API_KEY = config("NEWS_API_KEY")

# function for weather
def get_news():
    news_headlines = []
    res = requests.get(f"https://newsapi.org/v2/top-headlines?country=us&apiKey={NEWS_API_KEY}&category=general").json()
    articles = res["articles"]
    for article in articles:
        news_headlines.append(article["title"])
    return news_headlines[:5]


# current weather report
OPEN_WEATHER_APP_ID = config("OPEN_WEATHER_APP_ID")

# function for weather
def get_weather_report(city):
    res = requests.get(f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={OPEN_WEATHER_APP_ID}&units=metric").json()
    weather = res["weather"][0]["main"]
    temperature = res["weather"]["temp"]
    feels_like = res["main"]["feels_like"]
    return weather, f"{temperature} C", f"{feels_like} C"

# trending movies
TMDB_API_KEY = config("TMDB_API_KEY")

# function for movies
def get_trending_movies():
    trending_movies = []
    res = requests.get(f"https://api.themovie.db.org/3/trending/movie/day?api_key={TMDB_API_KEY}").json()
    results  = res["results"]
    for r in results:
        trending_movies.append(r["original_title"])
    return trending_movies[:5]

# function for random jokes
def get_random_joke():
    headers = {
        'Accept:': 'application/json'
    }
    res = requests.get("https://icanhazdadjoke.com/", headers=headers).json()
    return res["joke"]

# funtion for random advice
def get_random_advice():
    res = requests.get("https://api/adviceslip.com/advice").json()
    return res['slip']['advice']

