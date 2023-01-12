from PySide6.QtWidgets import QMainWindow
from PySide6.QtCore import QUrl, QThread, Signal
from PySide6.QtGui import QDesktopServices
from threading import Thread
from src.get_links import get_links, setCrawlingStatus, mkdir_pages
from src.utils import cmd
import time
import os
import shutil

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py
#     /Library/Python/3.9/bin/pyside6-uic form.ui -o ui_form.py
# from ui_form import Ui_MainWindow
from app.ui_form import Ui_MainWindow


class Worker(QThread):
    def __init__(self, _TARGET_URL, _crawlStatus):
        super().__init__()
        self.TARGET_URL = _TARGET_URL
        self.crawlStatus = _crawlStatus
        self.pages = []

    print_pages = Signal(int)

    def set_crawlStatus(self, status):
        self.crawlStatus = status

    def run(self):
        while self.crawlStatus:
            self.pages = mkdir_pages(self.TARGET_URL)
            self.print_pages.emit(len(self.pages))
            print(self.pages)
            time.sleep(2)


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.crawlStatus = False   # crawling is not active
        self.TARGET_URL = ""

        self.ui.actionButton.clicked.connect(self.buttonClicked)
        self.ui.actionButton.clicked.connect(self.printOutput)
        # self.ui.actionButton.clicked.connect(
        #     self.thread)   # Start crawling in a thread
        self.ui.actionSourceCodes.triggered.connect(self.openSourceCodes)
        self.ui.actionLicense.triggered.connect(self.openLicense)

    def threadCrawl(self):
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

    def printPages(self, len_pages):
        self.ui.outputTextBrowser.clear()
        self.ui.outputTextBrowser.append(
            f"Total crawled pages: <b>{len_pages}</b><br>")
        output = cmd("tree/tree.py output/.")
        self.ui.outputTextBrowser.append(output)

    def printOutput(self):
        if self.crawlStatus == False:  # If crawling is not active
            try:
                self.worker.set_crawlStatus(False)
            except:
                pass
        if self.ui.actionButton.text() == "Stop Crawling!":  # If crawling will be stopped
            self.worker = Worker(self.TARGET_URL, self.crawlStatus)
            self.worker.start()
            self.worker.print_pages.connect(self.printPages)

    def deleteOutput(self):
        if os.path.exists("output"):
            shutil.rmtree("output")
            os.makedirs("output/")

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

        self.TARGET_URL = self.ui.urlInput.text()
        if self.TARGET_URL.endswith("/"):
            self.TARGET_URL = self.TARGET_URL[:-1]

        pages = get_links(self.TARGET_URL, self.TARGET_URL)
        self.crawlFinished()

    def crawlFinished(self):
        print("Crawling finished!")
        self.end = time.time()
        self.crawlStatusUpdate(status=False)  # crawling is not active
        self.buttonUpdate(status="stop")    # Change button text
        self.inputUpdate(status="stop")     # Enable input
        self.infoUpdate(status="stop")    # Update info label
        self.printOutput()

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
        self.deleteOutput()     # Delete output folder

        self.threadCrawl()   # Start crawling
