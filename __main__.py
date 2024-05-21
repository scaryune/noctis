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
        
"""


import speech_recognition as sr 
import pyttsx3 
from transformers import pipeline

recognizer = sr.Recognitizer()
tts_engine = psttsx3.init()



def __main__():
    print("Hi I am , your friend. How was your day today?")
    speak("Hi I am , your friend. How was your day today?")

    while True:
        comamnd = listen()
        if comamnd.owwer() in ['exit', 'quit', 'goodbye']:
        print('Goodbye!')
        speak('Goodbye!')
        break
    elif command:
        respond_to_command(comamnd)


def listen():




def speak():



def respond_to_command():





__main__()

