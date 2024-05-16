from PyQt6.QtWidgets import QMainWindow
from .forms.create_order_form_ui import Ui_CreateOrderWindow
from .db_scripts.data_scripts import data
from .db_scripts.user_scripts import user


class CreateOrderWindow(QMainWindow, Ui_CreateOrderWindow):
    def __init__(self, order_data):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle('Создание заказа')
        
        self.price = order_data[3]
        self.price_by = order_data[3]
        
        self.name_label.setText(order_data[1])
        self.sizes_label.setText(data.get_size(order_data[2])['data'][0])
        self.categories_label.setText(data.get_categories(order_data[5])['data'][0])
        self.quantitytBox.setRange(1, 1000)
        self.price_label.setText(str(self.price) + ' Руб.')
        
        if user.post_id == 3:
            self.usersBox.hide()
            self.label_10.hide()
        else:
            self.completion_user_box()
        
        self.quantitytBox.valueChanged.connect(self.update_price)
        self.clousing_btn.clicked.connect(self.close)
        self.create_btn.clicked
        
    def update_price(self):
        self.price_by = self.price * self.quantitytBox.value()
        self.price_label.setText(str(self.price_by) + ' Руб.')
        
    def completion_user_box(self):
        users = user.get_all_users_by_post(3)['data']
        for us in users:
            self.usersBox.addItem(str(f'{us[1]}\nid: {us[0]}'))