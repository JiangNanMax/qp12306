# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(600, 500)
        Form.setMinimumSize(QtCore.QSize(600, 500))
        Form.setMaximumSize(QtCore.QSize(600, 500))
        self.horizontalLayout = QtWidgets.QHBoxLayout(Form)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setMinimumSize(QtCore.QSize(450, 400))
        self.widget.setMaximumSize(QtCore.QSize(450, 400))
        self.widget.setStyleSheet("")
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setObjectName("gridLayout")
        self.account_le = QtWidgets.QLineEdit(self.widget)
        self.account_le.setMinimumSize(QtCore.QSize(0, 45))
        self.account_le.setClearButtonEnabled(True)
        self.account_le.setObjectName("account_le")
        self.gridLayout.addWidget(self.account_le, 0, 0, 1, 2)
        self.pwd_le = QtWidgets.QLineEdit(self.widget)
        self.pwd_le.setMinimumSize(QtCore.QSize(0, 45))
        self.pwd_le.setEchoMode(QtWidgets.QLineEdit.Password)
        self.pwd_le.setClearButtonEnabled(True)
        self.pwd_le.setObjectName("pwd_le")
        self.gridLayout.addWidget(self.pwd_le, 1, 0, 1, 2)
        self.pushButton = QtWidgets.QPushButton(self.widget)
        self.pushButton.setMinimumSize(QtCore.QSize(50, 50))
        self.pushButton.setMaximumSize(QtCore.QSize(50, 50))
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 2, 0, 1, 1)
        self.yzm_label = QtWidgets.QLabel(self.widget)
        self.yzm_label.setMinimumSize(QtCore.QSize(293, 190))
        self.yzm_label.setMaximumSize(QtCore.QSize(293, 190))
        self.yzm_label.setStyleSheet("background-color: rgb(170, 255, 127);")
        self.yzm_label.setObjectName("yzm_label")
        self.gridLayout.addWidget(self.yzm_label, 2, 1, 2, 1)
        self.pushButton_2 = QtWidgets.QPushButton(self.widget)
        self.pushButton_2.setMinimumSize(QtCore.QSize(50, 50))
        self.pushButton_2.setMaximumSize(QtCore.QSize(50, 50))
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 3, 0, 1, 1)
        self.pushButton_3 = QtWidgets.QPushButton(self.widget)
        self.pushButton_3.setMinimumSize(QtCore.QSize(0, 50))
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout.addWidget(self.pushButton_3, 4, 0, 1, 2)
        self.horizontalLayout.addWidget(self.widget)

        self.retranslateUi(Form)
        self.pushButton.clicked.connect(Form.refresh_yzm)
        self.pushButton_2.clicked.connect(Form.auto_dm)
        self.pushButton_3.clicked.connect(Form.check_login)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "12306抢票"))
        self.account_le.setPlaceholderText(_translate("Form", "请输入你的12306账号"))
        self.pwd_le.setPlaceholderText(_translate("Form", "请输入密码"))
        self.pushButton.setText(_translate("Form", "刷新"))
        self.yzm_label.setText(_translate("Form", "验证码"))
        self.pushButton_2.setText(_translate("Form", "识别"))
        self.pushButton_3.setText(_translate("Form", "登录"))

