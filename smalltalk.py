# imports
import datetime
from tkinter import *
from tkinter import font
from tkinter import messagebox
from PIL import Image, ImageTk
import random
import os
import wikipedia
import webbrowser
import pyttsx3
import requests
import wolframalpha as wf

#_____________________________________________________________________________________________________________________
#some user inputs
# greetings
GREETING_INPUTS = ["hi there", "how are you", "is anyone there?", "hey", 
                    "hola", "hello", "good day", "hi", "good morning",
                    "good afternon", "good night", "hello arjun", "sup", "whats up", "what's up", "good evening"]

GREETING_RESPONSES = ["Hi there, how can I help?", "Good to see you again",
                     "Hello, thanks for asking","Hi", "Hello", "Hey",
                      "Hey there!", "Enjoying"]

# goodbye
GOODBYE_INPUTS = ["bye", "see you later", "goodbye", "nice chatting to you, bye",
                 "till next time ","ok bye", "okbye", "see ya", "see u",
                  "see you soon", "see u soon", "meet you again", "exit",
                  "ok bye see you soon", "shut up", "shut up your mouth"]

GOODBYE_RESPONSES = ["See you!", "Have a nice day", "Bye! Come back again soon",
                    "Bye!", "Take care"]
VOICE_INPUTS = ["your voice is very nice", "you have a nice voice", "you have nice voice", "nice voice",
                "pretty voice", "preety voice"]
VOICE_RESPONSES = ["That's nice", "Thanks"]

# exceptions

EXCEPTION_VOICE = ["Could not understand your audio. please try again.",
                    "Could not hear you. Please try again."]
EXCEPTION_ELSE = ["Sorry, I don't know the answer for that.\n I can search the web for you.\n Do You want to continue?"]

#safety asssurance
SAFETY_INPUTS = ["are you safe", "safe", "are you hacking my data", "hacked my data", "hacking data", "my data"]
SAFETY_RESPONSES = ["Just relax, Your information is safe.", "I am not hacking your machine.", "I am just trying to give you my best. but not by hacking your data.", "I am sorry, you feel that way."]

#android use
ANDROID_INPUTS = ["can i use you in android", "can i use u in android", "can i use in my phone", "can i use u in my phone", "can i use you in my phone"]
ANDROID_RESPONSES = ["Sorry, you can't use me on android or ios."]
# about assistant
ABOUT_INPUTS = ["who are you", "who are you?", "tell me something about yourself"]
ABOUT_RESPONSES = ["I am Arjun, your personal assistant."]
NAME_INPUTS = ["what is your name?", "what is your name", "your name", "ur name", "what's your name", "what's your name", "whats your name", "whats your name",]
NAME_RESPONSES = ["Arjun"]

GENDER_INPUTS = ["what is your gender", "what is your sex", "what's your gender",
                    "are you male or female", "are you male", "are you female"]
GENDER_RESPONSES = ["MALE"]

AGE_INPUTS = ["what is your age", "how old are you", "when was you born", "what is your date of birth",
                "what's your age", "what's your dob", "what is your dob", "your age", "ur age"]
AGE_RESPONSES = ["I was created on 20th september 2020"]

CREATION_INPUTS = ["who made you", "who created you", "who made u",
                    "who created u", "who is your creator", "who is your builder",
                    "who build you", "made", "created", "creator", "built", "god"]
CREATION_RESPONSES = ["I have been created by Shubham Tiwari", 
                         "Shubham Tiwari is my creator.", "Shubham Tiwari"]

CREATOR_INPUTS  = ["who is Shubham Tiwari", "Shubham Tiwari", "Shubham",
                     "tell me something about Shubham Tiwari"]
CREATOR_RESPONSES = ["He is a great human being.", "He is  my creator.", 
                    "Shubham Tiwari is a great mind.", "Because of him I am talking to you."]

ABILITIES_INPUTS = ["what can you do", "what can you do for me", 
                    "how can you help", "how can you help me"]
ABILITIES_RESPONSES = ["""I can perform various tasks like
    Calculations
    Opening an application
    Searching the web
    Answer your queries"""]

APPRECIATION_INPUTS = ["thankyou", "thanks", "thankyou arjun", "thanks for the help",
                        "you are quite intelligent", "smart", "intelligence", "quite intelligent", "intelligent"]
