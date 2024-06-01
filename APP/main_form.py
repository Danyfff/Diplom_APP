from PyQt6.QtWidgets import QMainWindow, QTableWidgetItem, QPushButton
from .forms.main_form_ui import Ui_MainWindow
from .db_scripts.user_scripts import user
from .db_scripts.product_scripts import product
from .db_scripts.order_scripts import order
from .db_scripts.suppli_scripts import suppli
from PyQt6.QtCore import Qt
from .product_form import ProductWindow
from .user_form import UserWindow
from .order_form import OrderWindow


class MainWindow(QMainWindow, Ui_MainWindow):
    
    main_window: QMainWindow
    
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.chec_user_usabilyty()
        
        self.setWindowTitle('Главная')
        self.name_text.setText(user.name)
        self.post_text.setText(user.post)
        
        self.cancel_btn.clicked.connect(self.close)
        self.products_btn.clicked.connect(self.get_all_products)
        self.create_btn.clicked.connect(self.create_product)
        self.orders_btn.clicked.connect(self.get_all_orders)
        self.orders_waiting_btn.clicked.connect(self.get_all_orders_in_weiting)
        self.my_orders_btn.clicked.connect(self.get_all_user_orders)
        self.users_btn.clicked.connect(self.get_all_users)
        self.supplies_btn.clicked.connect(self.get_all_supplies)
        self.categories_btn.clicked.connect(self.get_all_categories)
        self.user_prifil_btn.clicked.connect(self.user_form)
        
        self.get_all_products()
        
    def clear_table(self):
        '''Функция для поной отчистки таблицы'''
        self.table_data.clear()
        self.table_data.setRowCount(0)
        self.table_data.setColumnCount(0)
    
    def chec_user_usabilyty(self):
        '''Проверка на функциональность пользователя'''
        if user.post_id == 2:
            self.supplies_btn.hide()
            self.orders_btn.hide()
            
        elif user.post_id == 3:
            self.orders_btn.hide()
            self.orders_waiting_btn.hide()
            self.users_btn.hide()
            self.supplies_btn.hide()
            self.categories_btn.hide()

    def user_form(self):
        self.main_window = UserWindow(my_user_data=True)
        self.main_window.show()
        
# Товары
    def create_product(self):
        self.main_window = ProductWindow()
        self.main_window.show()

    def order_product(self, product_id):
        self.main_window = OrderWindow(product_id)
        self.main_window.show()

    def delte_product(self, product_id):
        product.delete_product(product_id)
        self.get_all_products()

    def change_product(self, product_id):
        self.main_window = ProductWindow(product_id)
        self.main_window.show()

    def get_all_products(self):
        '''Выводит все существующие товары'''
        if user.post_id != 3:
            self.create_btn.show()
            self.create_btn.clicked.disconnect()
            self.create_btn.clicked.connect(self.create_product)
        else:
            self.create_btn.hide()
        
        self.clear_table()
        col_row = 0
        products = product.get_all_products()
        if products:
            row = len(products)
            
            self.table_data.setRowCount(row) 
            if user.post_id == 3:
                self.table_data.setColumnCount(6)
            else:
                self.table_data.setColumnCount(8)
            self.table_data.setHorizontalHeaderLabels(
                ['Название', 'Размер', 'Цена', 'Наличие', 'Категория', '', '', '']) 
            
            for prod in products:
                self.table_data.setItem(col_row, 0, QTableWidgetItem(str(prod[1])))
                self.table_data.setItem(col_row, 1, QTableWidgetItem(str(product.get_size(prod[2]))))
                self.table_data.setItem(col_row, 2, QTableWidgetItem(str(prod[3]) + ' Руб.'))
                self.table_data.setItem(col_row, 3, QTableWidgetItem(str(prod[4])))
                self.table_data.setItem(col_row, 4, QTableWidgetItem(str(product.get_category(prod[5]))))
                
                if user.post_id != 3:
                    self.order_product_btn =  QPushButton('Создать заказ')
                else:
                    self.order_product_btn =  QPushButton('Заказать')
                self.order_product_btn.clicked.connect(lambda _, id=prod[0]: self.order_product(id))
                self.table_data.setCellWidget(col_row, 5, self.order_product_btn)
                
                if user.post_id != 3:
                    self.delte_product_btn =  QPushButton('Удалить')
                    self.delte_product_btn.clicked.connect(lambda _, id=prod[0]: self.delte_product(id))
                    self.table_data.setCellWidget(col_row, 6, self.delte_product_btn)
                    self.change_product_btn =  QPushButton('Изменить')
                    self.change_product_btn.clicked.connect(lambda _, id=prod[0]: self.change_product(id))
                    self.table_data.setCellWidget(col_row, 7, self.change_product_btn)
                
                col_row += 1
        
        self.table_data.setColumnWidth(0, 150)
                
        column = (1, 2, 3, 4)
        
        for row in range(self.table_data.rowCount()):
            for col in column:
                item = self.table_data.item(row, col)
                if item:
                    item.setTextAlignment(Qt.AlignmentFlag.AlignHCenter)
            
