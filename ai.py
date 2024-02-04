import speech_recognition as sr
import os
import win32com.client
import webbrowser
import datetime
import requests
import schedule
import time

# speak function for the AI bot
def speak_function(x):
    speaker = win32com.client.Dispatch("SAPI.SpVoice")
    speaker.Speak(x)


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = 0.5  # seconds of non-speaking audio before a phrase is considered complete
        print("Listening...")
        audio = r.listen(source)
        print("Recognizing...")
        try:
            query = r.recognize_google(audio, language="en-us")
            print(f"User said: {query}")
            return query
        except sr.UnknownValueError:
            print("Sorry, I didn't catch that. Please try again.")
            return ""


# Function to fetch the latest news headlines
def get_latest_news(api_key, country_code="us", category="health", count=3):
    url = f"https://newsapi.org/v2/top-headlines"
    params = {
        "apiKey": api_key,
        "country": country_code,
        "category": category,
        "pageSize": count
    }
    response = requests.get(url, params=params)
    news_data = response.json()

    # Extract news headlines
    headlines = [article["title"] for article in news_data.get("articles", [])]
    return headlines


# Function to speak the news headlines
def speak_news(headlines):
    for index, headline in enumerate(headlines, start=1):
        speak_function(f"News {index}: {headline}")


if __name__ == '__main__':
    news_api_key = "6fd1801e0a394b4da4fdf2dfaa67283d"
    speak_function("Personal Helper")

    while True:
        query = takeCommand()
        # Add more sites for more flexibility
        sites = [["Therapy", "https://buddyhelp.org/chat/"], ["Anxiety", "https://connect.crisistextline.org/chat"],
                 ["Assault", "https://www.thehotline.org/"],
                 ["Pride", "https://pflag.org/resource/support-hotlines/"],
                 ["Eating Disorder", "https://www.nationaleatingdisorders.org/get-help/"],
                 ["Period Problem",
                  "https://www.womenshealth.gov/menstrual-cycle/period-problems#:~:text=For%20more%20information%20about%20period,American%20Society%20for%20Reproductive%20Medicine/"]]
        for site in sites:
            if f"open {site[0]}".lower() in query.lower():
                speak_function(f"Opening {site[0]}")
                webbrowser.open(site[1])

        if "the time" in query:
            hour = datetime.datetime.now().strftime("%H")
            minute = datetime.datetime.now().strftime("%M")
            speak_function(f"The time is {hour} hours and {minute} minutes")

        elif "open facetime".lower() in query.lower():
            # set an emergency number such as parents or a close friend
            os.system(f"open/System/Applications/FaceTime.app", "tel://911")

        elif "shoes".lower() in query.lower():
            # automatically plays your ringtone so that you can pretend that you are getting a call and can try to escape an uncomfortable situation
            # you can say normal conversation phrases such as "Your shoes look good" the AI will recognize the word shoes and play the ringtone
            file_path = "C:/Users/Anup/Downloads/7120-download-iphone-6-original-ringtone-42676.mp3"
            os.system(f'start {file_path}')

        # To get and speak the latest news
        elif "news".lower in query.lower():
            speak_function("Fetching the latest news headlines.")
            news_headlines = get_latest_news(api_key=news_api_key, count=3)
            speak_news(news_headlines)

        elif "reset chat".lower() in query.lower():
            chatStr = ""

        elif "quit".lower in query.lower():
            quit()
