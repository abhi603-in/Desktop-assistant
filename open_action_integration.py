import apps
from files import open_file
from mongodbConnection import try_log_command
from textToSpeech import speak
import webs


def open_command(query):
    if "website" in query:
        webs_opend = webs.open_webs(query)
        if not webs_opend:
            speak("Sorry sir, I couldn't find that website.")
            try_log_command(query, "open website", success=False, mode="offline")
        else:   
            try_log_command(query, "open website", success=True, mode="offline")    
        return
    elif "app" in query or "application" in query:
        app_opend = apps.open_apps(query)
        if not app_opend:
            speak("Sorry sir, I couldn't find that application.")
            try_log_command(query, "open app", success=False, mode="offline")
        else:
            try_log_command(query, "open app", success=True, mode="offline")    
        return
    elif "file" in query:
        fileopened = open_file(query)
        if not fileopened:
            speak("Sorry sir, I couldn't find that file.")
            try_log_command(query, "open file", success=False, mode="offline")
        else:
            try_log_command(query, "open file", success=True, mode="offline")
        return 
    else:
        opened = webs.open_webs(query)
        if opened:
            try_log_command(query, "open website", success=True, mode="offline")
            return
        opened = apps.open_apps(query)
        if opened:
            try_log_command(query, "open app", success=True, mode="offline")
            return
        opened = open_file(query)   

        if opened:
            try_log_command(query, "open file", success=True, mode="offline")
        else:
            speak("Sorry sir, I couldn't recognize what to open.")
            try_log_command(query, "open unknown", success=False, mode="offline")
        return