# Form implementation generated from reading ui file 'APP\forms\forms_ui\supply_form.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_SupplyWindow(object):
    def setupUi(self, SupplyWindow):
        SupplyWindow.setObjectName("SupplyWindow")
        SupplyWindow.resize(411, 319)
        SupplyWindow.setStyleSheet("background-color: rgb(235, 231, 255);")
        self.centralwidget = QtWidgets.QWidget(parent=SupplyWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_5 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout.addWidget(self.label_5)
        self.quantitytBox = QtWidgets.QSpinBox(parent=self.centralwidget)
        self.quantitytBox.setMinimumSize(QtCore.QSize(46, 0))
        self.quantitytBox.setStyleSheet("background-color: rgb(235, 235, 245);\n"
"border-radius: 5px;\n"
"border: 1px solid dlack")
        self.quantitytBox.setObjectName("quantitytBox")
        self.horizontalLayout.addWidget(self.quantitytBox)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_3 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_4.addWidget(self.label_3)
        self.categoriesBox = QtWidgets.QComboBox(parent=self.centralwidget)
        self.categoriesBox.setMinimumSize(QtCore.QSize(150, 0))
        self.categoriesBox.setStyleSheet("background-color: rgb(235, 235, 245);\n"
"border-radius: 5px;\n"
"border: 1px solid dlack")
        self.categoriesBox.setObjectName("categoriesBox")
        self.categoriesBox.addItem("")
        self.categoriesBox.setItemText(0, "")
        self.horizontalLayout_4.addWidget(self.categoriesBox)
        self.horizontalLayout.addLayout(self.horizontalLayout_4)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.table_data = QtWidgets.QTableWidget(parent=self.centralwidget)
        self.table_data.setMinimumSize(QtCore.QSize(0, 0))
        self.table_data.setStyleSheet("background-color: rgb(253, 253, 255);\n"
"border-radius: 5px;\n"
"border: 1px solid dlack\n"
"")
        self.table_data.setObjectName("table_data")
        self.table_data.setColumnCount(0)
        self.table_data.setRowCount(0)
        self.table_data.horizontalHeader().setSortIndicatorShown(True)
        self.table_data.horizontalHeader().setStretchLastSection(True)
        self.verticalLayout_2.addWidget(self.table_data)
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
        SupplyWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(SupplyWindow)
        QtCore.QMetaObject.connectSlotsByName(SupplyWindow)

    def retranslateUi(self, SupplyWindow):
        _translate = QtCore.QCoreApplication.translate
        SupplyWindow.setWindowTitle(_translate("SupplyWindow", "MainWindow"))
        self.label_5.setText(_translate("SupplyWindow", "Количество:"))
        self.label_3.setText(_translate("SupplyWindow", "Категория:"))
        self.create_btn.setText(_translate("SupplyWindow", "Создать"))
        self.clousing_btn.setText(_translate("SupplyWindow", "Отмена"))
