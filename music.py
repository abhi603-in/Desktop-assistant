from textToSpeech import speak
import voiceToText 
import os
import re

def playMusic(query):
    music_dir = "C:\\Users\\Workspace\\Music"
    songs = os.listdir(music_dir)
    speak("Sir, the available songs in the current music directory are:")
    for file in songs:
        print(re.sub(r"_", " ", file[:-4]))
    speak("Which one would you like to play?")
    play_song = voiceToText.commands()
    for song in songs:
        if f"play {re.sub(r'_', ' ', song[:-4])}" in play_song:
            os.startfile(os.path.join(music_dir, song))
if __name__ == "__main__":
    query = voiceToText.commands().lower()
    playMusic(query)