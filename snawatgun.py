from textToSpeech import speak
from random import randint
from voiceToText import commands
win =0    
loss =0  
def greetings():
    speak("Hello, Fellow player.The game is best played while being online. Offline experiences may be inconvinient.")

#takes the user input
def userInput():
    recognised_text = commands()
    return recognised_text.lower() #converts the text to lower case for consistency


""" the match function takes the user input and compares it with the computer choice
    and returns the result of the match. It also keeps track of the wins and losses."""
#(bot v Human)
def match():
    userIn = userInput() #takes the userinput
    if "error--1~`" in userIn :
        userIn = commands() #using offline model incase useer is not online
    while not "water" in userIn.lower() and not "snake" in userIn.lower() and not "gun" in userIn.lower():
        print("could not understand")
        speak("could not understand, please speak again")
        userIn = userInput()

    choices = ["snake","water","gun"] #set of choices computer can make
    comChoice = choices[randint(0,2)] #choices computer makes randomly
    global win,loss
    if  comChoice.lower() in userIn.lower() :
        print(f"Draw\nComputer:{comChoice}\nYou choose:{userIn}\n")
        speak(f"it's a Draw,Computer choose {comChoice}and You choose {userIn}\n")
    elif comChoice =="snake":#incase computer has choosen snake
        if "gun" in userIn.lower():#human = gun & com = snake
            print(f"you won!!\nComputer: {comChoice}You: gun\n")
            speak(f"you won!!\nComputer: {comChoice}You: gun\n")
            win=win + 1
        if "water" in userIn.lower():#human = water & com = snake
            print(f"you lost!!\nComputer: {comChoice} You: water")
            speak(f"you lost!!\nComputer: {comChoice} You: water")
            loss = loss + 1
    elif comChoice =="gun":
        if "water" in userIn.lower():#human = water & com = gun
            print(f"you won!!\nComputer:{comChoice} You: water\n")
            speak(f"you won!!\nComputer:{comChoice} You: water\n")
            win=win + 1
        if "snake" in userIn.lower() :#human = snake & com = gun
            print(f"you lost!!\nComputer:{comChoice} You:snake\n")
            speak(f"you lost!!\nComputer:{comChoice} You:snake\n")
            loss = loss + 1
    elif comChoice == "water":
        if "snake" in userIn.lower():#human = snake & com = water
            print(f"you won!!\nComputer:{comChoice} You:snake\n")
            speak(f"you won!!\nComputer:{comChoice} You:snake\n")
            win=win + 1
        if "gun" in userIn.lower():#human = gun & com = water 
            print(f"you lost!!\nComputer:{comChoice} You:gun\n")
            speak(f"you lost!!\nComputer:{comChoice} You:gun\n")
            loss = loss + 1
    else : #if no input received
        print("invalid move\n")
        speak("invalid move")
        match()

#starts the game
def play():
    while True:

        print("Ready to play?! \nJust choose from snake, water and gun\nThe win is in order:\n (snake-->water)::(water-->gun)::(gun-->snake)")  
        greetings() #greet the user
        for x in range(0,4): 
            print(f"ROUND-->{x+1}\n") 
            speak(f"ROUND {x+1}, what will you choose?")    
            match()
        #declares winner and looser
        if(win>loss):
            print(f"you won the match with {win} Wins and {loss} Losses") 
            speak(f"you won the match with {win} Wins and {loss} Losses")
        elif(win<loss):
            print(f"you lost the match with {win} Wins and {loss} Losses")
            speak(f"you lost the match with {win} Wins and {loss} Losses")
        elif(win==loss):
            print(f"match tied with {win} Wins and {loss} Losses")
            speak(f"match tied with {win} Wins and {loss} Losses")

        #check if the user want to play again
        speak("ready for another game? To type manually say either 'T' or 'Type'")
        query = userInput()

        if "type".lower() in query.lower() or  "t" in query.lower():#if user decides to type
            tryAgain = (input("Play again(Y):::Leave game(L)"))
            if "y" in tryAgain.lower() : 
                play()
        else:#if user decides to say
            tryAgain = ""
            while "" == tryAgain:
                speak("To play again say 'YES' and 'NO' to leave the game")
                tryAgain = userInput()
            if "yes" in tryAgain:
                play()

        speak("Thank you for playing dear use, Hope you enjoyed.") #ends with a goodbye

#
if __name__== "__main__":
    play()