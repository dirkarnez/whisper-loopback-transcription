# import soundcard as sc
# import soundfile as sf

# OUTPUT_FILE_NAME = "out.wav"    # file name.
# SAMPLE_RATE = 48000              # [Hz]. sampling rate.
# RECORD_SEC = 5                  # [sec]. duration recording audio.

# with sc.get_microphone(id=str(sc.default_speaker().name), include_loopback=True).recorder(samplerate=SAMPLE_RATE) as mic:
#     # record audio with loopback from default speaker.
#     while True:
#         data = mic.record()
#         print(data.size)
    
#     # # change "data=data[:, 0]" to "data=data", if you would like to write audio as multiple-channels.
#     # sf.write(file=OUTPUT_FILE_NAME, data=data, samplerate=SAMPLE_RATE)
import sys
import random
from PySide6 import QtCore, QtWidgets

class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.hello = ["Hallo Welt", "Hei maailma", "Hola Mundo", "Привет мир"]

        self.button = QtWidgets.QPushButton("Click me!")
        self.text = QtWidgets.QLabel("Hello World",
                                     alignment=QtCore.Qt.AlignCenter)

        self.layout = QtWidgets.QVBoxLayout(self)
        self.layout.addWidget(self.text)
        self.layout.addWidget(self.button)

        self.button.clicked.connect(self.magic)

    @QtCore.Slot()
    def magic(self):
        self.text.setText(random.choice(self.hello))

if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    widget = MyWidget()
    widget.resize(800, 600)
    widget.setWindowFlags(QtCore.Qt.WindowType.FramelessWindowHint | QtCore.Qt.WindowType.WindowStaysOnTopHint)
    widget.show()

    sys.exit(app.exec())