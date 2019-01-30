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
        self.yzm_label = SzLabel(self.widget)
        self.yzm_label.setMinimumSize(QtCore.QSize(293, 190))
        self.yzm_label.setMaximumSize(QtCore.QSize(293, 190))
        self.yzm_label.setStyleSheet("background-color: rgb(85, 255, 255);")
        self.yzm_label.setTextFormat(QtCore.Qt.PlainText)
        self.yzm_label.setObjectName("yzm_label")
        self.gridLayout.addWidget(self.yzm_label, 2, 1, 2, 1)
        self.auto_dm_btn = QtWidgets.QPushButton(self.widget)
        self.auto_dm_btn.setMinimumSize(QtCore.QSize(50, 50))
        self.auto_dm_btn.setMaximumSize(QtCore.QSize(50, 50))
        self.auto_dm_btn.setObjectName("auto_dm_btn")
        self.gridLayout.addWidget(self.auto_dm_btn, 3, 0, 1, 1)
        self.login_btn = QtWidgets.QPushButton(self.widget)
        self.login_btn.setEnabled(False)
        self.login_btn.setMinimumSize(QtCore.QSize(0, 50))
        self.login_btn.setObjectName("login_btn")
        self.gridLayout.addWidget(self.login_btn, 4, 0, 1, 2)
        self.horizontalLayout.addWidget(self.widget)

        self.retranslateUi(Form)
        self.pushButton.clicked.connect(Form.refresh_yzm)
        self.auto_dm_btn.clicked.connect(Form.auto_dm)
        self.login_btn.clicked.connect(Form.check_login)
        self.account_le.textChanged['QString'].connect(Form.auto_enable_login_btn)
        self.pwd_le.textChanged['QString'].connect(Form.auto_enable_login_btn)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "12306抢票"))
        self.account_le.setPlaceholderText(_translate("Form", "请输入你的12306账号"))
        self.pwd_le.setPlaceholderText(_translate("Form", "请输入密码"))
        self.pushButton.setText(_translate("Form", "刷新"))
        self.yzm_label.setText(_translate("Form", "           正在下载验证码..."))
        self.auto_dm_btn.setText(_translate("Form", "识别"))
        self.login_btn.setText(_translate("Form", "登录"))

from Sz_Label import SzLabel
