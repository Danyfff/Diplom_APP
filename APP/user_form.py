from PyQt6.QtWidgets import QMainWindow
from .forms.user_form_ui import Ui_UserWindow
from .db_scripts.user_scripts import user



class UserWindow(QMainWindow, Ui_UserWindow):
    def __init__(self, user_id=None):
        super().__init__()
        self.setupUi(self)
        
        self.posts = user.get_all_posts()
        self.filling_posts()
        
        if user_id:
            self.user_id = user_id
            self.user_data = user.get_user(user_id)
            self.update_user_form()
        else:
            self.create_user_form()
            
        self.clousing_btn.clicked.connect(self.close)
        
    def filling_posts(self):
        for post in self.posts:
            self.postsBox.addItem(str(post[1]))
    
    def get_activ_post(self):
        for post in self.posts:
            if post[1] == self.postsBox.currentText():
                return post[0]
            
    def activ_post(self, id):
        for post in self.posts:
            if post[0] == id:
                self.postsBox.setCurrentText(post[1])
    
    def create_user(self):
        name = self.name_input.text()
        addres = self.addres_input.text()
        login = self.login_input.text()
        password = self.password_input.text()
        post_id = self.get_activ_post()
        if name and login and password and post_id:
            user.create_user(name, addres, login, password, post_id)
            self.close()
    
    def update_user(self):
        name = self.name_input.text()
        addres = self.addres_input.text()
        login = self.login_input.text()
        password = self.password_input.text()
        post_id = self.get_activ_post()
        if name and login and password and post_id:
            user.update_user(self.user_id, name, addres, login, password, post_id)
            self.close()
    
    
    def create_user_form(self):
        self.create_btn.setText('Создать')
        self.create_btn.clicked.connect(self.create_user)
    
    def update_user_form(self):
        self.create_btn.setText('Сохранить')
        self.create_btn.clicked.connect(self.update_user)
        if self.user_data:
            self.name_input.setText(self.user_data[1])
            self.addres_input.setText(self.user_data[2])
            self.login_input.setText(self.user_data[3])
            self.password_input.setText(self.user_data[4])
            self.activ_post(self.user_data[5])