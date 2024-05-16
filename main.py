from APP.db_scripts.user_scripts import user
from PyQt6.QtWidgets import QApplication
import sys
from APP.login_form import Login
from APP.create_product_form import CreateProductWindow



if __name__ == '__main__': 
    app = QApplication(sys.argv)
    window = Login()
    window.show()
    app.exec()