""" 
    # Making Advanced AI friend designed to be a highly intelligent, versatile, context-aware 
    personal assistant, capable of understanding natural language, performing a wide range of tasks, and providing insightful responses.

    * Sex
    * Name
    * Atributes 
    * Mood
    * Skills
    * Optional Traits
        
        HEIGHT    <>
        BODY TYPE <>
        FACE TYPE <>
        SKIN TONE <>
        EYE COLOR <>
        LIP COLOR <>
        HAIR COLOR <>
        ETHNICITY <>
        LANGUAGE <>
    
        NOCTIS EMANATOR DETECTED
        CONNECT

    * What libraries will i need ?
        - Speech Recognition
        - pyttsx3
        - PyAudio
        - Tensor flow 
        - Numpy 
        - Pandas 
    * Speech Recognition Text-To-Speech Engine?
    * Define Functions and Classes
        - Classe for Ai friend with everything we needs
        - Function to handle Speech Recognition.
        - Function to handle conversation

    * Create Hadle conversation 
        - Natural conversation with Ai, try track the best way to get human interaction and have good conversation with AI, not only have commands but that feels real.
    * Loop to Keep the assistent runnning
        - Its necessary a loop ? How can i improve it without loop ?
    * Use of Tensor flow to help with Ai
        - Study Tensor flow to be able to give Ai the best capablity's. 
    * Can we use pandas?
    * Create json file or data strutcture file to save the data. 
        - Study how to implement json file or data structure file to save all Ai data 
        - Ai need to be able to recognize is friend 

    speech to text (transcription) > language model > text to speech > speech to talking head > talking head to unreal metahuman > to robot
    Emanator is dispositive you can see the model 3d in hologram
"""

import pyttsx3
import speech_recognition as sr 
import datetime
engine = pyttsx3.init()
voices = engine.getProperty('voices')
# Voice[0] = male Voice[1] = female
engine.setProperty('voice', voices[1])


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def greeting():
    hour = datetime.datetime.now().hour
    if hour >= 6 and hour < 12:
        speak("Good Morning")
    if hour <=12 and hour < 18:
        speak("Good Afternoon")
    if hour <=18 and hour < 24:
        speak("Good Night")

def take_command():
    r = sr.recognizer()
    with sr.Microphone() as source:
        print("Listenning ...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing ...")
        query = r.recognize_google(audio, language='en-US').lower()
        print(query)
    except Exception as e:
        print(e)
        print("Say that again ...")
        return "None"
    return query

def process(empty, just):
    if empty == True:
        query = take_command()
    else:
        print(query)

def time():
    time = datetime.datetime.now().strftime("%I:%M:%S")
    speak("Current time is")
    speak(time)


def day_to_string(day):
    answer = ""
    ones = day % 10
    tens = (day - ones) / 10
    if tens <= 0:
        if ones == 1:
            answer = "first"
        elif ones == 2:
            answer = "second"
        elif ones == 3:
            answer = "third"
        elif ones == 4:
            answer = "fourth"
        elif ones == 5:
            answer = "fifth"
        elif ones == 6:
            answer = "sixth"
        elif ones == 7:
            answer = "seventh"
        elif ones == 8:
            answer = "eightieth"
        elif ones == 9:
            answer = "ninth"
    elif tens == 1:
        if ones == 1:
            answer = "tenth"
        elif ones == 1:
            answer = "eleventh"
        elif ones == 2:
            answer = "twelfth"
        elif ones == 3:
            answer = "thirtteenth"
        elif ones == 4:
            answer = "fourteenth"
        elif ones == 5:
            answer = "fifteenth"
        elif ones == 6:
            answer = "sixteenth"
        elif ones == 7:
            answer = "seventeenth"
        elif ones == 8:
            answer = "eighteenth"
        else : 
            answer = "ninetenth"




if __name__ == "__main__":
    greeting()
    speak("hello world")
    for i in voices:
        print(i.name)
    while True:
        process(True, "")
