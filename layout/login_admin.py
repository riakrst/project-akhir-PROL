# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login_admin.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(420, 321)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 401, 271))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_3.setContentsMargins(5, 5, 5, 5)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem)
        self.labelSelamatDatangAdmin = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.labelSelamatDatangAdmin.setFont(font)
        self.labelSelamatDatangAdmin.setAlignment(QtCore.Qt.AlignCenter)
        self.labelSelamatDatangAdmin.setObjectName("labelSelamatDatangAdmin")
        self.verticalLayout_3.addWidget(self.labelSelamatDatangAdmin)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem1)
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setContentsMargins(5, 5, 5, 5)
        self.formLayout.setObjectName("formLayout")
        self.labelUsername = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.labelUsername.setObjectName("labelUsername")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.labelUsername)
        self.lineEditUsername = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEditUsername.setText("")
        self.lineEditUsername.setClearButtonEnabled(False)
        self.lineEditUsername.setObjectName("lineEditUsername")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEditUsername)
        self.labelPassword = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.labelPassword.setObjectName("labelPassword")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.labelPassword)
        self.lineEditPassword = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEditPassword.setText("")
        self.lineEditPassword.setObjectName("lineEditPassword")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lineEditPassword)
        self.verticalLayout_3.addLayout(self.formLayout)
        self.pushButtonLogin = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButtonLogin.setObjectName("pushButtonLogin")
        self.verticalLayout_3.addWidget(self.pushButtonLogin)
        self.labelWarning = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.labelWarning.setObjectName("labelWarning")
        self.verticalLayout_3.addWidget(self.labelWarning)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 420, 18))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.labelSelamatDatangAdmin.setText(_translate("MainWindow", "Selamat Datang Admin"))
        self.labelUsername.setText(_translate("MainWindow", "Username"))
        self.labelPassword.setText(_translate("MainWindow", "Password"))
        self.pushButtonLogin.setText(_translate("MainWindow", "Masuk"))
        self.labelWarning.setText(_translate("MainWindow", "Masukkan username dan Password!"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())