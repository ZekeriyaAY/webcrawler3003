from PySide6.QtWidgets import QMainWindow
from PySide6.QtCore import QObject, QThread, Signal
from src.get_links import Worker
import time

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py
#     /Library/Python/3.9/bin/pyside6-uic form.ui -o ui_form.py
from app.ui_form import Ui_MainWindow


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.isOk = False

        self.ui.actionButton.clicked.connect(self.buttonClicked)
        self.ui.actionButton.clicked.connect(self.startCrawl)

    def buttonUpdate(self, status):
        if status == "start":
            self.ui.actionButton.setText("Stop Crawling!")
            self.ui.actionButton.setDefault(False)
        elif status == "stop":
            self.ui.actionButton.setText("Start Crawl")
            self.ui.actionButton.setDefault(True)

    def inputUpdate(self, status):
        if status == "start":   # If crawling starts
            self.ui.urlInput.setReadOnly(True)
            oldStyleSheet = self.ui.urlInput.styleSheet()
            self.ui.urlInput.setStyleSheet(oldStyleSheet + "\nQLineEdit {\n"
                                           "	border-color: gray;\n	color: gray;\n}")
        elif status == "stop":  # If crawling stops
            self.ui.urlInput.setReadOnly(False)
            oldStyleSheet = self.ui.urlInput.styleSheet()
            self.ui.urlInput.setStyleSheet(oldStyleSheet + "\nQLineEdit {\n"
                                           "	border-color: lightgray;\n	color: lightgray;\n}")

    def inputEmpty(self):
        if not self.ui.urlInput.text():  # If input is empty,
            self.ui.urlInput.setFocus()
            self.ui.outputTextBrowser.clear()
            self.ui.outputTextBrowser.append(
                "Please enter a URL to crawl like <b><i>https://uludag.edu.tr</i></b>")
            return True
        return False    # If input is not empty

    def infoUpdate(self, status):
        if status == "start":
            self.ui.infoLabel.setText("Crawling... Please wait!")
        elif status == "stop":
            hours, rem = divmod(self.end - self.start, 3600)
            minutes, seconds = divmod(rem, 60)
            self.ui.infoLabel.setText(
                f'Crawling time: {int(hours):0>2}h {int(minutes):0>2}m {seconds:05.2f}s')

    def outputUpdate(self, output):
        self.ui.outputTextBrowser.append(output)

    def startCrawl(self):
        if not self.isOk:
            return
        # self.thread = QThread()
        # self.worker = Worker()
        # self.worker.moveToThread(self.thread)
        # self.thread.started.connect(lambda: self.worker.crawl(self.ui))
        # self.worker.finished.connect(self.thread.quit)
        # self.worker.finished.connect(self.worker.deleteLater)
        # self.thread.finished.connect(self.thread.deleteLater)
        # self.thread.finished.connect(self.crawlFinished)
        # self.thread.start()
        self.worker = Worker(self.ui)
        self.worker.start()
        self.worker.finished.connect(self.crawlFinished)
        self.worker.output_signal.connect(self.outputUpdate)

    def crawlFinished(self):
        # self.worker.stop()  # Stop crawling
        self.isOk = False
        self.end = time.time()
        self.buttonUpdate(status="stop")    # Change button text
        self.inputUpdate(status="stop")     # Enable input
        self.infoUpdate(status="stop")    # Update info label

    def buttonClicked(self):
        if self.inputEmpty():   # If input is empty,
            return
        if self.ui.actionButton.text() == "Stop Crawling!":  # If crawling will be stopped
            self.crawlFinished()    # Stop crawling
            return

        # Crawling starts
        self.isOk = True
        self.start = time.time()
        self.buttonUpdate(status="start")   # Change button text
        self.inputUpdate(status="start")    # Disable input
        self.infoUpdate(status="start")    # Update info label

        self.ui.outputTextBrowser.clear()   # Clear output text browser
