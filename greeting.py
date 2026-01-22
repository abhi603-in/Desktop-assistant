import time
from textToSpeech import speak

t=time.localtime()

def speakTime():
    greet=""
    cur_time = time.strftime('%I:%M:%S%p',t)
    cur_date_words = time.strftime('%a,%d %B,%Y',t)
    cur_Hour = int((time.strftime('%H',t)))
    if cur_Hour<=12 and cur_Hour>=6:
       print("GOOD MORNING")
       greet="GOOD MORNING"
    elif cur_Hour<=16 and cur_Hour>12:
        print("GOOD AFTERNOON")
        greet="GOOD AFTERNOON"
    elif cur_Hour<24 and cur_Hour>16:
        print("GOOD EVENING")
        greet="GOOD EVENING"
    print("Time: ",cur_time,"\nDate: ",cur_date_words)
    toSpeak=f"{greet} Time: {cur_time}, Date: {cur_date_words}"
    # for words in toSpeak:
    #     speaker.speak(words)
    speak(toSpeak)

def paher():
    greet=""
    cur_Hour = int((time.strftime('%H',t)))
    if cur_Hour<=12 and cur_Hour>=6:
       print("GOOD MORNING")
       greet="GOOD MORNING"
    elif cur_Hour<=16 and cur_Hour>12:
        print("GOOD AFTERNOON")
        greet="GOOD AFTERNOON"
    elif cur_Hour<24 and cur_Hour>16:
        print("GOOD EVENING")
        greet="GOOD EVENING"
    return greet
if __name__=="__main__":
   speakTime() 
