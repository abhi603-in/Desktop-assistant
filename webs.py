import webbrowser
from textToSpeech import speak
import voiceToText

def open_webs(query):
    websites = [
        ["youtube", "https://www.youtube.com"],
        ["google", "https://www.google.com"],
        ["chat gpt", "https://chat.openai.com/"],
        ["git","https://github.com/"],
        ["khan academy", "https://www.khanacademy.org"],
        ["coursera","https://www.coursera.org"],
        ["udemy","https://www.udemy.com"],
        ["edx","https://www.edx.org"],
        ["reddit","https://www.reddit.com/"],
        ["quora","https://www.quora.com/"],
        ["wikipedia","https://www.wikipedia.org/"],
        ["stackoverflow","https://www.stackoverflow.com/"],
        ["linkedin","https://www.linkedin.com/"],
        ["facebook","https://www.facebook.com/"],
        ["twitter","https://www.twitter.com/"],
        ["instagram","https://www.instagram.com/"],
        ["pinterest","https://www.pinterest.com/"],
        ["tumblr","https://www.tumblr.com/"],
        ["flickr","https://www.flickr.com/"],
        ["vimeo","https://www.vimeo.com/"],
        ["tiktok","https://www.tiktok.com/"],
        ["snapchat","https://www.snapchat.com/"],
        ["whatsapp","https://www.whatsapp.com/"],
        ["telegram","https://www.telegram.org/"],
        ["discord","https://www.discord.com/"],
        ["skype","https://www.skype.com/"],
        ["zoom","https://www.zoom.us/"],
        ["microsoft teams","https://teams.microsoft.com/"],
        ["slack","https://www.slack.com/"],
        ["google drive","https://drive.google.com/"],
        ["dropbox","https://www.dropbox.com/"],
        ["onedrive","https://www.onedrive.com/"],
        ["box","https://www.box.com/"],
        ["icloud","https://www.icloud.com/"],
        ["spotify","https://www.spotify.com/"],
        ["apple music","https://music.apple.com/"],
        ["amazon music","https://music.amazon.com/"],
        ["pandora","https://www.pandora.com/"],
        ["soundcloud","https://www.soundcloud.com/"],
        ["deezer","https://www.deezer.com/"]
    ]
    
    query = query.lower()
    if "open" not in query:
        return False  # no "open" intent

    for webs in websites:
        if webs[0] in query:
            speak(f"Opening {webs[0]} website, sir")
            webbrowser.open(webs[1])
            return True
    return False
if __name__== "__main__":
    query = voiceToText.commands().lower()
    open_webs(query)