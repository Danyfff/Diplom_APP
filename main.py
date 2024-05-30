from PyQt6.QtWidgets import QApplication
import sys
from APP.login_form import Login


def login():
    app = QApplication(sys.argv)
    window = Login()
    window.show()
    app.exec()

if __name__ == '__main__': 
    login()