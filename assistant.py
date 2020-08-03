import speech_recognition as sr  # install as speechrecognition
import webbrowser
import time
import datetime
import playsound
import re
import os
import sys
import subprocess
import random
import requests
import pyautogui
import wikipedia
import pyttsx3
from gtts import gTTS
from time import ctime

class person:
    name = ''
    def setName(self, name):
        self.name = name

class asis:
    name = 'Assistant'
    def setName(self, name):
        self.name = name

def there_exists(terms):
    for term in terms:
        if term in voice_data:
            return True

def engine_speak(text):
    text = str(text)
    engine.say(text)
    engine.runAndWait()

r = sr.Recognizer() 

def record_audio(ask=''):
    with sr.Microphone() as source:
        if(ask):
            engine_speak(ask)
        r.adjust_for_ambient_noise(source, duration=0.5)
        audio = r.listen(source, 6, 4)
        voice_data = ''
        try:
            voice_data = r.recognize_google(audio)
        except sr.UnknownValueError:
            engine_speak("I didn't get that")
        except sr.RequestError:
            engine_speak('Sorry, my service is down')
        return voice_data.lower()

def engine_speak(audio_string):
    audio_string = str(audio_string)
    tts = gTTS(text=audio_string, lang='en')
    r = random.randint(1, 50000000)
    audio_file = 'audio-' + str(r) + '.mp3'
    tts.save(audio_file)
    playsound.playsound(audio_file)
    print(asis.name + ":", audio_string)
    os.remove(audio_file)

