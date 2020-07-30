# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainGUI.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(565, 358)
        MainWindow.setMinimumSize(QtCore.QSize(474, 310))
        MainWindow.setMaximumSize(QtCore.QSize(759, 504))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/img/img/icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalFrame = QtWidgets.QFrame(self.centralwidget)
        self.horizontalFrame.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.horizontalFrame.setObjectName("horizontalFrame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalFrame)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.horizontalFrame)
        self.label.setStyleSheet("min-width: 72.544px;\n"
"max-width: 72.544px;\n"
"min-height: 30px;\n"
"max-height: 30px;")
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(":/img/img/main_logo.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.VersionLabel = QtWidgets.QLabel(self.horizontalFrame)
        self.VersionLabel.setEnabled(True)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.VersionLabel.setFont(font)
        self.VersionLabel.setStyleSheet("color: rgb(255, 255, 255);")
        self.VersionLabel.setObjectName("VersionLabel")
        self.horizontalLayout.addWidget(self.VersionLabel, 0, QtCore.Qt.AlignBottom)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.frame = QtWidgets.QFrame(self.horizontalFrame)
        self.frame.setStyleSheet("min-height: 30px;\n"
"max-height: 30px;")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout_3.setContentsMargins(0, 0, 10, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.InputDataPushButton = QtWidgets.QPushButton(self.frame)
        self.InputDataPushButton.setStyleSheet("QPushButton#InputDataPushButton {\n"
"    min-width:25px;\n"
"    max-width:25px;\n"
"    min-height:25;\n"
"    max-height:25px;\n"
"\n"
"    color: rgb(255, 255, 255);\n"
"\n"
"    background:  rgb(0, 0, 0);\n"
"    border: 2px;\n"
"    border-style: solid;\n"
"    border-color: rgb(0, 0, 0);\n"
"    border-radius: 10.25;\n"
"}\n"
"\n"
"QPushButton#InputDataPushButton:hover {\n"
"    background-color: rgb(52, 52, 52);\n"
"    border-color:  rgb(52, 52, 52);\n"
"}\n"
"\n"
"QPushButton#InputDataPushButton:pressed {\n"
"    background-color: rgb(24, 24, 24);\n"
"    border-color:  rgb(24, 24, 24);\n"
"}")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/img/img/import.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.InputDataPushButton.setIcon(icon1)
        self.InputDataPushButton.setObjectName("InputDataPushButton")
        self.horizontalLayout_3.addWidget(self.InputDataPushButton)
        self.OutputDatasetPushButton = QtWidgets.QPushButton(self.frame)
        self.OutputDatasetPushButton.setWhatsThis("")
        self.OutputDatasetPushButton.setStyleSheet("QPushButton#OutputDatasetPushButton {\n"
"    min-width:25px;\n"
"    max-width:25px;\n"
"    min-height:25;\n"
"    max-height:25px;\n"
"\n"
"    color: rgb(255, 255, 255);\n"
"\n"
"    background:  rgb(0, 0, 0);\n"
"    border: 2px;\n"
"    border-style: solid;\n"
"    border-color: rgb(0, 0, 0);\n"
"    border-radius: 10.25;\n"
"}\n"
"\n"
"QPushButton#OutputDatasetPushButton:hover {\n"
"    background-color: rgb(52, 52, 52);\n"
"    border-color:  rgb(52, 52, 52);\n"
"}\n"
"\n"
"QPushButton#OutputDatasetPushButton:pressed {\n"
"    background-color: rgb(24, 24, 24);\n"
"    border-color:  rgb(24, 24, 24);\n"
"}")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/img/img/output.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.OutputDatasetPushButton.setIcon(icon2)
        self.OutputDatasetPushButton.setObjectName("OutputDatasetPushButton")
        self.horizontalLayout_3.addWidget(self.OutputDatasetPushButton)
        self.horizontalLayout.addWidget(self.frame)
        self.verticalLayout_2.addWidget(self.horizontalFrame)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_4.addWidget(self.label_2)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setWordWrap(True)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_4.addWidget(self.label_4)
        self.LabelLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.LabelLineEdit.setStyleSheet("QLineEdit {\n"
"    min-width:180px;\n"
"    min-height:30;\n"
"    max-height:30px;\n"
"    \n"
"    padding-left: 5px;\n"
"\n"
"    color: #495057;\n"
"\n"
"    background:  rgba(0,0,0,.08);\n"
"    border-bottom: 2px;\n"
"    border-style: solid;\n"
"    border-bottom-color: rgba(0,0,0,.3);\n"
"    border-top-left-radius: 3px;\n"
"    border-top-right-radius: 3px;\n"
"    border-bottom-right-radius: 0px;\n"
"    border-bottom-left-radius: 0px;\n"
"}\n"
"\n"
"QLineEdit::focus    {\n"
"    border-bottom-color:rgb(121, 137, 255);\n"
"}\n"
"\n"
"QLineEdit::disabled    {\n"
"    background:  rgba(0,0,0,.04);\n"
"    border-bottom-color: rgba(0,0,0,.15);\n"
"}")
        self.LabelLineEdit.setObjectName("LabelLineEdit")
        self.verticalLayout_4.addWidget(self.LabelLineEdit)
        self.horizontalLayout_2.addLayout(self.verticalLayout_4)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem3)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_3.addWidget(self.label_3)
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setWordWrap(True)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_3.addWidget(self.label_5)
        self.KWordLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.KWordLineEdit.setStyleSheet("QLineEdit {\n"
"    min-width:180px;\n"
"    min-height:30;\n"
"    max-height:30px;\n"
"    \n"
"    padding-left: 5px;\n"
"\n"
"    color: #495057;\n"
"\n"
"    background:  rgba(0,0,0,.08);\n"
"    border-bottom: 2px;\n"
"    border-style: solid;\n"
"    border-bottom-color: rgba(0,0,0,.3);\n"
"    border-top-left-radius: 3px;\n"
"    border-top-right-radius: 3px;\n"
"    border-bottom-right-radius: 0px;\n"
"    border-bottom-left-radius: 0px;\n"
"}\n"
"\n"
"QLineEdit::focus    {\n"
"    border-bottom-color:rgb(121, 137, 255);\n"
"}\n"
"\n"
"QLineEdit::disabled    {\n"
"    background:  rgba(0,0,0,.04);\n"
"    border-bottom-color: rgba(0,0,0,.15);\n"
"}")
        self.KWordLineEdit.setObjectName("KWordLineEdit")
        self.verticalLayout_3.addWidget(self.KWordLineEdit)
        self.horizontalLayout_2.addLayout(self.verticalLayout_3)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem4)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem5)
        self.SubmitPushButton = QtWidgets.QPushButton(self.centralwidget)
        self.SubmitPushButton.setStyleSheet("QPushButton#SubmitPushButton {\n"
"    min-width:80px;\n"
"    max-width:80px;\n"
"    min-height:30;\n"
"    max-height:30px;\n"
"\n"
"    color: rgb(255, 255, 255);\n"
"\n"
"    background:  rgb(0, 0, 0);\n"
"    border: 2px;\n"
"    border-style: solid;\n"
"    border-color: rgb(0, 0, 0);\n"
"    border-radius: 15;\n"
"\n"
"    margin-bottom: 10px;\n"
"}\n"
"\n"
"QPushButton#SubmitPushButton:hover {\n"
"    background-color: rgb(52, 52, 52);\n"
"    border-color:  rgb(52, 52, 52);\n"
"}\n"
"\n"
"QPushButton#SubmitPushButton:pressed {\n"
"    background-color: rgb(24, 24, 24);\n"
"    border-color:  rgb(24, 24, 24);\n"
"}")
        self.SubmitPushButton.setObjectName("SubmitPushButton")
        self.verticalLayout_2.addWidget(self.SubmitPushButton, 0, QtCore.Qt.AlignHCenter)
        self.ErrorLabel = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.ErrorLabel.setFont(font)
        self.ErrorLabel.setStyleSheet("color: rgb(255, 0, 0);")
        self.ErrorLabel.setObjectName("ErrorLabel")
        self.verticalLayout_2.addWidget(self.ErrorLabel, 0, QtCore.Qt.AlignHCenter)
        spacerItem6 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem6)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 565, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Zero"))
        self.VersionLabel.setText(_translate("MainWindow", "v2.0.1"))
        self.InputDataPushButton.setStatusTip(_translate("MainWindow", "Load corpus (Ctrl+I)"))
        self.InputDataPushButton.setShortcut(_translate("MainWindow", "Ctrl+I"))
        self.OutputDatasetPushButton.setStatusTip(_translate("MainWindow", "Define output file (Ctrl+O)"))
        self.OutputDatasetPushButton.setShortcut(_translate("MainWindow", "Ctrl+O"))
        self.label_2.setText(_translate("MainWindow", "*Lable"))
        self.label_4.setText(_translate("MainWindow", "Enter a label that will represent the target feature for keyword sentences."))
        self.LabelLineEdit.setPlaceholderText(_translate("MainWindow", "Example: Love, Anger ..."))
        self.label_3.setText(_translate("MainWindow", "*Keyword/s"))
        self.label_5.setText(_translate("MainWindow", "Enter keyword/s for targeted sentences."))
        self.KWordLineEdit.setPlaceholderText(_translate("MainWindow", "Example: love, sweet, like ..."))
        self.SubmitPushButton.setStatusTip(_translate("MainWindow", "Process (Enter)"))
        self.SubmitPushButton.setText(_translate("MainWindow", "Process"))
        self.SubmitPushButton.setShortcut(_translate("MainWindow", "Return"))
        self.ErrorLabel.setText(_translate("MainWindow", "Error line"))
import src_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
