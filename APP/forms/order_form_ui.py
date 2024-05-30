# Form implementation generated from reading ui file 'APP\forms\forms_ui\order_form.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_CreateOrderWindow(object):
    def setupUi(self, CreateOrderWindow):
        CreateOrderWindow.setObjectName("CreateOrderWindow")
        CreateOrderWindow.resize(396, 269)
        CreateOrderWindow.setStyleSheet("background-color: rgb(235, 231, 255);")
        self.centralwidget = QtWidgets.QWidget(parent=CreateOrderWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setStyleSheet("background-color: rgb(238, 240, 255);")
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.name_label = QtWidgets.QLabel(parent=self.centralwidget)
        self.name_label.setMinimumSize(QtCore.QSize(150, 0))
        self.name_label.setStyleSheet("background-color: rgb(238, 240, 255);")
        self.name_label.setText("")
        self.name_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.name_label.setObjectName("name_label")
        self.horizontalLayout_2.addWidget(self.name_label)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_6 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_6.setStyleSheet("background-color: rgb(238, 240, 255);")
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_4.addWidget(self.label_6)
        self.categories_label = QtWidgets.QLabel(parent=self.centralwidget)
        self.categories_label.setMinimumSize(QtCore.QSize(150, 0))
        self.categories_label.setStyleSheet("background-color: rgb(238, 240, 255);")
        self.categories_label.setText("")
        self.categories_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.categories_label.setObjectName("categories_label")
        self.horizontalLayout_4.addWidget(self.categories_label)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_3 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_3.setStyleSheet("background-color: rgb(238, 240, 255);")
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        self.sizes_label = QtWidgets.QLabel(parent=self.centralwidget)
        self.sizes_label.setMinimumSize(QtCore.QSize(50, 0))
        self.sizes_label.setStyleSheet("background-color: rgb(238, 240, 255);")
        self.sizes_label.setText("")
        self.sizes_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.sizes_label.setObjectName("sizes_label")
        self.horizontalLayout_3.addWidget(self.sizes_label)
        self.horizontalLayout_4.addLayout(self.horizontalLayout_3)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_5 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_5.setStyleSheet("background-color: rgb(238, 240, 255);")
        self.label_5.setObjectName("label_5")
        self.horizontalLayout.addWidget(self.label_5)
        self.quantitytBox = QtWidgets.QSpinBox(parent=self.centralwidget)
        self.quantitytBox.setMinimumSize(QtCore.QSize(46, 0))
        self.quantitytBox.setStyleSheet("background-color: rgb(235, 235, 245);\n"
"border-radius: 5px;\n"
"border: 1px solid dlack")
        self.quantitytBox.setObjectName("quantitytBox")
        self.horizontalLayout.addWidget(self.quantitytBox)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_8 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_8.setStyleSheet("background-color: rgb(238, 240, 255);")
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_5.addWidget(self.label_8)
        self.price_label = QtWidgets.QLabel(parent=self.centralwidget)
        self.price_label.setMinimumSize(QtCore.QSize(150, 0))
        self.price_label.setStyleSheet("background-color: rgb(238, 240, 255);")
        self.price_label.setText("")
        self.price_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.price_label.setObjectName("price_label")
        self.horizontalLayout_5.addWidget(self.price_label)
        self.horizontalLayout.addLayout(self.horizontalLayout_5)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.user_choise_layout = QtWidgets.QHBoxLayout()
        self.user_choise_layout.setObjectName("user_choise_layout")
        self.label_10 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_10.setStyleSheet("background-color: rgb(238, 240, 255);")
        self.label_10.setObjectName("label_10")
        self.user_choise_layout.addWidget(self.label_10)
        self.usersBox = QtWidgets.QComboBox(parent=self.centralwidget)
        self.usersBox.setMinimumSize(QtCore.QSize(250, 0))
        self.usersBox.setStyleSheet("background-color: rgb(235, 235, 245);\n"
"border-radius: 5px;\n"
"border: 1px solid dlack")
        self.usersBox.setObjectName("usersBox")
        self.usersBox.addItem("")
        self.usersBox.setItemText(0, "")
        self.user_choise_layout.addWidget(self.usersBox)
        self.verticalLayout_2.addLayout(self.user_choise_layout)
        self.commentTextEdit = QtWidgets.QPlainTextEdit(parent=self.centralwidget)
        self.commentTextEdit.setStyleSheet("background-color: rgb(235, 235, 245);\n"
"border-radius: 5px;\n"
"border: 1px solid dlack")
        self.commentTextEdit.setPlainText("")
        self.commentTextEdit.setObjectName("commentTextEdit")
        self.verticalLayout_2.addWidget(self.commentTextEdit)
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
        self.verticalLayout_2.addLayout(self.horizontalLayout_7)
        self.verticalLayout_3.addLayout(self.verticalLayout_2)
        CreateOrderWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(CreateOrderWindow)
        QtCore.QMetaObject.connectSlotsByName(CreateOrderWindow)

    def retranslateUi(self, CreateOrderWindow):
        _translate = QtCore.QCoreApplication.translate
        CreateOrderWindow.setWindowTitle(_translate("CreateOrderWindow", "MainWindow"))
        self.label.setText(_translate("CreateOrderWindow", "Продукт:"))
        self.label_6.setText(_translate("CreateOrderWindow", "Категория:"))
        self.label_3.setText(_translate("CreateOrderWindow", "Размер:"))
        self.label_5.setText(_translate("CreateOrderWindow", "Количество:"))
        self.label_8.setText(_translate("CreateOrderWindow", "Цена:"))
        self.label_10.setText(_translate("CreateOrderWindow", "Выбор пользователя:"))
        self.commentTextEdit.setPlaceholderText(_translate("CreateOrderWindow", "Коментарий"))
        self.clousing_btn.setText(_translate("CreateOrderWindow", "Отмена"))