# Заказы
    def get_all_orders(self):
        '''Выводит все существующие товары'''
        
        self.create_btn.hide()
        
        self.clear_table()
        col_row = 0
        orders = order.get_all_orders()
        if orders:
            row = len(orders)
            
            self.table_data.setRowCount(row) 
            self.table_data.setColumnCount(8)
            self.table_data.setHorizontalHeaderLabels(
                ['Коментарий', 'Дата', 'Цена', 'Кол-во', 'Товар', 'Продавец', 'Покупатель', 'Статус']) 
            
            for ord in orders:
                
                item = product.get_product(ord[5])
                if item:
                    item = item[1]
                    
                seller = user.get_user(ord[6])
                if seller:
                    seller = seller[1]
                    
                bayer = user.get_user(ord[7])
                if bayer:
                    bayer = bayer[1]
                    
                status = order.get_status(ord[8])
                
                self.table_data.setItem(col_row, 0, QTableWidgetItem(str(ord[1])))
                self.table_data.setItem(col_row, 1, QTableWidgetItem(str(ord[2])))
                self.table_data.setItem(col_row, 2, QTableWidgetItem(str(ord[3]) + ' Руб.'))
                self.table_data.setItem(col_row, 3, QTableWidgetItem(str(ord[4])))
                self.table_data.setItem(col_row, 4, QTableWidgetItem(str(item)))
                self.table_data.setItem(col_row, 5, QTableWidgetItem(str(seller)))
                self.table_data.setItem(col_row, 6, QTableWidgetItem(str(bayer)))
                self.table_data.setItem(col_row, 7, QTableWidgetItem(str(status)))
                
                
                col_row += 1
                
        self.table_data.resizeRowsToContents()
        self.table_data.setColumnWidth(7, 80)
        self.table_data.setColumnWidth(6, 100)
        self.table_data.setColumnWidth(5, 100)
        self.table_data.setColumnWidth(4, 160)
        self.table_data.setColumnWidth(3, 50)
        self.table_data.setColumnWidth(2, 80)
        self.table_data.setColumnWidth(1, 80)
        self.table_data.setColumnWidth(0, 220)
        
        column = (1, 2, 3, 4, 5 ,6 ,7)
        for row in range(self.table_data.rowCount()):
            for col in column:
                item = self.table_data.item(row, col)
                if item:
                    item.setTextAlignment(Qt.AlignmentFlag.AlignHCenter)

