# Form implementation generated from reading ui file '/Users/pinxun/Documents/MindX/PTA/PTA07/FINAL PROJECT/TriCuong/python-app/ui/login.ui'
#
# Created by: PyQt6 UI code generator 6.8.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setStyleSheet("background-color:rgb(217, 217, 217)")
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Logopicture = QtWidgets.QLabel(parent=self.centralwidget)
        self.Logopicture.setGeometry(QtCore.QRect(40, 180, 311, 231))
        self.Logopicture.setText("")
        self.Logopicture.setPixmap(QtGui.QPixmap("/Users/pinxun/Documents/MindX/PTA/PTA07/FINAL PROJECT/TriCuong/python-app/ui/../img/302065e0-36bf-477b-86d3-f71749fd23b1.webp"))
        self.Logopicture.setScaledContents(True)
        self.Logopicture.setObjectName("Logopicture")
        self.frame = QtWidgets.QFrame(parent=self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(430, -30, 401, 681))
        font = QtGui.QFont()
        font.setKerning(True)
        self.frame.setFont(font)
        self.frame.setStyleSheet("background-color:rgb(255, 255, 255);\n"
"")
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.logologin = QtWidgets.QLabel(parent=self.frame)
        self.logologin.setGeometry(QtCore.QRect(110, 150, 171, 91))
        font = QtGui.QFont()
        font.setFamily("Algerian")
        font.setPointSize(36)
        self.logologin.setFont(font)
        self.logologin.setStyleSheet("color: black;")
        self.logologin.setObjectName("logologin")
        self.loginemail = QtWidgets.QLineEdit(parent=self.frame)
        self.loginemail.setGeometry(QtCore.QRect(60, 270, 261, 41))
        font = QtGui.QFont()
        font.setFamily("SimSun")
        font.setPointSize(-1)
        self.loginemail.setFont(font)
        self.loginemail.setStyleSheet("border: none;\n"
"    border-bottom: 1px solid #000; /* Black underline */\n"
"    font-size: 14px;\n"
"    padding: 5px;\n"
"color: black;")
        self.loginemail.setText("")
        self.loginemail.setFrame(False)
        self.loginemail.setEchoMode(QtWidgets.QLineEdit.EchoMode.Normal)
        self.loginemail.setCursorPosition(0)
        self.loginemail.setDragEnabled(False)
        self.loginemail.setReadOnly(False)
        self.loginemail.setClearButtonEnabled(False)
        self.loginemail.setObjectName("loginemail")
        self.Buttonlogin = QtWidgets.QPushButton(parent=self.frame)
        self.Buttonlogin.setGeometry(QtCore.QRect(60, 430, 261, 51))
        self.Buttonlogin.setStyleSheet("background-color: #000; /* Black background */\n"
"    color: #fff; /* White text */\n"
"    font-size: 14px; /* Adjust text size */\n"
"    border: none; /* Remove borders */\n"
"    border-radius: 20px; /* Rounded corners */\n"
"    padding: 10px 20px; /* Add padding for a larger button */\n"
"    text-align: center; /* Center the text */")
        self.Buttonlogin.setObjectName("Buttonlogin")
        self.Loddontyou = QtWidgets.QLabel(parent=self.frame)
        self.Loddontyou.setGeometry(QtCore.QRect(60, 550, 201, 20))
        self.Loddontyou.setStyleSheet("color: black;")
        self.Loddontyou.setObjectName("Loddontyou")
        self.Buttonsignup = QtWidgets.QPushButton(parent=self.frame)
        self.Buttonsignup.setGeometry(QtCore.QRect(230, 550, 93, 21))
        self.Buttonsignup.setStyleSheet("background: transparent; /* No background */\n"
"    border: none; /* Remove border */\n"
"    color: #666; /* Light gray text color */\n"
"    font-size: 14px; /* Adjust font size as needed */\n"
"    text-align: left; /* Align text to the left */")
        self.Buttonsignup.setObjectName("Buttonsignup")
        self.loginpassword = QtWidgets.QLineEdit(parent=self.frame)
        self.loginpassword.setGeometry(QtCore.QRect(60, 350, 261, 41))
        font = QtGui.QFont()
        font.setFamily("SimSun")
        font.setPointSize(-1)
        self.loginpassword.setFont(font)
        self.loginpassword.setStyleSheet("border: none;\n"
"    border-bottom: 1px solid #000; /* Black underline */\n"
"    font-size: 14px;\n"
"    padding: 5px;\n"
"color: black;")
        self.loginpassword.setText("")
        self.loginpassword.setFrame(False)
        self.loginpassword.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        self.loginpassword.setCursorPosition(0)
        self.loginpassword.setDragEnabled(False)
        self.loginpassword.setReadOnly(False)
        self.loginpassword.setClearButtonEnabled(False)
        self.loginpassword.setObjectName("loginpassword")
        self.Buttoneye_2 = QtWidgets.QPushButton(parent=self.frame)
        self.Buttoneye_2.setGeometry(QtCore.QRect(300, 370, 21, 21))
        self.Buttoneye_2.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("/Users/pinxun/Documents/MindX/PTA/PTA07/FINAL PROJECT/TriCuong/python-app/ui/../img/hidden.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.Buttoneye_2.setIcon(icon)
        self.Buttoneye_2.setObjectName("Buttoneye_2")
        self.frame.raise_()
        self.Logopicture.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 24))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.logologin.setText(_translate("MainWindow", "Login"))
        self.loginemail.setPlaceholderText(_translate("MainWindow", "Email"))
        self.Buttonlogin.setText(_translate("MainWindow", "Login"))
        self.Loddontyou.setText(_translate("MainWindow", "Don\'t you have an account"))
        self.Buttonsignup.setText(_translate("MainWindow", "Sign up?"))
        self.loginpassword.setPlaceholderText(_translate("MainWindow", "Password"))