# This Python file uses the following encoding: utf-8
import sys

from PySide6.QtWidgets import QApplication, QMainWindow
import time

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
from ui_form import Ui_MainWindow


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.crawlButton.clicked.connect(self.crawl)

    def updateButton(self):
        self.ui.crawlButton.setText("Stop Crawling!")
        self.ui.crawlButton.setDefault(False)

    def updateInput(self):
        self.ui.crawlInput.setReadOnly(True)
        oldStyleSheet = self.ui.crawlInput.styleSheet()
        self.ui.crawlInput.setStyleSheet(oldStyleSheet + "\nQLineEdit {\n"
                                         "	border-color: gray;\n	color: gray;\n}")

    def updateInfo(self):
        hours, rem = divmod(self.end - self.start, 3600)
        minutes, seconds = divmod(rem, 60)
        self.ui.infoLabel.setText(
            f'Crawling time: {int(hours):0>2}h {int(minutes):0>2}m {seconds:05.2f}s')

    def defaultButton(self):
        self.ui.crawlButton.setText("Start Crawl")
        self.ui.crawlButton.setDefault(True)

    def defaultInput(self):
        self.ui.crawlInput.setReadOnly(False)
        oldStyleSheet = self.ui.crawlInput.styleSheet()
        self.ui.crawlInput.setStyleSheet(oldStyleSheet + "\nQLineEdit {\n"
                                         "	border-color: lightgray;\n	color: lightgray;\n}")

    def checkButton(self):
        if self.ui.crawlButton.text() == "Stop Crawling!":
            self.defaultButton()
            self.defaultInput()
            return False
        return True

    def checkInput(self):
        self.ui.outputTextBrowser.clear()
        if not self.ui.crawlInput.text():
            self.ui.crawlInput.setFocus()
            self.ui.outputTextBrowser.append(
                "Please enter a URL to crawl like <b><i>https://uludag.edu.tr</i></b>")
            return False
        return True

    def crawl(self):
        if not self.checkButton():  # If button is Stop Crawling!
            self.end = time.time()
            self.updateInfo()
            return
        if not self.checkInput():   # If input is empty,
            return

        self.start = time.time()
        self.updateButton()
        self.updateInput()
        self.ui.infoLabel.setText("Crawling... Please wait!")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MainWindow()
    widget.show()
    sys.exit(app.exec())
