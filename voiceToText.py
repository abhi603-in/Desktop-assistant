from vosk import Model, KaldiRecognizer
import sounddevice as sd
import json
import numpy as np
import speech_recognition as sr
from textToSpeech import speak


# Global flag to switch between online and offline mode
locked = False

# Load VOSK offline model once at startup
try:
    model = Model("model")
except Exception as e:
    print(f"[ERROR] Failed to load VOSK model: {e}")
    model = None
    locked = True  # fallback to online if model fails
    speak("Offline model is not available, switching to online mode.")

# ---------------- OFFLINE RECOGNITION ---------------- #

def offline_recognition():
    recognizer = KaldiRecognizer(model, 16000)
    print("Listening...")

    with sd.RawInputStream(samplerate=16000, blocksize=8000, dtype='int16',
                           channels=1) as stream:
        audio_data = bytearray()

        while True:
            block = stream.read(4000)[0]  # read() returns (data, overflow)
            block = bytes(block)
            audio_data.extend(block)

            if recognizer.AcceptWaveform(block):
                result = json.loads(recognizer.Result())
                command = result.get("text", "").strip()  # Remove extra spaces

                if command:
                    print(f"Recognized: {command}")
                    return command
                else:
                    print(f"Recognized: {command}")
                    print("Didn't catch that. Try again.")
                    return ""  # Optional: return empty if nothing detected
# ---------------- ONLINE RECOGNITION ---------------- #
def online_recognition():
    recognizer = sr.Recognizer()

    try:
        with sr.Microphone() as source:
            print("Listening (online)...")
            recognizer.adjust_for_ambient_noise(source, duration=0.5)
            audio = recognizer.listen(source, timeout=5, phrase_time_limit=10)
    except Exception as e:
        print(f"[ERROR] Microphone issue: {e}")
        return "error--1~`"

    try:
        print("Recognizing...")
        recognized_text = recognizer.recognize_google(audio, language="en-in")
        print(f"[Google] You said: {recognized_text}")
        return recognized_text
    except sr.UnknownValueError:
        print("[Google] Could not understand audio")
        return "error--1~`"
    except sr.RequestError as e:
        print(f"[Google] API unavailable: {e}")
        return "error--1~`"

# ---------------- MAIN LOGIC ---------------- #
def commands():
    """
    Get spoken command using online first, then offline as fallback.
    """
    global locked
    text = ""

    if not locked:
        text = online_recognition()
        if text == "error--1~`":
            locked = True
            speak("Sorry sir, Online mode not available. I'll switch you to offline mode.")
            speak("Please repeat your command.")

    if locked:
        text = offline_recognition()
        while not text:
            speak("No command detected, please repeat.")
            text = offline_recognition()

    return text.lower()

# ---------------- ENTRY POINT ---------------- #
if __name__ == "__main__":
    print("Voice assistant is listening...")
    command = commands()
    print(f"[FINAL] Command: {command}")
