#gives you the current available features of the system
#This script checks if certain features are available based on the user's voice command.

from textToSpeech import speak
from voiceToText import commands
features = ["play music", "open apps", "open websites","play games"]
def check_features(query):
    for feature in features:
        if feature in query:
            return True
    return False
if __name__ == "__main__":
    query = commands().lower()
    # print(f"Recognized text: {query}")  # Debugging step
    if check_features(query):
        speak("Feature available.")
    else:
        speak("Feature not available.")
