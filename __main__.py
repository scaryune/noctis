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

    speech to text (transcription) > language model > text to speech > speech to talking head > talking head to unreal metahuman > to robot
"""

import pyttsx3 
engine = pyttsx3.init()
voices = engine.getProperty('voices')
# Voice[0] = male Voice[1] = female
engine.setProperty('voice', voices[1])


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

if __main__ = "__main__":
    speak("Hello World")
    for i in voices:
        print(i.name)
def __main__():





__main__()

