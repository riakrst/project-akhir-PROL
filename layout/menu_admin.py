# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'menu_admin.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(315, 245)
        self.verticalLayoutWidget = QtWidgets.QWidget(Form)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 291, 231))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(5, 5, 5, 5)
        self.verticalLayout.setObjectName("verticalLayout")
        self.labelNama = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.labelNama.setFont(font)
        self.labelNama.setAlignment(QtCore.Qt.AlignCenter)
        self.labelNama.setObjectName("labelNama")
        self.verticalLayout.addWidget(self.labelNama)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.pushButtonUpdateStok = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButtonUpdateStok.setObjectName("pushButtonUpdateStok")
        self.verticalLayout.addWidget(self.pushButtonUpdateStok)
        self.pushButtonRiwayatPembelian = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButtonRiwayatPembelian.setObjectName("pushButtonRiwayatPembelian")
        self.verticalLayout.addWidget(self.pushButtonRiwayatPembelian)
        self.pushButtonRekapPenjualan = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButtonRekapPenjualan.setObjectName("pushButtonRekapPenjualan")
        self.verticalLayout.addWidget(self.pushButtonRekapPenjualan)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.pushButtonKembali = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButtonKembali.setObjectName("pushButtonKembali")
        self.verticalLayout.addWidget(self.pushButtonKembali)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.labelNama.setText(_translate("Form", "Menu Admin"))
        self.pushButtonUpdateStok.setText(_translate("Form", "Update Stok"))
        self.pushButtonRiwayatPembelian.setText(_translate("Form", "Riwayat Pembelian"))
        self.pushButtonRekapPenjualan.setText(_translate("Form", "Rekap Penjualan"))
        self.pushButtonKembali.setText(_translate("Form", "Kembali"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())