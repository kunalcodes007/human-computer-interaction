#importing necessary modules


import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia


listen_me = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listen_me.listen(source)
            command = listen_me.recognize_google(voice)
            command = command.lower()
            if 'kunal' in command:
                command = command.replace('kunal', '')
                print(command)
    except:
        pass
    return command


def run_alexa():
    command = take_command()
    print(command)

    #if "a keyword" matches 
    
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing ' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('Current time is ' + time)
    elif 'who the fuck is' in command:
        person = command.replace('who the fuck is', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
    elif 'date' in command:
        talk('sorry, you are not my type')
    elif 'are you single' in command:
        talk('I am in a relationship with wifi')
    else:
        talk('Please say the command again.')


while True:
    run_alexa()
