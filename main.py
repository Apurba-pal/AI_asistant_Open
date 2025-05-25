import speech_recognition as sr
import webbrowser
import pyttsx3 
import musicLibrary
import requests
import os
from groq import Groq

recognizer = sr.Recognizer() # recogniser object to recognise the voice (gives the speech recognition functionality)
engine = pyttsx3.init() # initialise the pyttsx3 engine

# speak a text 
def speak(text):
    engine.say(text)
    engine.runAndWait()

def aiProcessing(command):

    client = Groq(api_key="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")

    completion = client.chat.completions.create(
        model="mixtral-8x7b-32768",
        messages=[
            {
                "role": "user",
                "content": command
            }
        ],
        temperature=1,
        max_tokens=1024,
        top_p=1,
        stream=True,
        stop=None,
    )
    response = ""

    for chunk in completion:
        response += (chunk.choices[0].delta.content or "")
    return(response)


def processCommand(command):
    print(command)
    if "open google" in command.lower():
        webbrowser.open("https://www.google.com/")
    elif "open linkedin" in command.lower():
        webbrowser.open("https://www.linkedin.com/")
    elif "open Chat GPT" in command.lower():
        webbrowser.open("https://chatgpt.com/")
    elif "open youtube" in command.lower():
        webbrowser.open("https://www.youtube.com/")
    elif command.lower().startswith("play"):
        song = command.lower().split( " ")[1]
        link = musicLibrary.music[song]
        webbrowser.open(link)
    
    else:
        output = aiProcessing(command)
        print(f"AI Response: {output}")
        if output:
            speak(output)
        else:
            speak("Sorry, I didn't get a response.")

if __name__ == '__main__':
    speak("Initialising open ... ")
    while True:
        # Listen for the wake word "open"
        # obtain audio from the microphone
        r = sr.Recognizer()
         
        print("recognizing...")
        try:
            with sr.Microphone() as source:
                print("Listening...")
                audio = r.listen(source, timeout=2, phrase_time_limit=1) 
            word = r.recognize_google(audio)
            print(audio)
            if(word.lower() == "open"):
                speak("Ya")
                # Listen for command
                with sr.Microphone() as source:
                    print("open Active...")
                    audio = r.listen(source)
                    command = r.recognize_google(audio)

                    processCommand(command)


        except Exception as e:
            print("Error; {0}".format(e))