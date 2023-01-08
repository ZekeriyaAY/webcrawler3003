from PySide6.QtWidgets import QMainWindow
from PySide6.QtCore import QUrl
from PySide6.QtGui import QDesktopServices
from threading import Thread
from src.get_links import get_links, setCrawlingStatus
import time

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py
#     /Library/Python/3.9/bin/pyside6-uic form.ui -o ui_form.py
# from ui_form import Ui_MainWindow
from app.ui_form import Ui_MainWindow


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.crawlStatus = False   # crawling is not active

        self.ui.actionButton.clicked.connect(self.buttonClicked)
        self.ui.actionButton.clicked.connect(
            self.thread)   # Start crawling in a thread
        self.ui.actionSourceCodes.triggered.connect(self.openSourceCodes)
        self.ui.actionLicense.triggered.connect(self.openLicense)

    def thread(self):
        if self.ui.actionButton.text() != "Stop Crawling!":  # If crawling will be stopped
            return

        TARGET_URL = self.ui.urlInput.text()
        if TARGET_URL and ("." in TARGET_URL):
            t1 = Thread(target=self.crawlStart)
            t1.start()

    def crawlStatusUpdate(self, status):
        self.crawlStatus = status
        setCrawlingStatus(status)

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
            self.ui.urlInput.setStyleSheet(u"QLineEdit {\n"
                                           "	padding-left: 5px;\n"
                                           "	padding-right: 5px;\n"
                                           "	border-style: solid;\n"
                                           "	border-width: 1px;\n"
                                           "	border-radius: 8px;\n"
                                           "	border-color: gray;\n"
                                           "	color: gray;\n"
                                           "}")

        elif status == "stop":  # If crawling stops
            self.ui.urlInput.clear()
            self.ui.urlInput.setReadOnly(False)
            self.ui.urlInput.setStyleSheet(u"QLineEdit {\n"
                                           "	padding-left: 5px;\n"
                                           "	padding-right: 5px;\n"
                                           "	border-style: solid;\n"
                                           "	border-width: 1px;\n"
                                           "	border-radius: 8px;\n"
                                           "	border-color: lightgray;\n"
                                           "	color: lightgray;\n"
                                           "}")

    def inputEmpty(self):
        if not self.ui.urlInput.text() or ("." not in self.ui.urlInput.text()):  # If input is empty or not a valid url
            self.ui.urlInput.setFocus()
            self.ui.outputTextBrowser.clear()
            self.ui.outputTextBrowser.append(
                "Please enter a URL to crawl like <b><i>https://uludag.edu.tr</i></b>")
            return True
        return False    # If input is not empty or not a valid url

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

    def openSourceCodes(self):
        url = QUrl("https://github.com/ZekeriyaAY/webcrawler3003")
        try:
            QDesktopServices.openUrl(url)
        except:
            print("Error: Could not open url")

    def openLicense(self):
        url = QUrl(
            "https://github.com/ZekeriyaAY/webcrawler3003/blob/master/LICENSE")
        try:
            QDesktopServices.openUrl(url)
        except:
            print("Error: Could not open url")

    def crawlStart(self):
        self.crawlStatusUpdate(status=True)  # crawling is active

        TARGET_URL = self.ui.urlInput.text()
        if TARGET_URL.endswith("/"):
            TARGET_URL = TARGET_URL[:-1]

        pages = get_links(TARGET_URL, TARGET_URL)
        self.crawlFinished()

    def crawlFinished(self):
        print("Crawling finished!")
        self.end = time.time()
        self.buttonUpdate(status="stop")    # Change button text
        self.inputUpdate(status="stop")     # Enable input
        self.infoUpdate(status="stop")    # Update info label

    def buttonClicked(self):
        if self.inputEmpty():   # If input is empty or not a valid url
            return
        if self.ui.actionButton.text() == "Stop Crawling!":  # If crawling will be stopped
            self.crawlStatusUpdate(status=False)  # crawling is not active
            self.crawlFinished()    # Stop crawling
            return

        # Crawling starts
        self.start = time.time()
        self.buttonUpdate(status="start")   # Change button text
        self.inputUpdate(status="start")    # Disable input
        self.infoUpdate(status="start")    # Update info label

        self.ui.outputTextBrowser.clear()   # Clear output text browser
