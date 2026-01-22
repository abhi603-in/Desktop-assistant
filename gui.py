from PySide6.QtWidgets import QApplication, QPushButton, QVBoxLayout, QWidget, QLabel#defines interface of the desktop assistant
import threading
import assistant # Import your voice automation script
import voiceToText
class VoiceAssistantGUI(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Desktop Assistant")
        self.setGeometry(100, 100, 400, 200)

        self.label = QLabel("", self)
        self.button = QPushButton("Start Assistant", self)
        self.button.clicked.connect(self.run_voice_recognition)

        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.button)
        self.setLayout(layout)

    def run_voice_recognition(self):
        """Runs speech recognition in a separate thread."""
        self.button.setEnabled(False)  # Disable button while listening
        threading.Thread(target=self.recognize_speech, daemon=True).start()

    def recognize_speech(self):
        """Calls the voice recognition function and updates the GUI."""
        Assistant = assistant.Desk_Assistant()
        query = Assistant.run()
        if query == "SHUTOFF":
            self.label.setText("Turned off")
            self.button.setEnabled(True) 
        
def gui_run():
    app = QApplication([])
    window = VoiceAssistantGUI()
    window.show()
    app.exec()

