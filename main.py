import webbrowser
import pyttsx3
import pyjokes
from quote import quote
import random
import phonenumbers
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

speak("hello I'm trinity, how may i help you")
speak("enter here"),takeCommand()

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
def phone_number_service():
    from phonenumbers import carrier
    number=input("enter here")
    service_provider = phonenumbers.parse(number)
    speak(carrier.name_for_number(service_provider,'en'))

def password():
    import random
    import array
    MAX_LEN = 12
    DIGITS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    LOCASE_CHARACTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
                         'i', 'j', 'k', 'm', 'n', 'o', 'p', 'q',
                         'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
                         'z']
    UPCASE_CHARACTERS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
                         'I', 'J', 'K', 'M', 'N', 'O', 'P', 'Q',
                         'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y',
                         'Z']
    SYMBOLS = ['@', '#', '$', '%', '_', '?', '.', '/', '|', '~', '>',
               '*', '(', ')', '<']
    COMBINED_LIST = DIGITS + UPCASE_CHARACTERS + LOCASE_CHARACTERS + SYMBOLS
    rand_digit = random.choice(DIGITS)
    rand_upper = random.choice(UPCASE_CHARACTERS)
    rand_lower = random.choice(LOCASE_CHARACTERS)
    rand_symbol = random.choice(SYMBOLS)
    temp_pass = rand_digit + rand_upper + rand_lower + rand_symbol
    for x in range(MAX_LEN - 4):
        temp_pass = temp_pass + random.choice(COMBINED_LIST)
        temp_pass_list= array.array('u', temp_pass)
        random.shuffle(temp_pass_list)
    password = ""
    for x in temp_pass_list:
        password = password + x
    print(password)
    speak(password)
def self_protection_badwords():
    bdlist = ["shit", "fuck", "damn", "bitch", "crap", "piss", "darn", "ass hole",
          "bastard", "slut", "douche", "bloody", "bugger"]
    list=random.choice(bdlist)
    speak("if anyone tries to misbihave with me I would say")
    speak(list)
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

def trins():
    trin=takeCommand().lower()
    if 'joke' in trin:
        joke()
    elif 'something' in trin :
        quotes()
    elif 'will' in trin:
        descision()
    elif 'track' in trin:
        Phonenumber_location_tracker()
    elif 'number' in trin:
        random_number()
    elif 'service' in trin:
        speak("your phone number with your country code")
        phone_number_service()
    elif 'badword' or 'like' or 'misbehave' in trin:
        self_protection_badwords()
    elif 'time' in trin:
        time_now()
    elif 'play' in trin:
        playsound('C:/Users/DELL/PycharmProjects/The alexa/dubai.mp3')
    elif ('who is') in trin or 'know' in trin or 'tell' in trin:
        wiki()
    elif 'you' in trin:
        about_me()
    elif 'password' in trin:
        speak("suggesting the best and strong password for you")
        password()
    elif 'search' in trin:
        l1 = ["Instagram", "Twitter", "Facebook", "FB", "Wikipedia", "Google", "mail"]
        l2 = ["www.instagram.com", "www.facebook.com", "www.wikipedia.org",
              "www.google.com", "mail.google.com/mail/u/0/#inbox"]
        search1 = input('...')
        for i in range(len(l1)):
            if l1[i] in search1:
                engine.say("opening" + l1[i])
                engine.runAndWait()
                webbrowser.open_new_tab("http://" + l2[i])
            break
    else:
        speak('sorry i will get that soon')


if __name__ == '__main__':
    trins()