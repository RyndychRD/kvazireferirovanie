# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'window.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_extractiveSummarization(object):
    def setupUi(self, extractiveSummarization):
        extractiveSummarization.setObjectName("extractiveSummarization")
        extractiveSummarization.resize(730, 624)
        self.centralwidget = QtWidgets.QWidget(extractiveSummarization)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.textInput = QtWidgets.QTextEdit(self.centralwidget)
        self.textInput.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.textInput.setPlaceholderText("")
        self.textInput.setObjectName("textInput")
        self.gridLayout.addWidget(self.textInput, 0, 0, 1, 2)
        self.doRefer = QtWidgets.QPushButton(self.centralwidget)
        self.doRefer.setObjectName("doRefer")
        self.gridLayout.addWidget(self.doRefer, 1, 1, 1, 1)
        self.numberBox = QtWidgets.QSpinBox(self.centralwidget)
        self.numberBox.setObjectName("numberBox")
        self.gridLayout.addWidget(self.numberBox, 1, 0, 1, 1)
        self.textOutput = QtWidgets.QTextEdit(self.centralwidget)
        self.textOutput.setReadOnly(True)
        self.textOutput.setObjectName("textOutput")
        self.gridLayout.addWidget(self.textOutput, 2, 0, 1, 2)
        extractiveSummarization.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(extractiveSummarization)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 730, 22))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        extractiveSummarization.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(extractiveSummarization)
        self.statusbar.setObjectName("statusbar")
        extractiveSummarization.setStatusBar(self.statusbar)
        self.actionOpen = QtWidgets.QAction(extractiveSummarization)
        self.actionOpen.setObjectName("actionOpen")
        self.actionSave = QtWidgets.QAction(extractiveSummarization)
        self.actionSave.setObjectName("actionSave")
        self.actionExit = QtWidgets.QAction(extractiveSummarization)
        self.actionExit.setObjectName("actionExit")
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExit)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(extractiveSummarization)
        QtCore.QMetaObject.connectSlotsByName(extractiveSummarization)

    def retranslateUi(self, extractiveSummarization):
        _translate = QtCore.QCoreApplication.translate
        extractiveSummarization.setWindowTitle(_translate("extractiveSummarization", "MainWindow"))
        self.doRefer.setText(_translate("extractiveSummarization", "Реферировать"))
        self.menuFile.setTitle(_translate("extractiveSummarization", "&File"))
        self.actionOpen.setText(_translate("extractiveSummarization", "&Open"))
        self.actionSave.setText(_translate("extractiveSummarization", "&Save"))
        self.actionExit.setText(_translate("extractiveSummarization", "&Exit"))