APPRECIATION_RESPONSES = ["Happy to help", "Nice to help you", "Glad you like it",
                            "welcome", "It's my pleasure."]
chatinitializer_words = ["Tell me something about python", "Hello, how can I help you?", "Try saying tell me the time.", "Try saying, open notepad.", "Try saying, open chrome.", "Try saying, tell me today's date", "I am waiting for your commands."]

# time
TIME_INPUTS =["time", "tell me the time", "what is the time", "what's the time", "time please"]
TIME_HOUR = int(datetime.datetime.now().hour)
if TIME_HOUR> 12:
    TIME_SHOW = str(TIME_HOUR-12) + datetime.datetime.now().strftime(":%M") + " PM"
elif TIME_HOUR == 12:
    TIME_SHOW = datetime.datetime.now().strftime("%H:%M") + " PM"
else:
    TIME_SHOW= datetime.datetime.now().strftime("%H:%M") + " AM"

TIME_RESPONSES = [f"The time is {TIME_SHOW}"]

DATE_INPUTS = ["what is the date", "what is the date today", "date", "whats the date today",
               "tell me today's date", "tell me todays date", "arjun tell me the date", "tell me the date"]
DATE = datetime.date.today()
DATE_RESPONSES = [f"Today is {DATE}"]

DATABASE_INPUTS = [GREETING_INPUTS,
                    GOODBYE_INPUTS,
                    VOICE_INPUTS,
                    SAFETY_INPUTS,
                    ANDROID_INPUTS,
                    ABOUT_INPUTS,
                    NAME_INPUTS,
                    GENDER_INPUTS,
                    AGE_INPUTS,
                    CREATION_INPUTS,
                    CREATOR_INPUTS,
                    ABILITIES_INPUTS,
                    APPRECIATION_INPUTS,
                    TIME_INPUTS,
                    DATE_INPUTS
                    ]

DATABASE_RESPONSES = [GREETING_RESPONSES,
                        GOODBYE_RESPONSES,
                        VOICE_RESPONSES,
                        SAFETY_RESPONSES,
                        ANDROID_RESPONSES,
                        ABOUT_RESPONSES,
                        NAME_RESPONSES,
                        GENDER_RESPONSES,
                        AGE_RESPONSES,
                        CREATION_RESPONSES,
                        CREATOR_RESPONSES,
                        ABILITIES_RESPONSES,
                        APPRECIATION_RESPONSES,
                        TIME_RESPONSES,
                        DATE_RESPONSES
                        ]

initializer = []

initializer.extend(GREETING_INPUTS)
initializer.extend(GOODBYE_INPUTS)
initializer.extend(VOICE_INPUTS)
initializer.extend(SAFETY_INPUTS)
initializer.extend(ANDROID_INPUTS)
initializer.extend(ABOUT_INPUTS)
initializer.extend(NAME_INPUTS)
initializer.extend(GENDER_INPUTS)
initializer.extend(AGE_INPUTS)
initializer.extend(CREATION_INPUTS)
initializer.extend(CREATOR_INPUTS)
initializer.extend(ABILITIES_INPUTS)
initializer.extend(APPRECIATION_INPUTS)
initializer.extend(TIME_INPUTS)
initializer.extend(DATE_INPUTS)



