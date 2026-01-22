from textToSpeech import speak
import voiceToText
# from newsapi import news
import snawatgun
import greeting
from mongodbConnection import try_log_command
import music
from  open_action_integration import open_command
# Available games
GAMES = ["snake water gun"]

class Desk_Assistant:
    def __init__(self):
        """Initialize the Assistant and greet the user."""
        self.greet()

    def greet(self):
        """Greets the user based on the time of day."""
        # print("Starting assistant...")  # Debugging step
        speak("Starting assistant")
        paher = greeting.paher()  # Returns if it's morning/afternoon/evening
        speak(f"Very {paher} sir, how may I help you?")
        # print(f"Very {paher} sir, how may I help you?")

    def run(self):
        """Main loop for listening and executing commands."""
        while True:

            query = voiceToText.commands()  # Simulating speech recognition

            # Get date and time
            if "date and time" in query or ("what" and "time" in query):
                greeting.speakTime()
                # try_log_command(query, "date and time", success=True, mode="offline")


            # Stop the assistant
            elif "stop" in query or "exit" in query or "shut down" in query or "shut" in query:
                speak("As you wish sir!")
                try_log_command(query, "stop", success=True, mode="offline")
                return "SHUTOFF"

            # Play music
            elif "play music" in query:
                music.playMusic(query)
                try_log_command(query, "play music", success=True, mode="offline")

            # Open apps or websites
            elif "open" in query:
                open_command(query)
            # Play a game
            elif "play game" in query or "play a game" in query or "game" in query:
                snawatgun()
                try_log_command(query, "play game", success=True, mode="offline")   

            elif "snake water gun" in query:
                speak("Starting snake water gun game")
                snawatgun.snake_water_gun()
                try_log_command(query, "play game", success=True, mode="offline")
            
            # else:
            #     speak("Sorry sir,I could not recognise you or yet to have this feature scaled, I'm sorry for inconvenience.")
    
"""----------------------------------------------------------------------------------------------------------------------------"""

# Run the assistant
if __name__ == "__main__":
    assistant = Desk_Assistant()
    assistant.run()