# Заказы в обработке
    def change_order(self, order_id):
        order.update_status_order(order_id, user.id, 2)
        self.get_all_orders_in_weiting()

    def get_all_orders_in_weiting(self):
        '''Выводит все существующие товары'''
        
        self.create_btn.hide()
        
        self.clear_table()
        col_row = 0
        orders = order.get_orders_by_status(1)
        if orders:
            row = len(orders)
            
            self.table_data.setRowCount(row) 
            self.table_data.setColumnCount(8)
            self.table_data.setHorizontalHeaderLabels(
                ['Коментарий', 'Дата', 'Цена', 'Кол-во', 'Товар', 'Продавец', 'Покупатель', '']) 
            
            for ord in orders:
                
                item = product.get_product(ord[5])
                if item:
                    item = item[1]
                    
                seller = user.get_user(ord[6])
                if seller:
                    seller = seller[1]
                else:
                    seller = 'Нет'
                    
                bayer = user.get_user(ord[7])
                if bayer:
                    bayer = bayer[1]
                
                self.table_data.setItem(col_row, 0, QTableWidgetItem(str(ord[1])))
                self.table_data.setItem(col_row, 1, QTableWidgetItem(str(ord[2])))
                self.table_data.setItem(col_row, 2, QTableWidgetItem(str(ord[3])))
                self.table_data.setItem(col_row, 3, QTableWidgetItem(str(ord[4])))
                self.table_data.setItem(col_row, 4, QTableWidgetItem(str(item)))
                self.table_data.setItem(col_row, 5, QTableWidgetItem(str(seller)))
                self.table_data.setItem(col_row, 6, QTableWidgetItem(str(bayer)))
                self.change_product_btn =  QPushButton('Принять')
                self.change_product_btn.clicked.connect(lambda _, id=ord[0]: self.change_order(id))
                self.table_data.setCellWidget(col_row, 7, self.change_product_btn)
                
                col_row += 1
        
        self.table_data.setColumnWidth(6, 100)
        self.table_data.setColumnWidth(5, 100)
        self.table_data.setColumnWidth(4, 150)
        self.table_data.setColumnWidth(3, 50)
        self.table_data.setColumnWidth(2, 80)
        self.table_data.setColumnWidth(1, 80)
        self.table_data.setColumnWidth(0, 220)
        
        column = (1, 2, 3, 5, 6)
        for row in range(self.table_data.rowCount()):
            for col in column:
                item = self.table_data.item(row, col)
                if item:
                    item.setTextAlignment(Qt.AlignmentFlag.AlignHCenter)
                
# Заказы залоггиненого пользователя
    def get_all_user_orders(self):
        '''Выводит все существующие товары'''
        
        self.create_btn.hide()
        
        self.clear_table()
        col_row = 0
        if user.post_id != 3:
            orders = order.get_orders_by_seller(user.id)
        else:
            orders = order.get_orders_by_bayer(user.id)
        
        if orders:
            row = len(orders)
            
            self.table_data.setRowCount(row) 
            self.table_data.setColumnCount(8)
            self.table_data.setHorizontalHeaderLabels(
                ['Коментарий', 'Дата', 'Цена', 'Кол-во', 'Товар', 'Продавец', 'Покупатель', 'Статус']) 
            
            for ord in orders:
                
                item = product.get_product(ord[5])
                if item:
                    item = item[1]
                    
                seller = user.get_user(ord[6])
                if seller:
                    seller = seller[1]
                else:
                    seller = 'Нет'
                    
                bayer = user.get_user(ord[7])
                if bayer:
                    bayer = bayer[1]
                    
                status = order.get_status(ord[8])
                
                self.table_data.setItem(col_row, 0, QTableWidgetItem(str(ord[1])))
                self.table_data.setItem(col_row, 1, QTableWidgetItem(str(ord[2])))
                self.table_data.setItem(col_row, 2, QTableWidgetItem(str(ord[3]) + ' Руб.'))
                self.table_data.setItem(col_row, 3, QTableWidgetItem(str(ord[4])))
                self.table_data.setItem(col_row, 4, QTableWidgetItem(str(item)))
                self.table_data.setItem(col_row, 5, QTableWidgetItem(str(seller)))
                self.table_data.setItem(col_row, 6, QTableWidgetItem(str(bayer)))
                self.table_data.setItem(col_row, 7, QTableWidgetItem(str(status)))
                
                col_row += 1
                
        self.table_data.setColumnWidth(6, 100)
        self.table_data.setColumnWidth(5, 100)
        self.table_data.setColumnWidth(4, 150)
        self.table_data.setColumnWidth(3, 50)
        self.table_data.setColumnWidth(2, 80)
        self.table_data.setColumnWidth(1, 80)
        self.table_data.setColumnWidth(0, 250)
        
        column = (1, 2, 3, 5, 6, 7)
        for row in range(self.table_data.rowCount()):
            for col in column:
                item = self.table_data.item(row, col)
                if item:
                    item.setTextAlignment(Qt.AlignmentFlag.AlignHCenter)
                
