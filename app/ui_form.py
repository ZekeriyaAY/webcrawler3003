# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.4.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QLineEdit,
    QMainWindow, QMenu, QMenuBar, QPushButton,
    QSizePolicy, QTextBrowser, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setMinimumSize(QSize(800, 600))
        self.actionSource_Codes = QAction(MainWindow)
        self.actionSource_Codes.setObjectName(u"actionSource_Codes")
        self.actionLicense = QAction(MainWindow)
        self.actionLicense.setObjectName(u"actionLicense")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.layoutWidget = QWidget(self.centralwidget)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(10, 7, 781, 561))
        self.gridLayout = QGridLayout(self.layoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(10, 10, 10, 0)
        self.outputTextBrowser = QTextBrowser(self.layoutWidget)
        self.outputTextBrowser.setObjectName(u"outputTextBrowser")
        self.outputTextBrowser.setStyleSheet(u"QTextBrowser {\n"
"	border-style: solid;\n"
"	border-width: 1px;\n"
"	border-color: lightgray;\n"
"}")
        self.outputTextBrowser.setOpenExternalLinks(True)

        self.gridLayout.addWidget(self.outputTextBrowser, 3, 0, 1, 3)

        self.crawlInput = QLineEdit(self.layoutWidget)
        self.crawlInput.setObjectName(u"crawlInput")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.crawlInput.sizePolicy().hasHeightForWidth())
        self.crawlInput.setSizePolicy(sizePolicy)
        self.crawlInput.setStyleSheet(u"QLineEdit {\n"
"	padding-left: 5px;\n"
"	padding-right: 5px;\n"
"	border-style: solid;\n"
"	border-width: 1px;\n"
"	border-radius: 8px;\n"
"	border-color: lightgray;\n"
"}")
        self.crawlInput.setMaxLength(512)

        self.gridLayout.addWidget(self.crawlInput, 2, 1, 1, 1)

        self.crawlButton = QPushButton(self.layoutWidget)
        self.crawlButton.setObjectName(u"crawlButton")

        self.gridLayout.addWidget(self.crawlButton, 2, 2, 1, 1)

        self.urlLabel = QLabel(self.layoutWidget)
        self.urlLabel.setObjectName(u"urlLabel")
        self.urlLabel.setAlignment(Qt.AlignCenter)
        self.urlLabel.setWordWrap(True)

        self.gridLayout.addWidget(self.urlLabel, 2, 0, 1, 1)

        self.infoLabel = QLabel(self.layoutWidget)
        self.infoLabel.setObjectName(u"infoLabel")

        self.gridLayout.addWidget(self.infoLabel, 4, 0, 1, 2)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 24))
        self.menuHelp = QMenu(self.menubar)
        self.menuHelp.setObjectName(u"menuHelp")
        MainWindow.setMenuBar(self.menubar)
        QWidget.setTabOrder(self.crawlInput, self.outputTextBrowser)

        self.menubar.addAction(self.menuHelp.menuAction())
        self.menuHelp.addAction(self.actionSource_Codes)
        self.menuHelp.addAction(self.actionLicense)

        self.retranslateUi(MainWindow)

        self.crawlButton.setDefault(True)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"webcrawler3003", None))
        self.actionSource_Codes.setText(QCoreApplication.translate("MainWindow", u"Source Codes", None))
        self.actionLicense.setText(QCoreApplication.translate("MainWindow", u"License", None))
        self.crawlInput.setPlaceholderText(QCoreApplication.translate("MainWindow", u"https://uludag.edu.tr/bm", None))
        self.crawlButton.setText(QCoreApplication.translate("MainWindow", u"Start Crawl", None))
        self.urlLabel.setText(QCoreApplication.translate("MainWindow", u"Website Address \n"
"to Crawl", None))
        self.infoLabel.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Please enter the website address to be crawled and click the &quot;Start Crawl&quot; button.</p></body></html>", None))
        self.menuHelp.setTitle(QCoreApplication.translate("MainWindow", u"Help", None))
    # retranslateUi

