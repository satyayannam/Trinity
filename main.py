import webbrowser
from urllib.request import urlopen
import pyttsx3
import pyjokes
from quote import quote
import random
import phonenumbers
from datetime import datetime
from playsound import playsound
from tkinter import *
import wikipedia
import json
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
        'r.pause_threshold = 1'
        audio = r.listen(source)

    try:
        query = r.recognize_google(audio, language='en-in')
        speak(query)

    except Exception as e:
        print(e)
        print("Unable to Recognize your voice.")
        return "None"

    return query
def video():
    import cv2
    cap = cv2.VideoCapture('rr.gif')
    if (cap.isOpened() == False):
        print("Error opening video  file")
    while (cap.isOpened()):
        ret, frame = cap.read()
        if ret == True:
            cv2.imshow('Initializing engine', frame)
            if cv2.waitKey(20) & 0xFF == ord('q'):
                break
        else:
            break
    cap.release()
    cv2.destroyAllWindows()
speak('do you want to start the engine')
if 'yes' in takeCommand():
    speak("initializing engine")
    video()
else:
    quit()
speak("hello I'm trinity, how may i help you")
speak("enter here"),takeCommand()
def joke():
    jokes = pyjokes.get_joke()
    my_joke = ('listen this', jokes)
    speak(my_joke)
    speak("how is it")
    revs=takeCommand().lower()
    if 'good'or'nice'in revs:
        speak('thankyou')
    elif 'bad' or 'worst' in revs:
        speak('sorry,I will get better soon')
    else:
        speak('sorry,I will get better soon')

def about_me():
    speak("hello i'm Trinity, I'm a virtual assistant, nice to meet you")

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
def converter():
    import tkinter as tk
    import tkinter.messagebox
    root = tk.Tk()
    root.title("Currency converter by TRINITY")
    Tops = Frame(root, bg='#e6e5e5', pady=2, width=1850, height=100, relief="ridge")
    Tops.grid(row=0, column=0)
    headlabel = tk.Label(Tops, font=('lato black', 19, 'bold'), text='Currency converter :GeeksForGeeks ',
                         bg='#e6e5e5', fg='black')
    headlabel.grid(row=1, column=0, sticky=W)
    variable1 = tk.StringVar(root)
    variable2 = tk.StringVar(root)
    variable1.set("currency")
    variable2.set("currency")
    def RealTimeCurrencyConversion():
        from forex_python.converter import CurrencyRates
        c = CurrencyRates()
        from_currency = variable1.get()
        to_currency = variable2.get()
        if (Amount1_field.get() == ""):
            tkinter.messagebox.showinfo("Error !!", "Amount Not Entered.\n Please a valid amount.")
        elif (from_currency == "currency" or to_currency == "currency"):
            tkinter.messagebox.showinfo("Error !!",
                                        "Currency Not Selected.\n Please select FROM and TO Currency form menu.")
        else:
            new_amt = c.convert(from_currency, to_currency, float(Amount1_field.get()))
            new_amount = float("{:.4f}".format(new_amt))
            Amount2_field.insert(0, str(new_amount))
    def clear_all():
        Amount1_field.delete(0, tk.END)
        Amount2_field.delete(0, tk.END)
    CurrenyCode_list = ["INR", "USD", "CAD", "CNY", "DKK", "EUR"]
    root.configure(background='#e6e5e5')
    root.geometry("700x400")
    Label_1 = Label(root, font=('lato black', 27, 'bold'), text="", padx=2, pady=2, bg="#e6e5e5", fg="black")
    Label_1.grid(row=1, column=0, sticky=W)
    label1 = tk.Label(root, font=('lato black', 15, 'bold'), text="\t Amount : ", bg="#e6e5e5", fg="black")
    label1.grid(row=2, column=0, sticky=W)
    label1 = tk.Label(root, font=('lato black', 15, 'bold'), text="\t From Currency : ", bg="#e6e5e5", fg="black")
    label1.grid(row=3, column=0, sticky=W)
    label1 = tk.Label(root, font=('lato black', 15, 'bold'), text="\t To Currency : ", bg="#e6e5e5", fg="black")
    label1.grid(row=4, column=0, sticky=W)
    label1 = tk.Label(root, font=('lato black', 15, 'bold'), text="\t Converted Amount : ", bg="#e6e5e5", fg="black")
    label1.grid(row=8, column=0, sticky=W)
    Label_1 = Label(root, font=('lato black', 7, 'bold'), text="", padx=2, pady=2, bg="#e6e5e5", fg="black")
    Label_1.grid(row=5, column=0, sticky=W)
    Label_1 = Label(root, font=('lato black', 7, 'bold'), text="", padx=2, pady=2, bg="#e6e5e5", fg="black")
    Label_1.grid(row=7, column=0, sticky=W)
    FromCurrency_option = tk.OptionMenu(root, variable1, *CurrenyCode_list)
    ToCurrency_option = tk.OptionMenu(root, variable2, *CurrenyCode_list)
    FromCurrency_option.grid(row=3, column=0, ipadx=45, sticky=E)
    ToCurrency_option.grid(row=4, column=0, ipadx=45, sticky=E)
    Amount1_field = tk.Entry(root)
    Amount1_field.grid(row=2, column=0, ipadx=28, sticky=E)
    Amount2_field = tk.Entry(root)
    Amount2_field.grid(row=8, column=0, ipadx=31, sticky=E)
    Label_9 = Button(root, font=('arial', 15, 'bold'), text=" Convert ", padx=2, pady=2, bg="lightblue", fg="white",
                     command=RealTimeCurrencyConversion)
    Label_9.grid(row=6, column=0)
    Label_1 = Label(root, font=('lato black', 7, 'bold'), text="", padx=2, pady=2, bg="#e6e5e5", fg="black")
    Label_1.grid(row=9, column=0, sticky=W)
    Label_9 = Button(root, font=('arial', 15, 'bold'), text=" Clear All ", padx=2, pady=2, bg="lightblue", fg="white",
                     command=clear_all)
    Label_9.grid(row=10, column=0)
    root.mainloop()

