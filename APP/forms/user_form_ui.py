# Form implementation generated from reading ui file 'APP\forms\forms_ui\user_form.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_UserWindow(object):
    def setupUi(self, UserWindow):
        UserWindow.setObjectName("UserWindow")
        UserWindow.resize(277, 190)
        UserWindow.setStyleSheet("background-color: rgb(235, 231, 255);")
        self.centralwidget = QtWidgets.QWidget(parent=UserWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_6 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_6.addWidget(self.label_6)
        self.name_input = QtWidgets.QLineEdit(parent=self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.name_input.sizePolicy().hasHeightForWidth())
        self.name_input.setSizePolicy(sizePolicy)
        self.name_input.setMinimumSize(QtCore.QSize(0, 0))
        self.name_input.setMouseTracking(True)
        self.name_input.setTabletTracking(False)
        self.name_input.setAcceptDrops(True)
        self.name_input.setAutoFillBackground(False)
        self.name_input.setStyleSheet("background-color: rgb(235, 235, 245);\n"
"border-radius: 5px;\n"
"border: 1px solid dlack")
        self.name_input.setInputMethodHints(QtCore.Qt.InputMethodHint.ImhNone)
        self.name_input.setInputMask("")
        self.name_input.setText("")
        self.name_input.setEchoMode(QtWidgets.QLineEdit.EchoMode.Normal)
        self.name_input.setDragEnabled(False)
        self.name_input.setReadOnly(False)
        self.name_input.setPlaceholderText("")
        self.name_input.setClearButtonEnabled(False)
        self.name_input.setObjectName("name_input")
        self.horizontalLayout_6.addWidget(self.name_input)
        self.verticalLayout.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_5 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_5.addWidget(self.label_5)
        self.addres_input = QtWidgets.QLineEdit(parent=self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.addres_input.sizePolicy().hasHeightForWidth())
        self.addres_input.setSizePolicy(sizePolicy)
        self.addres_input.setMinimumSize(QtCore.QSize(0, 0))
        self.addres_input.setMouseTracking(True)
        self.addres_input.setTabletTracking(False)
        self.addres_input.setAcceptDrops(True)
        self.addres_input.setAutoFillBackground(False)
        self.addres_input.setStyleSheet("background-color: rgb(235, 235, 245);\n"
"border-radius: 5px;\n"
"border: 1px solid dlack")
        self.addres_input.setInputMethodHints(QtCore.Qt.InputMethodHint.ImhNone)
        self.addres_input.setInputMask("")
        self.addres_input.setText("")
        self.addres_input.setEchoMode(QtWidgets.QLineEdit.EchoMode.Normal)
        self.addres_input.setDragEnabled(False)
        self.addres_input.setReadOnly(False)
        self.addres_input.setPlaceholderText("")
        self.addres_input.setClearButtonEnabled(False)
        self.addres_input.setObjectName("addres_input")
        self.horizontalLayout_5.addWidget(self.addres_input)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.login_input = QtWidgets.QLineEdit(parent=self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.login_input.sizePolicy().hasHeightForWidth())
        self.login_input.setSizePolicy(sizePolicy)
        self.login_input.setMinimumSize(QtCore.QSize(0, 0))
        self.login_input.setMouseTracking(True)
        self.login_input.setTabletTracking(False)
        self.login_input.setAcceptDrops(True)
        self.login_input.setAutoFillBackground(False)
        self.login_input.setStyleSheet("background-color: rgb(235, 235, 245);\n"
"border-radius: 5px;\n"
"border: 1px solid dlack")
        self.login_input.setInputMethodHints(QtCore.Qt.InputMethodHint.ImhNone)
        self.login_input.setInputMask("")
        self.login_input.setText("")
        self.login_input.setEchoMode(QtWidgets.QLineEdit.EchoMode.Normal)
        self.login_input.setDragEnabled(False)
        self.login_input.setReadOnly(False)
        self.login_input.setPlaceholderText("")
        self.login_input.setClearButtonEnabled(False)
        self.login_input.setObjectName("login_input")
        self.horizontalLayout.addWidget(self.login_input)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.password_input = QtWidgets.QLineEdit(parent=self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.password_input.sizePolicy().hasHeightForWidth())
        self.password_input.setSizePolicy(sizePolicy)
        self.password_input.setMinimumSize(QtCore.QSize(0, 0))
        self.password_input.setMouseTracking(True)
        self.password_input.setTabletTracking(False)
        self.password_input.setAcceptDrops(True)
        self.password_input.setAutoFillBackground(False)
        self.password_input.setStyleSheet("background-color: rgb(235, 235, 245);\n"
"border-radius: 5px;\n"
"border: 1px solid dlack")
        self.password_input.setInputMethodHints(QtCore.Qt.InputMethodHint.ImhNone)
        self.password_input.setInputMask("")
        self.password_input.setText("")
        self.password_input.setEchoMode(QtWidgets.QLineEdit.EchoMode.Normal)
        self.password_input.setDragEnabled(False)
        self.password_input.setReadOnly(False)
        self.password_input.setPlaceholderText("")
        self.password_input.setClearButtonEnabled(False)
        self.password_input.setObjectName("password_input")
        self.horizontalLayout_2.addWidget(self.password_input)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.user_choise_layout = QtWidgets.QHBoxLayout()
        self.user_choise_layout.setObjectName("user_choise_layout")
        self.label_10 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_10.setMinimumSize(QtCore.QSize(30, 0))
        self.label_10.setStyleSheet("")
        self.label_10.setObjectName("label_10")
        self.user_choise_layout.addWidget(self.label_10)
        self.postsBox = QtWidgets.QComboBox(parent=self.centralwidget)
        self.postsBox.setMinimumSize(QtCore.QSize(200, 0))
        self.postsBox.setStyleSheet("background-color: rgb(235, 235, 245);\n"
"border-radius: 5px;\n"
"border: 1px solid dlack")
        self.postsBox.setObjectName("postsBox")
        self.postsBox.addItem("")
        self.postsBox.setItemText(0, "")
        self.user_choise_layout.addWidget(self.postsBox)
        self.verticalLayout.addLayout(self.user_choise_layout)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem)
        self.create_btn = QtWidgets.QPushButton(parent=self.centralwidget)
        self.create_btn.setMinimumSize(QtCore.QSize(100, 0))
        self.create_btn.setStyleSheet("QPushButton {\n"
"    background-color: rgb(185, 196, 255);\n"
"    padding: 5 10 5 10;\n"
"    border:1px solid black;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(155, 155, 224);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(140, 140, 207);\n"
"}")
        self.create_btn.setText("")
        self.create_btn.setObjectName("create_btn")
        self.horizontalLayout_7.addWidget(self.create_btn)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem1)
        self.clousing_btn = QtWidgets.QPushButton(parent=self.centralwidget)
        self.clousing_btn.setMinimumSize(QtCore.QSize(100, 0))
        self.clousing_btn.setStyleSheet("QPushButton {\n"
"    background-color: rgb(217, 74, 74);\n"
"    padding: 5 10 5 10;\n"
"    border:1px solid black;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(222, 87, 87);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(217, 139, 139);\n"
"}")
        self.clousing_btn.setObjectName("clousing_btn")
        self.horizontalLayout_7.addWidget(self.clousing_btn)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem2)
        self.verticalLayout.addLayout(self.horizontalLayout_7)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        UserWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(UserWindow)
        QtCore.QMetaObject.connectSlotsByName(UserWindow)

    def retranslateUi(self, UserWindow):
        _translate = QtCore.QCoreApplication.translate
        UserWindow.setWindowTitle(_translate("UserWindow", "MainWindow"))
        self.label_6.setText(_translate("UserWindow", "Имя:"))
        self.label_5.setText(_translate("UserWindow", "Адрес:"))
        self.label.setText(_translate("UserWindow", "Логин:"))
        self.label_2.setText(_translate("UserWindow", "Пароль:"))
        self.label_10.setText(_translate("UserWindow", "Роль:"))
        self.clousing_btn.setText(_translate("UserWindow", "Отмена"))