# Пользователи
    def create_user(self):
        self.main_window = UserWindow()
        self.main_window.show()

    def change_user(self, user_id):
        self.main_window = UserWindow(user_id)
        self.main_window.show()

    def delte_user(self, user_id):
        user.delete_user(user_id)
        self.get_all_users()

    def get_all_users(self):
        '''Выводит все существующие товары'''
        
        self.create_btn.show()
        self.create_btn.clicked.disconnect()
        self.create_btn.clicked.connect(self.create_user)
        
        self.clear_table()
        col_row = 0
        users = user.get_all_users()
        
        if users:
            row = len(users)
            
            self.table_data.setRowCount(row-1) 
            self.table_data.setColumnCount(7)
            self.table_data.setHorizontalHeaderLabels(
                ['Имя', 'Адрес', 'Логин', 'Пароль', 'Роль', '', '']) 
            
            for us in users:
                if us[0] != user.id:
                    
                    post = user.get_post(us[5])
                    
                    self.table_data.setItem(col_row, 0, QTableWidgetItem(str(us[1])))
                    self.table_data.setItem(col_row, 1, QTableWidgetItem(str(us[2])))
                    self.table_data.setItem(col_row, 2, QTableWidgetItem(str(us[3])))
                    self.table_data.setItem(col_row, 3, QTableWidgetItem(str(us[4])))
                    self.table_data.setItem(col_row, 4, QTableWidgetItem(str(post)))
                    self.change_user_btn =  QPushButton('Изменить')
                    self.change_user_btn.clicked.connect(lambda _, id=us[0]: self.change_user(id))
                    self.table_data.setCellWidget(col_row, 5, self.change_user_btn)
                    self.delte_user_btn =  QPushButton('Удалить')
                    self.delte_user_btn.clicked.connect(lambda _, id=us[0]: self.delte_user(id))
                    self.table_data.setCellWidget(col_row, 6, self.delte_user_btn)
                    
                    col_row += 1
                
# Поставки
    def create_suppli(self):
        print(f'Создать поставку')

    def delte_suppli(self, suppli_id):
        print(f'удалить {suppli_id}')

    def get_all_supplies(self):
        '''Выводит все существующие товары'''
        
        self.create_btn.show()
        self.create_btn.clicked.disconnect()
        self.create_btn.clicked.connect(self.create_suppli)
        
        self.clear_table()
        col_row = 0
        supplies = suppli.get_all_supplies()
        
        if supplies:
            row = len(supplies)
            
            self.table_data.setRowCount(row) 
            self.table_data.setColumnCount(4)
            self.table_data.setHorizontalHeaderLabels(
                ['Дата', 'Количество', 'Товар', '']) 
            
            for supp in supplies:
                    
                item = product.get_product(supp[2])
                if item:
                    item = item[1]
                
                self.table_data.setItem(col_row, 0, QTableWidgetItem(str(supp[1])))
                self.table_data.setItem(col_row, 1, QTableWidgetItem(str(supp[2])))
                self.table_data.setItem(col_row, 2, QTableWidgetItem(str(item)))
                self.delte_user_btn =  QPushButton('Удалить')
                self.delte_user_btn.clicked.connect(lambda _, id=supp[2]: self.delte_suppli(id))
                self.table_data.setCellWidget(col_row, 3, self.delte_user_btn)
                
                col_row += 1
                
# Категории
    def create_category(self):
        print(f'Создать категорию')

    def change_category(self, category_id):
        print(f'Изменить {category_id}')

    def delte_category(self, category_id):
        print(f'удалить {category_id}')

    def get_all_categories(self):
        '''Выводит все существующие товары'''
        
        self.create_btn.show()
        self.create_btn.clicked.disconnect()
        self.create_btn.clicked.connect(self.create_category)
        
        self.clear_table()
        col_row = 0
        categories = product.get_all_categories()
        
        if categories:
            row = len(categories)
            
            self.table_data.setRowCount(row) 
            self.table_data.setColumnCount(4)
            self.table_data.setHorizontalHeaderLabels(
                ['Название', 'Кол-во товаров', '', '']) 
            
            for cat in categories:
                
                col_itens = product.get_all_products_by_category(cat[0])
                if col_itens:
                    col_itens = len(col_itens)
                
                self.table_data.setItem(col_row, 0, QTableWidgetItem(str(cat[1])))
                self.table_data.setItem(col_row, 1, QTableWidgetItem(str(col_itens)))
                self.change_category_btn =  QPushButton('Изменить')
                self.change_category_btn.clicked.connect(lambda _, id=cat[0]: self.delte_suppli(id))
                self.table_data.setCellWidget(col_row, 2, self.change_category_btn)
                self.delte_category_btn =  QPushButton('Удалить')
                self.delte_category_btn.clicked.connect(lambda _, id=cat[0]: self.delte_category(id))
                self.table_data.setCellWidget(col_row, 3, self.delte_category_btn)
                
                col_row += 1