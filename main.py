import speech_recognition as sr
import webbrowser
import pyttsx3
from musicLib import songs
from datetime import datetime

engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def processCommand(c):
    if "open google" in c.lower():
        speak("Opening Google")
        webbrowser.open("https://google.com")
    elif "schedule" in c.lower():
        speak("Meeting with Marko at 7:00 pm")
        speak("And date with Arush! Don't forget to bring a gift; it's his birthday!")
    elif "time" in c:
        current_time = datetime.now().strftime("%I:%M %p")
        speak(f"The current time is {current_time}")

    elif c.lower().startswith("play"):
        try:
            play = c.lower().split(" ")[1]
            link = songs[play] 
            play=c.lower().split(" ")[1:] 
            speak(f"Playing {play}")
            webbrowser.open(link)
        except KeyError:
            speak(f"Sorry, I don't know the song {play}.")
        except IndexError:
            speak("Please specify the song name after 'play'.")

if __name__ == "__main__":
    speak("Hey, how may I help you!")

    while True:
        r = sr.Recognizer()

        try:
            with sr.Microphone() as source:
                r.adjust_for_ambient_noise(source, duration=1)
                print("Listening...")
                audio = r.listen(source, timeout=5, phrase_time_limit=5)

            command = r.recognize_google(audio)
            print(f"I heard you say: {command}")  

            if "jarvis" in command.lower():
                speak("Yes")

                with sr.Microphone() as source:
                    r.adjust_for_ambient_noise(source, duration=1)
                    audio = r.listen(source, timeout=5, phrase_time_limit=5)
                    command = r.recognize_google(audio)
                    print(f" {command}")  
                    processCommand(command)
                    
        except sr.UnknownValueError:
            print("Sorry, I did not understand that.")
        except sr.RequestError as e:
            print(f"Could not request results; check your network connection. Error: {e}")
        except Exception as e:
            print(f"Error: {e}")
