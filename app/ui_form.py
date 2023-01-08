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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QLineEdit,
    QMainWindow, QMenu, QMenuBar, QPushButton,
    QSizePolicy, QTextBrowser, QTextEdit, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setMinimumSize(QSize(800, 600))
        MainWindow.setMaximumSize(QSize(800, 600))
        self.actionSourceCodes = QAction(MainWindow)
        self.actionSourceCodes.setObjectName(u"actionSourceCodes")
        self.actionLicense = QAction(MainWindow)
        self.actionLicense.setObjectName(u"actionLicense")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayoutWidget = QWidget(self.centralwidget)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(10, 0, 781, 561))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(10, 10, 10, 0)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.urlLabel = QLabel(self.verticalLayoutWidget)
        self.urlLabel.setObjectName(u"urlLabel")
        self.urlLabel.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.urlLabel)

        self.urlInput = QLineEdit(self.verticalLayoutWidget)
        self.urlInput.setObjectName(u"urlInput")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.urlInput.sizePolicy().hasHeightForWidth())
        self.urlInput.setSizePolicy(sizePolicy)
        self.urlInput.setStyleSheet(u"QLineEdit {\n"
"	padding-left: 5px;\n"
"	padding-right: 5px;\n"
"	border-style: solid;\n"
"	border-width: 1px;\n"
"	border-radius: 8px;\n"
"	border-color: lightgray;\n"
"}")
        self.urlInput.setMaxLength(512)

        self.horizontalLayout.addWidget(self.urlInput)

        self.actionButton = QPushButton(self.verticalLayoutWidget)
        self.actionButton.setObjectName(u"actionButton")

        self.horizontalLayout.addWidget(self.actionButton)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.outputTextBrowser = QTextBrowser(self.verticalLayoutWidget)
        self.outputTextBrowser.setObjectName(u"outputTextBrowser")
        self.outputTextBrowser.setStyleSheet(u"QTextBrowser {\n"
"	border-style: solid;\n"
"	border-width: 1px;\n"
"	border-color: lightgray;\n"
"}")
        self.outputTextBrowser.setAutoFormatting(QTextEdit.AutoAll)
        self.outputTextBrowser.setOpenExternalLinks(True)

        self.verticalLayout.addWidget(self.outputTextBrowser)

        self.infoLabel = QLabel(self.verticalLayoutWidget)
        self.infoLabel.setObjectName(u"infoLabel")

        self.verticalLayout.addWidget(self.infoLabel)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 24))
        self.menuHelp = QMenu(self.menubar)
        self.menuHelp.setObjectName(u"menuHelp")
        MainWindow.setMenuBar(self.menubar)
        QWidget.setTabOrder(self.urlInput, self.actionButton)
        QWidget.setTabOrder(self.actionButton, self.outputTextBrowser)

        self.menubar.addAction(self.menuHelp.menuAction())
        self.menuHelp.addAction(self.actionSourceCodes)
        self.menuHelp.addAction(self.actionLicense)

        self.retranslateUi(MainWindow)

        self.actionButton.setDefault(True)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"webcrawler3003", None))
        self.actionSourceCodes.setText(QCoreApplication.translate("MainWindow", u"Source Codes", None))
        self.actionLicense.setText(QCoreApplication.translate("MainWindow", u"License", None))
        self.urlLabel.setText(QCoreApplication.translate("MainWindow", u"Website Address \n"
"to Crawl", None))
        self.urlInput.setPlaceholderText(QCoreApplication.translate("MainWindow", u"https://uludag.edu.tr", None))
        self.actionButton.setText(QCoreApplication.translate("MainWindow", u"Start Crawl", None))
        self.infoLabel.setText(QCoreApplication.translate("MainWindow", u"Please enter the website address to be crawled and click the \"Start Crawl\" button.", None))
        self.menuHelp.setTitle(QCoreApplication.translate("MainWindow", u"Help", None))
    # retranslateUi