#________________________________________________________________________________________________________________________________________________________________________________________________________
class TODO:

    def arjun_response(self, user_response):
        query = user_response
        stop_words = ['in', 'new', 'tab','arjun','window', "degree",'/', '?', '.', '"', "'","`", "~", "!","@","#","$","^","&", "_", "|", ":", ";", ".",","]
        query_words = query.split()
        result_words = [word for word in query_words if word.lower() not in stop_words]
        user_response = " ".join(result_words)

        query = user_response
        stop_words = ['/', '?', '.', '"', "'","`", "~", "!","@","#","$","^","&", "_", "|", ":", ";", ".",","]
        query_words = list(query)
        result_words = [word for word in query_words if word.lower() not in stop_words]
        user_response = "".join(result_words)

        try:
            if user_response in initializer:
                for i in DATABASE_INPUTS:
                    if user_response in i:
                        index = DATABASE_INPUTS.index(i)
                        ans = random.choice(DATABASE_RESPONSES[index])
                        return ans
            
            elif "open" in user_response:
                ans = open_apps(user_response)
                return ans
            
            elif "search" in user_response or "play" in user_response:
                query = user_response
                stop_words = ['what', 'who', 'is', 'for', 'in', 'play', 'search','at']
                query_words = query.split()
                result_words = [word for word in query_words if word.lower() not in stop_words]
                user_response = " ".join(result_words)
                ans = search_web(user_response)
                return ans
            
            elif "can i call you" in user_response or "can i change your name" in user_response:
                ans = "You can't change my name."
                return ans
            
            elif "search wikipedia for" in user_response or "tell me something about" in user_response:
                query = user_response.split()
                stop_words = ["tell", "search", "wikipedia", "for", "me", "something", "about"]
                query_words = query.split()
                result_words = [word for word in query_words if word.lower() not in stop_words]
                results = wikipedia.summary(query, sentences=2)
                ans = "According to wikipedia "+results
                return ans
            
            elif "weather" in user_response:
                api_key = "your api key"
                weather_url = "http://api.openweathermap.org/data/2.5/weather?"
                data = user_response.split()
                stop_words = ["tell", "search", "wikipedia", "for", "me", "something", "about", "what", "is", "the", "weather", "in", "what's", "whats", "my", "area", "of"]
                location = [word for word in data if word.lower() not in stop_words]
                url = weather_url + "appid=" + api_key + "&q=" + location[0] 
                js = requests.get(url).json() 
                if js["cod"] != "404": 
                    weather = js["main"] 
                    temp = weather["temp"] 
                    hum = weather["humidity"] 
                    desc = js["weather"][0]["description"]
                    resp_string = " The temperature in Kelvin is " + str(temp) + ". The humidity is " + str(hum) + " and the weather description is "+ str(desc)+"."
                    return resp_string
                else: 
                    return "City Not Found" 

            else:
                app_id = "wolframalpha app id"
                client = wf.Client(app_id)
                res = client.query(user_response)
                ans = next(res.results).text
                return ans

        except:
            return "Google"

def search_web(message):

    if "youtube" in message:
        ans = "Opening in youtube"
        query = message.lower().replace("youtube", " ")
        webbrowser.open('https://www.youtube.com/results?search_query='+'+'.join(query.split()))
        return ans

    elif "wikipedia" in message:
        query = message.lower().replace("wikipedia", " ")
        result = wikipedia.summary(query, sentences=2)
        ans = "According to wikipedia"+result
        return ans
    
    else:
        if 'google' in message:
            query = message.replace("google", " ")
            webbrowser.open('https://www.google.com/search?q='+'+'.join(query))
        
        else:
            webbrowser.open('https://www.google.com/search?q='+'+'.join(message.split()))
            return


