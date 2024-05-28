from PyQt6.QtCore import pyqtSignal
from PyQt6.QtWidgets import QMainWindow
from .forms.login_form_ui import Ui_LoginWindow
from .db_scripts.user_scripts import user
from .main_form import MainWindow


class Login(QMainWindow, Ui_LoginWindow):

    login_correct = pyqtSignal()
    main_window: QMainWindow

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle('Вход')
        
        self.name.hide()
        
        self.login_btn.clicked.connect(self.check_user)
        self.registrate_btn.clicked.connect(self.registerate_user_form)
        self.login.textChanged.connect(self.no_eror)
        self.password.textChanged.connect(self.no_eror)
        self.name.textChanged.connect(self.no_eror)

    def no_eror(self):
        self.login.setStyleSheet('background-color: rgb(235, 235, 245)')
        self.password.setStyleSheet('background-color: rgb(235, 235, 245)')
        self.name.setStyleSheet('background-color: rgb(235, 235, 245)')
    
    def eror(self):
        self.login.setStyleSheet('background-color: rgb(235, 64, 52)')
        self.password.setStyleSheet('background-color: rgb(235, 64, 52)')
        self.name.setStyleSheet('background-color: rgb(235, 64, 52)')

    def registerate_user_form(self):
        self.registrate_btn.clicked.disconnect()
        self.login_btn.clicked.disconnect()
        self.login_btn.clicked.connect(self.check_user_form)
        self.registrate_btn.clicked.connect(self.registerate_user)
        self.name.show()
        pass
    
    def check_user_form(self):
        self.registrate_btn.clicked.disconnect()
        self.login_btn.clicked.disconnect()
        self.registrate_btn.clicked.connect(self.registerate_user_form)
        self.login_btn.clicked.connect(self.check_user)
        self.name.hide()
        pass


    def registerate_user(self):
        name = self.name.text()
        login = self.login.text()
        password = self.password.text()
        if not user.check_user(login, password) and login and password and name:
            user.create_user(name, None, login, password)
            if user.check_user(login, password):
                self.main_window = MainWindow()
                self.main_window.show()
                self.close()
        else:
            self.eror()

    def check_user(self):
        login = self.login.text()
        password = self.password.text()
        if user.check_user(login, password) and login and password:
            self.main_window = MainWindow()
            self.main_window.show()
            self.close()
        else:
            self.eror()

