import pyttsx3
import speech_recognition as sr
import wikipedia
import datetime
import wolframalpha
import webbrowser
import time
import subprocess
import requests
import ecapture as ec

engine = pyttsx3.init('sapi5')    
voices= engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)

def speak(audio):
    engine.say(audio)  
    engine.runAndWait() 

def wishMe():
    hour= int(datetime.datetime.now().hour)
    if hour>= 0 and hour<12:
        speak ("Good Morning Zuhaib") 

    elif hour>= 12 and hour <18:
        speak("Good Afternoon Zuhaib")
    
    else:
        speak("Good Evening Zuhaib")

    speak("How can I help you")

def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening......")
        r.pause_threshold = 1.3
        r.energy_threshold=4000
        audio= r.listen(source)
    
    try:
        print("Recognizing.....")
        statement = r.recognize_google(audio , language='en-in').lower()
        print(f'User said :\n{statement}')
        
    except:
        speak("Pardon me, please say that again")
        time.sleep(2) 
        return "None"
    
    return statement
    
def open_wikipedia(statement) :
    speak('Searching wikipedia.....')
    print('Searching wikipedia.....')
    statement = statement.replace('wikipedia', '')
    results = wikipedia.summary(statement, sentences = 2)
    speak('According to wikipedia, ')
    print(results)
    speak(results)
        
def open_youtube(statement):
    webbrowser.open_new_tab("https://www.youtube.com")
    print('Opening YouTube.....')
    speak("YouTube is open for you")

def open_google(statement):
    webbrowser.open_new_tab("https://www.google.com")
    print('Opening Google.....')
    speak("Google search is open for you")
    
def open_gmail(statement):
    webbrowser.open_new_tab("https://www.gmail.com")
    print('Opening Gmail.....')
    speak("Gmail is open for you")
    
def current_time(statement):
    strTime = datetime.datetime.now().strftime('%H:%M:%S')
    print(f"The time is {strTime}")
    speak(f"The time is {strTime}")
    
def weather(statement):
    api_key = '8ef61edcf1c576d65d836254e11ea420'
    base_url = "https://api.openweathermap.org/data/2.5/weather?"
    print('What is the city name?')
    speak('What is the city name?')
    city_name = takeCommand()
    complete_url = base_url + 'appid=' + api_key + '&q=' + city_name
    response = requests.get(complete_url)
    x = response.json()
    
    if x['cod'] != '404' :
        y = x['main']
        current_temperature = y['temp']
        current_humidity = y['humidity']
        z = x['weather']
        weather_description = z[0]['description']
        print(f'The temperature in {city_name} is ' + str(current_temperature) + ' Kelvin, ' + 'humidity is ' + str(current_humidity) + '% and the' + ' weather description is ' + str(weather_description))
        speak(f'The temperature in {city_name} is ' + str(current_temperature) + ' Kelvin, ' + 'humidity is ' + str(current_humidity) + '% and the' + ' weather description is ' + str(weather_description))

    else :
        print('City not found')
        speak('City not found.')

def ask(statement):
    print('I can answer computational and geographical questions too! What do you want to ask?')
    speak('I can answer computational and geographical questions too! What do you want to ask?')
    question = takeCommand()
    app_id = "R2K75H-7ELALHR35X" 
    client = wolframalpha.Client(app_id)
    res = client.query(question)
    answer = next(res.results).text
    print(answer)
    speak(answer)

def news(statement):
    webbrowser.open_new_tab('https://timesofindia.indiatimes.com/home/headlines')
    print('Here are the latest headlines from Times of India!')
    speak('Here are the latest headlines from Times of India!')
    time.sleep(5)

def whats_next():
    time.sleep(1)
    print("what would you like me to do next?")
    speak("what would you like me to do next?")
    
if __name__ == '__main__':
    wishMe()
    while True:
        statement =takeCommand().lower()
        
        if 'wikipedia' in statement:
            open_wikipedia(statement)
            whats_next()

        elif 'youtube' in statement:
            open_youtube(statement)
            whats_next()
        
        elif 'google' in statement:
            open_google(statement)
            whats_next()
            
        elif 'gmail' in statement:
            open_gmail(statement)
            whats_next()
        
        elif 'weather' in statement:
            weather(statement)
            whats_next()
        
        elif 'ask' in statement:
            ask(statement)
            whats_next()
        
        elif 'news' in statement or 'headlines' in statement:
            news(statement)
            whats_next()
        
        elif 'current time' in statement:
            current_time(statement)
            whats_next()
            
        elif 'search' in statement:
            statement = statement.replace('search', ' ')
            webbrowser.open(statement)
            time.sleep(5)
            whats_next()
        
        elif "take a picture" in statement or "take a photo" in statement or "take my photo" in statement or "take my picture" in statement:
            speak('Taking picture.....')
            print('Taking picture.....')
            ec.capture(0, "PICS", "img.jpg")
            whats_next()
        
        elif 'shutdown system' in statement:
            print("Hold On a Sec ! Your system is on its way to shut down")
            speak("Hold On a Sec ! Your system is on its way to shut down")
            subprocess.call('shutdown / p /f')
                
        elif "restart" in statement:
            print("Hold On a Sec ! Your system is about to restart.")
            speak("Hold On a Sec ! Your system is about to restart.")
            subprocess.call(["shutdown", "/r"])
            
        elif 'who made you' in statement or 'who created you' in statement or 'who built you' in statement :
            print('I was built by Mohammed Zuhaib during his internship')
            speak('I was built by Mohammed Zuhaib during his internship')
            whats_next()
        
        elif 'why are we here today' in statement :
            print('We are here for the Final Phase Internship Presentation')
            speak('We are here for the Final Phase Internship Presentation')
            whats_next()
            
        elif 'who are you' in statement or 'what can you do' in statement:
            print('I am your personal assistant. I am programmed to do minor tasks such as opening youtube, google chrome and gmail,' 
                  'take a photo, tell the time or the weather in different cities, search wikipedia, get headlines from times of india' 
                  'and you can also ask me computational or geograhical questions too!')
            speak('I am your personal assistant. I am programmed to do minor tasks such as opening youtube, google chrome and gmail,' 
                  'take a photo, tell the time or the weather in different cities, search wikipedia, get headlines from times of india' 
                  'and you can also ask me computational or geograhical questions too!')
            whats_next()
            
        elif 'goodbye' in statement or 'good bye' in statement or 'bye' in statement or 'thank you' in statement or 'thankyou' in statement: 
            print("Good bye Zuhaib! Have a good day")
            speak("Good bye Zuhaib! Have a good day")
            break
        

