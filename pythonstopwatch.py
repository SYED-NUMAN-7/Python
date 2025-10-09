import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout
from PyQt5.QtCore import QTimer, QTime, Qt

class Stopwatch(QWidget):
    def __init__(self):
        super().__init__()
        self.time = QTime(0, 0, 0, 0)
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Stopwatch")

        # Create the time label
        self.time_label = QLabel("00:00:00.00", self)
        self.time_label.setAlignment(Qt.AlignCenter)

        # Create buttons
        self.start_button = QPushButton("Start", self)
        self.stop_button = QPushButton("Stop", self)
        self.reset_button = QPushButton("Reset", self)

        # Connect buttons to methods
        self.start_button.clicked.connect(self.start)
        self.stop_button.clicked.connect(self.stop)
        self.reset_button.clicked.connect(self.reset)

        # Create timer
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_display)

        # Layouts
        vbox = QVBoxLayout()
        hbox = QHBoxLayout()

        vbox.addWidget(self.time_label)
        hbox.addWidget(self.start_button)
        hbox.addWidget(self.stop_button)
        hbox.addWidget(self.reset_button)
        vbox.addLayout(hbox)

        self.setLayout(vbox)

    def start(self):
        self.timer.start(10)  # Update every 10 milliseconds

    def stop(self):
        self.timer.stop()

    def reset(self):
        self.timer.stop()
        self.time = QTime(0, 0, 0, 0)
        self.time_label.setText(self.format_time(self.time))

    def format_time(self, time):
        hours = time.hour()
        minutes = time.minute()
        seconds = time.second()
        milliseconds = time.msec() // 10  # Two digits for milliseconds
        return f"{hours:02d}:{minutes:02d}:{seconds:02d}.{milliseconds:02d}"

    def update_display(self):
        self.time = self.time.addMSecs(10)
        self.time_label.setText(self.format_time(self.time))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    stopwatch = Stopwatch()
    stopwatch.show()
    sys.exit(app.exec_()) 