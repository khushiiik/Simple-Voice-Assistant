import speech_recognition as sr
import webbrowser
import pyttsx3
from datetime import datetime

engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def processCommand(c):
    print(f"Command received: {c}")
    c = c.lower()
    
    if "open google" in c:
        webbrowser.open("https://google.com")
    elif "schedule" in c:
        speak("Meeting with Marko at 7:00 pm")
        speak("And date with Arush! Don't forget to bring a gift; it's his birthday!")
    elif "time" in c:
        current_time = datetime.now().strftime("%I:%M %p")
        speak(f"The current time is {current_time}")

def listen_for_jarvis():
    r = sr.Recognizer()
    listening_for_command = False

    while True:
        try:
            with sr.Microphone() as source:
                r.adjust_for_ambient_noise(source, duration=1)
                print("Listening...")
                audio = r.listen(source, timeout=5, phrase_time_limit=5)
            
            command = r.recognize_google(audio)
            print(f"Recognized command: {command}")

            if not listening_for_command:
                if "jarvis" in command.lower():
                    speak("Jarvis Active!")
                    speak("Hey Khushi! How may I help you?")
                    listening_for_command = True
            else:
                processCommand(command)
                
        except sr.UnknownValueError:
            print("Sorry, I did not understand that.")
        except sr.RequestError as e:
            print(f"Could not request results; check your network connection. Error: {e}")
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__dup__":
    speak("Hey, how may I help you!")
    listen_for_jarvis()
