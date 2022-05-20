import webbrowser
import pyttsx3
import pyjokes
from quote import quote
import random
from datetime import datetime
from playsound import playsound
import wikipedia
import speech_recognition as sr


engine = pyttsx3.init()
engine.setProperty("rate", 140)
sound = engine.getProperty('voices')
engine.setProperty('voice', sound[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def takeCommand():
    r = sr.Recognizer()

    with sr.Microphone() as source:

        print("Listening...")
        'r.pause_threshold = 0'
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        print(e)
        print("Unable to Recognize your voice.")
        return "None"

    return query

speak("hello I'm vlada 2 point o, how may i help you")
speak("enter here"),takeCommand()
l1 = ["Instagram", "Twitter", "Facebook", "FB", "Wikipedia", "Google", "mail"]
l2 = ["www.instagram.com", "www.facebook.com", "www.wikipedia.org",
      "www.google.com", "mail.google.com/mail/u/0/#inbox"]

def joke():
    jokes = pyjokes.get_joke()
    my_joke = ('listen this', jokes)
    speak(my_joke)
    speak("how is it")
    takeCommand()
    if 'good'or'nice'in takeCommand():
        speak('thankyou')
    elif 'bad' or 'worst' in takeCommand():
        speak('sorry,I will get better soon')


    else:
        speak('sorry,I will get better soon')

    return takeCommand()

def about_me():
    speak("hello i'm vlada, I'm a virtual assistant, nice to meet you, how can i help you?")

def quotes():
    res = quote('w', limit=1)
    for i in range(len(res)):
        speak(res)

def descision():
    outcomes = ["no", "yes"]
    desc = random.choice(outcomes)
    my_answer = ('my answer is', desc)
    speak(my_answer)

def random_number():
    rand = random.randrange(1, 6)
    my_number = ('my number is', rand)
    speak(my_number)
    return takeCommand()

def time_now():
    now = datetime.now()
    hour = int(datetime.now().hour)
    timenow = now.strftime("%I %M,%p")
    if (hour >= 0) and (hour <= 12) and ('AM' in timenow):
        speak(f'Good morning babe,the time is {timenow}')
    elif (hour >= 12) and (hour <= 16) and ('PM' in timenow):
        speak(f"good afternoon babe, time is {timenow}")
    else:
        speak(f"good evening babe,the time is {timenow}")

def wiki():
    speak('want to search about something?, search here')
    person = (input('...'))
    print('searching...')
    target1 = person.replace("tell me about", " ")
    info = wikipedia.summary(target1, 5)
    speak("according to wikipedia " + info)

def Phonenumber_location_tracker():
    import datetime
    import phonenumbers
    from phonenumbers import geocoder
    import folium
    from phonenumbers import carrier
    from opencage.geocoder import OpenCageGeocode

    num = input("Enter a number: ")
    time = datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S')
    API_key = "_OPEN_CAGE_GEOCODE_API_KEY_"
    sanNummber = phonenumbers.parse(num)
    location = geocoder.description_for_number(sanNummber, "en")
    sea_pro = phonenumbers.parse(num)
    servise_prover = carrier.name_for_number(sea_pro, 'en')
    geocoder = OpenCageGeocode(API_key)
    quesry = str(location)
    resltt = geocoder.geocode(quesry)
    lat = resltt[0]['geometry']['lat']
    lng = resltt[0]['geometry']['lng']
    mymap = folium.Map(location=[lat, lng], zoom_start=9)
    folium.Marker([lat, lng], popup=location).add_to(mymap)

    return location, servise_prover, lat, lng


#if __name__ == '__main__':
    #while True:
        #query = takeCommand().lower()
if 'joke' in takeCommand():
    joke()
elif 'something' in takeCommand():
    quotes()
elif 'will' in takeCommand():
    descision()
elif 'number' in takeCommand():
    random_number()
elif 'time' in takeCommand():
    time_now()
elif 'play' in takeCommand():
    playsound('C:/Users/DELL/PycharmProjects/The alexa/dubai.mp3')
elif ('who is') in takeCommand() or 'know' in takeCommand() or 'tell' in takeCommand():
    wiki()
elif 'you' in takeCommand():
    about_me()
elif 'search' in takeCommand():
    search1 = input('...')
    for i in range(len(l1)):
        if l1[i] in search1:
            engine.say("opening" + l1[i])
            engine.runAndWait()
            webbrowser.open_new_tab("http://" + l2[i])
        break
else:
    speak('sorry i will get that soon')