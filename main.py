import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibrary
import singing

recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def processCommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")
    elif "open linkedin" in c.lower():
        webbrowser.open("https://linkedin.com")
    elif c.lower().startswith("play"):
        song = c.lower().split(" ")[1]
        link = musicLibrary.music[song]
        webbrowser.open(link)
    elif "Good morning" in c.lower():
        speak("Good morning, how can I assist you today?")
    elif c.lower().startswith("song"):
        son = c.lower().split(" ")[1]
        lyrics = singing.sing[son]
        # print(f"Singing: {lyrics}")
        speak(lyrics)

if __name__ == "__main__":
    speak(" Initializing Jarvis....")
    while True:
#         # Listen for the wake word "Jarvis"
#         # obtain audio from the microphone
#         

#         # recognize speech using Sphinx
        print("recognizing...")
        try:
            with sr.Microphone() as source:
                print("Listening for wake word 'Jarvis'...")
                audio = recognizer.listen(source, timeout=5, phrase_time_limit=3)
            word = recognizer.recognize_google(audio).lower()
            if word == "jarvis":
                speak("Yup , I'm Here!!..")
                print("Jarvis Active...")
                # Listen for command 
                with sr.Microphone() as source:
                    print("Listening for command...")
                    audio = recognizer.listen(source, timeout=5, phrase_time_limit=3)
                    # audio = r.listen(source)
                    command = recognizer.recognize_google(audio).lower()
                    
                    processCommand(command)
                    speak("Command executed.")


        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand the audio")
        except sr.RequestError as e:
            print(f"Could not request results from Google Speech Recognition service; {e}")
        except Exception as e:
            print(f"Error: {e}")

