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
        
        self.login_btn.clicked.connect(self.check_user)
        self.registrate_btn.clicked.connect(self.registerate_user)


    def check_user(self):
        req = user.check_user(self.login.text(), self.password.text())
        if req['code'] == 200:
            self.main_window = MainWindow()
            self.main_window.show()
            self.close()
        
        elif req['code'] == 201:    
            print('NO USER')
        
        else:
            print('EROR 400')

    def registerate_user(self):
        user.create_user(self.login.text(), self.password.text())
        req = user.check_user(self.login.text(), self.password.text())
        print(req)