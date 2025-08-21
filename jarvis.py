import pyttsx3
import speech_recognition as sr
import datetime
import os
import webbrowser
import sys
import time

# Initialize the speech engine
engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[1].id)

# Speak function
def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()

# Function to tell the current time and greet
def tell_time():
    now = datetime.datetime.now()
    hour = now.hour
    current_time = now.strftime("%I:%M %p")  # Format the time as HH:MM AM/PM

    if 0 <= hour < 12:
        speak(f"Good morning Saad! It's {current_time}.")
    elif 12 <= hour < 18:
        speak(f"Good afternoon Saad! It's {current_time}.")
    else:
        speak(f"Good evening Saad! It's {current_time}.")

    speak("My name is Jarvis and I am here to assist you. If you need any help, please let me know.")

# Function to take voice command
def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        sentence = r.recognize_google(audio, language="en-in")
        print(f"User said: {sentence}\n")
    except Exception as e:
        print("Say that again please...")
        return "none"
    
    return sentence.lower()

# Main program
if __name__ == "__main__":
    tell_time()

    while True:
        sentence = take_command()

        # Logic building for tasks
        if "open youtube" in sentence:
            speak("Opening YouTube.")
            webbrowser.open("https://youtube.com")

        elif "open chat gpt" in sentence or "open chatgpt" in sentence:
            speak("Opening ChatGPT.")
            webbrowser.open("https://chat.openai.com")

        elif "spotify" in sentence:
            speak("Opening Spotify.")
            spotify_path = "C:\\Users\\IT-AM17B\\AppData\\Roaming\\Spotify\\Spotify.exe"
            os.startfile(spotify_path)

        elif "open visual studio" in sentence or "open vs code" in sentence:
            speak("Opening Visual Studio Code.")
            vs_path = "C:\\Users\\IT-AM17B\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(vs_path)

        elif "no thanks" in sentence or "exit" in sentence or "shutdown" in sentence or "quit" in sentence:
            speak("Thanks for using me Saad. Jarvis signing off!")
            time.sleep(2)  # Optional: wait 2 seconds before exit
            sys.exit()

        elif sentence == "none":
            continue  # Skip and listen again

        else:
            speak("I'm sorry, I didn't catch that. Could you repeat?")

        


        

        