def open_apps(apps):
    query = apps
    stop_words = ['in', 'new', 'tab','window','open', 'play', '/', '?', '.', ';', ':', '"', "'"]
    query_words = query.split()
    result_words = [word for word in query_words if word.lower() not in stop_words]
    apps = " ".join(result_words)

    query = apps
    stop_words = ['/', '?', '.', ';', ':', '"', "'"]
    query_words = list(query)
    result_words = [word for word in query_words if word.lower() not in stop_words]
    apps = "".join(result_words)

    if "netflix" in apps:
        ans="Opening Netflix"
        os.system("start Netflix:")
        return ans
    elif "youtube" in apps:
        ans = "Opening Youtube"
        webbrowser.open('https://www.youtube.com/results?search_query=')
        return ans
    elif "google" in apps:
        ans = "Opening Google"
        webbrowser.open('https://www.google.com/search?q=')
        return ans
    elif "whatsapp" in apps:
        ans = "Opening Whatsapp"
        webbrowser.open("https://web.whatsapp.com/")
        return ans
    elif "chrome" in apps or "google chrome" in apps:
        ans="Opening Google Chrome"
        os.system("start chrome") 
        return ans 
    elif "word" in apps:
        ans="opening Microsoft Word"
        os.system("start winword")
        return ans
    elif "powerpoint" in apps or "ppt" in apps or "presentation" in apps:
        ans = "Opening Microsoft powerpoint"
        os.system("start powerpnt")
        return ans
    elif "firefox" in apps:
        ans="Opening Mozilla Firefox"
        os.system("start firefox")
        return ans
    elif "excel" in apps:
        ans="Opening Microsoft Excel"
        os.system("start excel")
        return ans 
    elif "3d viewer" in apps or "3dviewer" in apps:
        ans="Opening 3D Viewer"
        os.system("start com.microsoft.builder3d:")
        return ans
    elif "action center" in apps or "action centre" in apps:
        ans="Opening Action Center"
        os.system("start ms-actioncenter:")
        return ans
    elif "alarms and clock" in apps or "alarms" in apps or "alarms & clock" in apps:
        ans="Opening Alarms and Clock"
        os.system("start ms-clock:")
        return ans 
    elif "networks" in apps or "available networks" in apps:
        ans="Opening Available Networks"
        os.system("start ms-availablenetworks:")
        return ans 
    elif "calculator" in apps:
        ans="Opening Calculator"
        os.system("start calculator:")
        return ans
    elif "camera" in apps:
        ans="Opening Camera"
        os.system("start microsoft.windows.camera:")
        return ans
    elif "candy crush" in apps or "candy crush soda saga" in apps:
        ans="Opening Candy Crush Soda Saga"
        os.system("start candycrushsodasaga:")
        return ans
    elif "connect" in apps or "wifi" in apps:
        ans="Opening Connect"
        os.system("start ms-projection:")
        return ans
    elif "cortana" in apps or "assistant" in apps:
        ans="Opening Cortana"
        os.system("start ms-cortana:")
        return ans
    elif "cortana services" in apps or "cortana connected services" in apps:
        ans="Opening Cortana Connected Services"
        os.system("start ms-cortana://notebook/?ConnectedServices")
        return ans
    elif "cortana personal info" in apps or "cortana personal information" in apps:
        ans="Opening Cortana Personal Information"
        os.system("start ms-cortana://settings/ManageBingProfile")
        return ans
    elif "device discovey" in apps:
        ans="Opening Device Discovery"
        os.system("start ms-settings-connectabledevices:devicediscovery")
        return ans
    elif "drawboard" in apps or "drawboard pdf" in apps:
        ans="Opening Drawboard PDF"
        os.system("start drawboardpdf:")
        return ans
    elif "facebook" in apps or "fb" in apps:
        ans="Opening Facebook"
        os.system("start fb:")
        return ans
    elif "feedback" in apps or "feedback hub" in apps:
        ans="Opening Feedback Hub"
        os.system("start feedback-hub:")
        return ans
    elif "get help" in apps or "help" in apps:
        ans="Opening Get Help"
        os.system("start 	ms-contact-support:")
        return ans
    elif "groove" in apps or "music" in apps or "groove" in apps:
        ans="Opening Groove Music"
        os.system("start mswindowsmusic:")
        return ans
    elif "mail" in apps:
        ans="Opening Mail"
        os.system("start outlookmail:")
        return ans
    elif "maps" in apps:
        ans="Opening Maps"
        os.system("start bingmaps:")
        return ans
    elif "internet explorer" in apps:
        ans = "Opening Internet Explorer"
        os.system("start iexplore")
        return
    elif "explorer" in apps or "file" in apps or "my computer" in apps or "this pc" in apps:
        ans = "Opening File Explorer"
        os.system("start explorer")
        return
    elif "message" in apps or "messaging" in apps:
        ans="Opening Messaging"
        os.system("start ms-chat:")
        return ans
    elif "microsoft edge" in apps or "edge" in apps:
        ans="Opening Microsoft Edge"
        os.system("start 	microsoft-edge:")
        return ans
    elif "microsoft news" in apps or "news" in apps:
        ans="Opening Microsoft News"
        os.system("start bingnews:")
        return ans
    elif "solitaire" in apps or "microsoft solitaire collection" in apps:
        ans="Opening Microsoft Solitaire Collection"
        os.system("start xboxliveapp-1297287741:")
        return ans
    elif "store" in apps or "microsoft store" in apps:
        ans="Opening Microsoft Store"
        os.system("start ms-windows-store:")
        return ans
    elif "store music" in apps or "microsoft store music" in apps:
        ans="Opening Microsoft Store - Music"
        os.system("start microsoftmusic:")
        return ans
    elif "store movies and tv" in apps or "microsoft store movies and tv" in apps:
        ans="Opening Microsoft Store - Movies & TV"
        os.system("start microsoftvideo:")
        return ans
    elif "whiteboard" in apps or "microsoft whiteboard" in apps:
        ans="Opening Microsoft Whiteboard"
        os.system("start ms-whiteboard-cmd:")
        return ans
    elif "minecraft" in apps:
        ans="Opening Minecraft"
        os.system("start minecraft:")
        return ans
    elif "mixed reality" in apps or "mixed reality camera" in apps:
        ans="Opening Mixed Reality Camera"
        os.system("start ms-holocamera:")
        return ans
    elif "mixed reality portal" in apps:
        ans="Opening Mixed Reality Portal"
        os.system("start ms-holographicfirstrun:")
        return ans
    elif "movies and tv" in apps or "films and tv" in apps:
        ans="Opening Movies & Tv"
        os.system("start mswindowsvideo:")
        return ans
    elif "onenote" in apps:
        ans="Opening OneNote"
        os.system("start onenote:")
        return ans
    elif "paint 3d" in apps:
        ans="Opening Paint 3D"
        os.system("start ms-paint:")
        return ans
    elif "people" in apps:
        ans="Opening People"
        os.system("start ms-people:")
        return ans
    elif "photos" in apps:
        ans="opening Photos"
        os.system("start ms-photos:")
        return ans
    elif "project display" in apps:
        ans="Opening Project Display"
        os.system("start ms-settings-displays-topology:projection")
        return ans
    elif "screen snip" in apps:
        ans="Opening Screen Snip"
        os.system("start ms-screenclip:")
        return ans
    elif "settings" in apps:
        ans="Opening Settings"
        os.system("start ms-settings:")
        return ans
    elif "snip and sketch" in apps:
        ans="Opening Snip & Sketch"
        os.system("start ms-ScreenSketch:")
        return ans
    elif "tips" in apps:
        ans="Opening Tips"
        os.system("start ms-get-started:")
        return ans
    elif "twitter" in apps:
        ans="Opening Twitter"
        os.system("start twitter:")
        return ans
    elif "3d preview" in apps or "view 3d preview" in apps:
        ans="Opening View 3d Preview"
        os.system("start com.microsoft.3dviewer:")
        return ans
    elif "weather" in apps:
        ans="Opening Weather"
        os.system("start bingweather:")
        return ans
    elif "mixed reality environment" in apps or "mixed reality environments" in apps:
        ans="Opening Windows Mixed Reality Environmets"
        os.system("start ms-environment-builder:")
        return ans
    elif "parental controls" in apps:
        ans="Opening Windows Parental Controls"
        os.system("start ms-wpc:")
        return ans
    elif "security" in apps or "windows security" in apps:
        ans="Opening Windows Security"
        os.system("start windowsdefender:")
        return ans
    elif "xbox" in apps:
        ans="Opening Xbox"
        os.system("start xbox:")
        return ans
    elif "xbox friends list" in apps or "friends list in xbox" in apps:
        ans="Opening Xbox - Friends List"
        os.system("start xbox-friendfinder:")
        return ans
    elif "xbox profile page" in apps or "profile page in xbox" in apps:
        ans="Opening Xbox - Profile Page"
        os.system("start xbox-profile:")
        return ans
    elif "xbox network settings" in apps or "network settings in xbox" in apps:
        ans="Opening Xbox - Network Settings"
        os.system("start xbox-network:")
        return ans
    elif "xbox settings" in apps or "settings in xbox" in apps:
        ans="Opening Xbox - Settings"
        os.system("start xbox-settings:")
        return ans
    elif "xbox one smart glass" in apps:
        ans="Opening Xbox One SmartGlass"
        os.system("start smartglass:")
        return ans
    
    elif "notepad" in apps:
        ans = "Opening Notepad"
        os.system("start notepad")
        return ans
    elif "spotify" in apps:
        ans = "Opening Spotify"
        os.system("start spotify")
        return ans
    elif "alexa" in apps:
        ans = "Opening Alexa"
        os.system("start alexa")
        return ans
    else:
        ans="Application not available"
        return ans