def time_now():
    speak("What should i call you")
    uname = takeCommand()
    speak(f'Welcome Mister {uname}')
    now = datetime.now()
    hour = int(datetime.now().hour)
    timenow = now.strftime("%I %M,%p")
    if (hour >= 0) and (hour <= 12) and ('AM' in timenow):
        speak(f'Good morning {uname},the time is {timenow}')
    elif (hour >= 12) and (hour <= 16) and ('PM' in timenow):
        speak(f"good afternoon {uname}, time is {timenow}")
    else:
        speak(f"good evening {uname},the time is {timenow}")

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
        lst= array.array('u', temp_pass)
        random.shuffle(lst)
    password = ""
    for x in lst:
        password = password + x
    print(password)
    speak(password)

def self_protection_badwords():
    bdlist = ["shit", "fuck", "damn", "bitch", "crap", "piss", "darn", "ass hole",
          "bastard", "slut", "douche", "bloody", "bugger"]
    list=random.choice(bdlist)
    speak("if anyone tries to misbehave with me I would say")
    speak(list)


def trins():
    trin=takeCommand().lower()
    if 'joke' in trin:
        joke()
    elif 'quote' in trin:
        quotes()
    elif 'will' in trin:
        descision()
    elif 'number' in trin:
        random_number()
    elif 'service' in trin:
        speak("your phone number with your country code")
        phone_number_service()
    elif 'bad word' in trin:
        self_protection_badwords()
    elif 'time' in trin:
        time_now()
    elif 'play' in trin:
        playsound('C:/Users/DELL/PycharmProjects/The alexa/dubai.mp3')
    elif 'who is' in trin:
        query = trin.replace("who is", "")
        name = query
        speak(name)
        speak(f'searching about {name}')
        info = wikipedia.summary(query, 5)
        speak("according to wikipedia " + info)
    elif 'yourself' in trin:
        about_me()
    elif 'password' in trin:
        speak("suggesting the best and strong password for you")
        password()
    elif 'open' in trin:
        l1 = ["Instagram", "Twitter", "Facebook", "FB", "Wikipedia", "Google", "mail"]
        l2 = ["www.instagram.com", "www.facebook.com", "www.wikipedia.org",
              "www.google.com", "mail.google.com/mail/u/0/#inbox"]
        search1 = takeCommand()
        for i in range(len(l1)):
            if l1[i] in search1:
                engine.say("opening" + l1[i])
                engine.runAndWait()
                webbrowser.open("http://" + l2[i])
            break

    elif "where is" in trin:
        query = trin.replace("where is","")
        location = query
        speak("User asked to Locate")
        speak(location)
        webbrowser.open(f"www.maps.google.com/maps/place/{location}")
    elif 'news' in trin:
        speak("these are some top 10 tech  news according to tech crunch")
        try:
            jsonObj = urlopen(
                '''https://newsapi.org/v2/top-headlines?sources=techcrunch&apiKey=b5a415bd0aa946af8b36d0558f45c1d9''')
            data = json.load(jsonObj)
            i = 1
            for item in data['articles']:
                print(str(i) + '. ' + item['title'] + '\n')
                print(item['description'] + '\n')
                speak(str(i) + '. ' + item['title'] + '\n')
                i += 1
        except Exception as e:
            print(str(e))
    elif "converter" in trin:
        converter()

    elif 'can you dance' in trin:
        speak("yes I can dance, do you want to see")
        import cv2
        cap = cv2.VideoCapture('u.gif')
        if (cap.isOpened() == False):
            print("Error opening video  file")
        while (cap.isOpened()):
            ret, frame = cap.read()
            if ret == True:
                cv2.imshow('Frame', frame)
                if cv2.waitKey(20) & 0xFF == ord('q'):
                    break
            else:
                break
        cap.release()
        cv2.destroyAllWindows()

    else:
        speak("sorry i'll get that soon")


if __name__ == '__main__':
    trins()