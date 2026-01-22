import pyttsx3;

def speak(text):
    # Initialize pyttsx3
    engine = pyttsx3.init()
    engine.setProperty("rate", 150)
    engine.setProperty("volume", 1.0)
    voices = engine.getProperty("voices")
    engine.setProperty("voice", voices[1].id)
    engine.say(text)
    engine.runAndWait()


if __name__ == "__main__":
    speak("Hello, sir! How can I assist you today?")