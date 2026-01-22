# from  textToSpeech import speak
# from voiceToText import commands
# import os
# import subprocess
# COMMON_APP_PATHS = [
#     r"C:\Users\Workspace",
#     r"D:\Workspace",
#     r"C:\Users\Public",
# ]
# def filePath(file_name):
#     file_name = file_name.lower()

#     # Check in PATH first (fastest)
#     result = subprocess.run(["where", file_name], capture_output=True, text=True, shell=True)
#     paths = result.stdout.splitlines()
#     if paths:
#         return paths[0]
    
#     for folder in COMMON_APP_PATHS:
#         if os.path.exists(folder):
#             for root, _, files in os.walk(folder):
#                 for file in files:
#                     file_without_ext, ext = os.path.splitext(file)
#                     if file_without_ext.lower() == file_name or file.lower() == file_name:
#                         return os.path.join(root, file)  # Return the full path

#     return None  # Not found

# def open_file(query):
#     file_name = query.replace("open ", "").strip().lower()
#     file_path = filePath(file_name)

#     if file_path:
#         speak(f"Opening {file_name}, sir")
#         try:
#             os.startfile(file_path)
#             print(f"Opened: {file_path}")
#             return True
#         except Exception as e:
#             print(f"Error opening file: {e}")
#             return False

#     speak(f"Sorry sir, I couldn't find {file_name} file, sir")
#     return False



# if __name__ == "__main__":
#     query =  commands()# Example query, replace with actual input
#     print("started")
#     open_file(query)
#     print("finished")

from textToSpeech import speak
from voiceToText import commands
import os
import subprocess
from pathlib import Path

# Common directories to search
COMMON_APP_PATHS = [
    Path(r"C:\Users") / os.getlogin() / "Desktop",
    Path(r"C:\Users") / os.getlogin() / "Documents",
    Path(r"C:\Users") / os.getlogin() / "Downloads",
    Path(r"D:\Workspace"),
    Path(r"C:\Users\Public"),
]

def filePath(file_name: str) -> str | None:
    """
    Returns full path of file/folder matching the name
    """

    file_name = file_name.lower()

    # Step 1: Try using the system PATH (fastest for known apps)
    try:
        result = subprocess.run(["where", file_name], capture_output=True, text=True, shell=True)
        paths = result.stdout.splitlines()
        if paths:
            return paths[0]
    except Exception as e:
        print(f"[DEBUG] 'where' failed: {e}")

    # Step 2: Walk through common paths
    for folder in COMMON_APP_PATHS:
        if folder.exists():
            for root, _, files in os.walk(folder):
                for file in files:
                    base, ext = os.path.splitext(file)
                    if base.lower() == file_name or file.lower() == file_name:
                        return os.path.join(root, file)

                # Also check for folders with matching name
                for dir in os.listdir(root):
                    full_path = os.path.join(root, dir)
                    if os.path.isdir(full_path) and dir.lower() == file_name:
                        return full_path

    return None  # Not found

def open_file(query: str) -> bool:
    """
    Attempts to open a file/folder from a query string
    """
    file_name = query.lower().replace("open ", "").strip()
    file_path = filePath(file_name)

    if file_path:
        speak(f"Opening {file_name}, sir")
        try:
            os.startfile(file_path)
            print(f"[INFO] Opened: {file_path}")
            return True
        except Exception as e:
            speak("Something went wrong while opening it, sir.")
            print(f"[ERROR] Cannot open file: {e}")
            return False
    else:
        speak(f"Sorry sir, I couldn't find the file or folder named {file_name}.")
        return False

if __name__ == "__main__":
    print("Assistant ready. Listening for your file open command...")
    query = commands()
    print(f"[DEBUG] Command received: {query}")
    open_file(query)
