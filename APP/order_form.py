from PyQt6.QtWidgets import QMainWindow
from .forms.order_form_ui import Ui_CreateOrderWindow
from .db_scripts.product_scripts import product
from .db_scripts.user_scripts import user
from .db_scripts.order_scripts import order
from datetime import date
import re


class OrderWindow(QMainWindow, Ui_CreateOrderWindow):
    def __init__(self, item_id):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle('Создание заказа')
        
        self.item_data = product.get_product(item_id)
        self.quantitytBox.setRange(1, self.item_data[4])
        
        if user.post_id == 3:
            self.usersBox.hide()
            self.label_10.hide()
            self.create_btn.setText('Заказать')
        else:
            self.completion_user_box()
            self.create_btn.setText('Создать заказ')

        self.price_by = self.item_data[3]
        
        self.clousing_btn.clicked.connect(self.close)
        self.name_label.setText(self.item_data[1])
        self.sizes_label.setText(product.get_size(self.item_data[2]))
        self.categories_label.setText(product.get_category(self.item_data[5]))
        self.price_label.setText(str(self.item_data[3]) + ' Руб.')
        
        self.quantitytBox.valueChanged.connect(self.update_price)
        self.clousing_btn.clicked.connect(self.close)
        self.create_btn.clicked.connect(self.create_order)
    
    def get_user(self):
        user_id = re.search(r'id: (\d+)', self.usersBox.currentText())
        if user_id:
            user_id = user_id.group(1)
            return int(user_id)
        else:
            return 
        
    
    def completion_user_box(self):
        users = user.get_all_users_by_post(3)
        if users:
            for us in users:
                self.usersBox.addItem(str(f'{us[1]}\nid: {us[0]}\n{us[2]}'))
    
    def update_price(self):
        self.price_by = self.item_data[3] * self.quantitytBox.value()
        self.price_label.setText(str(self.price_by) + ' Руб.')
        
    def create_order(self):
        data = date.today()
        price = self.price_by
        quantity = self.quantitytBox.value()
        product_id = self.item_data[0]
        if user.post_id == 3:
            bayer_id = user.id
            seller_id = None
            status_id = 1
        else:
            bayer_id = self.get_user()
            seller_id = user.id
            status_id = 2
        comment = self.commentTextEdit.toPlainText()
        if product.update_quantity_product(product_id, -quantity):
            order.create_order(data, price, quantity, product_id, bayer_id, status_id, seller_id, comment)
            self.close()