def respond(voice_data):
    if there_exists(['hey', 'hi', 'hello']):
        greetings = ["hey, how can I help you " + person_obj.name, "hey, what's up? " + person_obj.name, "I'm listening " + person_obj.name, "how can I help you? " + person_obj.name, "hello " + person_obj.name, "hi " + person_obj.name]
        greet = greetings[random.randint(0, len(greetings) - 1)]
        engine_speak(greet)

    if there_exists(["what is your name","what's your name","tell me your name"]):
        if person_obj.name:
            engine_speak(f"my name is {asis_obj.name}")
        else:                                                   
            engine_speak(f"my name is {asis_obj.name}. what's your name?")

    if there_exists(["my name is"]):
        person_name = voice_data.split("is")[-1].strip()
        engine_speak("okay, i will remember that " + person_name)
        person_obj.setName(person_name)
    
    if there_exists(["what is my name"]):
        engine_speak("Your name must be " + person_obj.name)
    
    if there_exists(["your name should be"]):
        asis_name = voice_data.split("be")[-1].strip()
        engine_speak("okay, i will remember that my name is " + asis_name)
        asis_obj.setName(asis_name)
   
    if there_exists(["how are you", "how are you doing", "what's up"]):
        engine_speak("I'm very well, thanks for asking " + person_obj.name)
    
    if there_exists(["how old are you"]):
        engine_speak("I'm quite young, I'm still learning")

    if there_exists(["what's the time", "tell me the time", "what time is it", "what is the time", "time now"]):
        time = ctime().split(" ")[3].split(":")[0:2]
        if time[0] == "00":
            hours = '12'
        else:
            hours = time[0]
        minutes = time[1]
        time = hours + " hours and " + minutes + "minutes"
        engine_speak(time)
    
    if there_exists(['open website']):
        reg_ex = re.search('open website (.+)', voice_data)
        if reg_ex:
            domain = reg_ex.group(1)
            url = 'https://www.' + domain
            webbrowser.open(url)
    
    if there_exists(['music', 'play music', 'songs']):
        url = "https://www.youtube.com/watch?v=l0U7SxXHkPY&list=RDMM&start_radio=1"
        webbrowser.get().open(url)
    
    if there_exists(['restaurants', 'restaurants near me', 'nearby restaurants']):
        url = "https://www.google.com/search?q=restaurants+near+me"
        webbrowser.get().open(url)

    if there_exists(['supermarket', 'supermarket near me', 'nearby supermarket']):
        url = "https://www.google.com/search?q=supermarket+near+me"
        webbrowser.get().open(url)

    if there_exists(['i need a haircut', 'hair salon', 'hair saloon', 'haircut', 'nearby hair salon']):
        url = "https://www.google.com/search?q=hair+salon+near+me"
        webbrowser.get().open(url)

    if there_exists(['barber', 'barber shop', 'i need a barber', 'nearby barber shop']):
        url = "https://www.google.com/search?q=barber+shop+near+me"
        webbrowser.get().open(url)

    if there_exists(['pet shop', 'pet shops', 'pet shops near me']):
        url = "https://www.google.com/search?q=pet+shops+near+me"
        webbrowser.get().open(url)

    if there_exists(['butcher', 'butcher shop']):
        url = "https://www.google.com/search?q=butchers+near+me"
        webbrowser.get().open(url)

    if there_exists(['coffee', 'coffee shops']):
        url = "https://google.com/search?q=coffee+shops+near+me"
        webbrowser.get().open(url)

    if there_exists(['bars', 'bars near me', 'drinks']):
        url = "https://www.google.com/search?q=bars+near+me"
        webbrowser.get().open(url)

    if there_exists(['clubs', 'clubs near me']):
        url = "https://www.google.com/search?q=clubs+near+me"
        webbrowser.get().open(url)
        
    if there_exists(['news', 'latest news', 'news feed', 'top stories']):
        url = "https://news.google.com/"
        webbrowser.get().open(url)

    if there_exists(['gmail', 'g mail', 'geemail']):
        url = "https://www.google.com/gmail/" 
        webbrowser.get().open(url)
    
    if there_exists(['facebook', 'open facebook']):
        url = "https://facebook.com"
        webbrowser.get().open(url)

    if there_exists(['github']):
        url = "https://github.com"
        webbrowser.get().open(url)

    if there_exists(["search"]) and 'youtube' not in voice_data:
        search_term = voice_data.split("search")[-1]
        url = "https://google.com/search?q=" + search_term
        webbrowser.get().open(url)
        engine_speak("Here is what I found for" + search_term)

    if there_exists(["youtube"]):
        search_term = voice_data.split("youtube")[-1]
        url = "https://www.youtube.com/results?search_query=" + search_term
        webbrowser.get().open(url)
        engine_speak("Here is what I found for" + search_term + " on youtube")
    
    if there_exists(["game"]):
        voice_data = record_audio("choose among rock paper or scissor")
        moves = ["rock", "paper", "scissor"]
        cmove = random.choice(moves)
        pmove = voice_data
        engine_speak("The computer chose " + cmove)
        engine_speak("You chose " + pmove)
        if pmove == cmove:
            engine_speak("the match is draw")
        elif pmove == "rock" and cmove == "scissor":
            engine_speak("Player wins")
        elif pmove == "rock" and cmove == "paper":
            engine_speak("Computer wins")
        elif pmove == "paper" and cmove == "rock":
            engine_speak("Player wins")
        elif pmove == "paper" and cmove == "scissor":
            engine_speak("Computer wins")
        elif pmove == "scissor" and cmove == "paper":
            engine_speak("Player wins")
        elif pmove == "scissor" and cmove == "rock":
            engine_speak("Computer wins")
   
    if there_exists(["price of"]): 
        search_term = voice_data.split("of")[-1]
        url = "https://google.com/search?q=" + search_term + "%20stock"
        webbrowser.get().open(url)
        engine_speak("Here is what I found for" + search_term)

    if there_exists(["weather"]):
        search_term = voice_data.split("weather")[-1]
        url = "https://google.com/search?q=weather"
        webbrowser.get().open(url)
        engine_speak("Here is what I found for weather")
    
    if there_exists(["my region"]):
        Ip_info = requests.get('https://api.ipdata.co?api-key=test').json()
        loc = Ip_info['region']
        engine_speak(f"You must be somewhere in {loc}")    
        
    if 'find location' in voice_data:
        location = record_audio('What is the location?')
        url = "https://google.com/maps/place/" + location
        webbrowser.get().open(url)
        engine_speak('Here is the location of ' + location)
    
    #Current location from Google maps
    if there_exists(["what is my exact location", "what's my exact location", "my exact location", "my location", "where am i"]):
        url = "https://www.google.com/maps/search/Where+am+I+?/"
        webbrowser.get().open(url)
        engine_speak("You must be somewhere near here, as per Google maps")  

    def note(voice_data):
        date = datetime.datetime.now()
        file_name = str(date).replace(":", "-") + "-note.txt"
        with open(file_name, "w") as f:
            f.write(voice_data)
        subprocess.Popen(["notepad.exe", file_name])
        #os.system('Notepad')

    NOTE_STRS = ["make a note", "write this down", "remember this", "type this"]
    for phrase in NOTE_STRS:
        if phrase in voice_data:
            engine_speak("What would you like me to write down? ")
            write_down = record_audio()
            note(write_down)
            engine_speak("I've made a note of that.")
    
    if there_exists(['open calculator']):
        os.system('calc')

    if there_exists(['open calendar']):
        url = "https://calendar.google.com/calendar"
        webbrowser.get().open(url)

    if there_exists(['open mail', 'open the mail']):
        os.startfile('Outlook')

#    if there_exists(['open photos']):
#        os.system('Photos')
#
#    if there_exists(['open settings', 'settings']):
#        os.startfile('C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Settings')

    if there_exists(["user", "users"]):
        path = "C:/Users"
        path = os.path.realpath(path)
        os.startfile(path)

    if there_exists(["capture", "my screen", "screenshot"]):
        z = random.randint(1, 50000000)
        myScreenshot = pyautogui.screenshot()
        myScreenshot.save('C:/Users/user/image' + str(z) + '.png') 
        
    if there_exists(["definition"]): 
        try:
            definition = record_audio("What do you need the definition of?")
            wiki = wikipedia.page(str(definition))
            url = wiki.url
            webbrowser.get().open(url)
            print(wikipedia.summary(str(definition), sentences=2))
        except:
                engine_speak("I am sorry I could not find the definition for " + definition)
    
    if there_exists(["exit", "quit", "goodbye", "bye", "sleep", "i'm out"]):
        engine_speak("bye")
        sys.exit("Bye")

time.sleep(1)

person_obj = person()
person_obj.name = ''
asis_obj = asis()
asis_obj.name = 'Assistant'
engine = pyttsx3.init()
engine_speak('How can I help you?')

while 1:
    voice_data = record_audio("Recording")
    print("Q:", voice_data)
    respond(voice_data)
    
