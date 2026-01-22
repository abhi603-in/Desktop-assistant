import os
import subprocess
from textToSpeech import speak
import voiceToText
# Common locations where apps might be installed
COMMON_APP_PATHS = [
    r"C:\Program Files",
    r"C:\Program Files (x86)",
    r"C:\Users\{}\AppData\Local\Programs".format(os.getlogin())
]
# UWP apps (like Camera, Calculator)
UWP_APPS = {
    "camera": "microsoft.windows.camera:",
    "calculator": "calculator:",
    "settings": "ms-settings:",
    "store": "ms-windows-store:",
    "mail": "outlookmail:",
    "edge": "microsoft-edge:",
    "calendar": "outlookcal:",
    "photos": "ms-photos:",
    "notepad": "notepad:",
    "snipping tool": "snippingtool:",
    "windows media player": "wmplayer:",
    "windows security": "windowsdefender:",
}


def find_exe(app_name):
    """Search common directories for an .exe file matching the app name."""
    app_name = app_name.lower()

    # Check in PATH first (fastest)
    result = subprocess.run(["where", app_name], capture_output=True, text=True, shell=True)
    paths = result.stdout.splitlines()
    if paths:
        return paths[0]  # Return first found executable

    # Manually scan common install directories
    for folder in COMMON_APP_PATHS:
        if os.path.exists(folder):
            for root, _, files in os.walk(folder):
                for file in files:
                    if file.lower() == f"{app_name}.exe":
                        return os.path.join(root, file)  # Return the full path

    return None  # Not found


def open_apps(query):
    """Find and open an application (UWP or normal .exe)."""
    app_name = query.replace("open ", "").strip().lower()

    # Check if it's a UWP app
    if app_name in UWP_APPS:
        speak(f"Opening {app_name}, sir")
        # subprocess.run(["start", "", UWP_APPS[app_name]], shell=True)
        os.startfile(UWP_APPS[app_name])
        return True

    # Check for a standard .exe app
    exe_path = find_exe(app_name)
    if exe_path:
        speak(f"Opening {app_name}, sir")
        # subprocess.run(["start", "", exe_path], shell=True)
        os.startfile(exe_path)
        return True

    return False


if __name__ == "__main__":
    query = voiceToText.commands()
    for q in query:
        print(f"Query: {q}")
        open_apps(q)
