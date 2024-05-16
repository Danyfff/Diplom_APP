from PyQt6.QtWidgets import QMainWindow, QTableWidgetItem, QPushButton
from .forms.main_form_ui import Ui_MainWindow
from .db_scripts.user_scripts import user
from .db_scripts.data_scripts import data
from .create_product_form import CreateProductWindow
from .create_order_form import CreateOrderWindow


class MainWindow(QMainWindow, Ui_MainWindow):
    
    main_window: QMainWindow
    
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.get_all_products()
        
        self.setWindowTitle('Главная')
        self.name_text.setText(user.name)
        self.post_text.setText(user.post)
        
        self.chec_user_usabilyty()
        
        self.products_btn.clicked.connect(self.get_all_products)
        self.create_product_btn.clicked.connect(self.create_product)
        self.users_btn.clicked.connect(self.get_all_users)
        

    
    def chec_user_usabilyty(self):
        '''Проверка на функциональность пользователя'''
        if user.post_id == 2:
            self.supplies_btn.hide()
            self.create_supplies_btn.hide()
            
        elif user.post_id == 3:
            self.create_product_btn.hide()
            self.orders_waiting_btn.hide()
            self.users_btn.hide()
            self.supplies_btn.hide()
            self.create_supplies_btn.hide()
    
    def clear_table(self):
        '''Функция для поной отчистки таблицы'''
        self.table_data.clear()
        self.table_data.setRowCount(0)
        self.table_data.setColumnCount(0)
        
    def get_all_products(self):
        '''Выводит все существующие товары'''
        
        self.clear_table()
        col_row = 0
        products = data.get_all_products()['data']
        row = len(products)
        
        self.table_data.setRowCount(row) 
        if user.post_id == 3:
            self.table_data.setColumnCount(6)
        else:
            self.table_data.setColumnCount(7)
        self.table_data.setHorizontalHeaderLabels(
            ['Название', 'Размер', 'Цена', 'Наличие', 'Категория', '', '']) 
        
        
        for prod in products:
            self.table_data.setItem(col_row, 0, QTableWidgetItem(str(prod[1])))
            self.table_data.setItem(col_row, 1, QTableWidgetItem(str(data.get_size(prod[2])['data'][0])))
            self.table_data.setItem(col_row, 2, QTableWidgetItem(str(prod[3]) + ' Руб.'))
            self.table_data.setItem(col_row, 3, QTableWidgetItem(str(prod[4])))
            self.table_data.setItem(col_row, 4, QTableWidgetItem(str(data.get_categories(prod[5])['data'][0])))
            self.delte_product_btn =  QPushButton('Заказать')
            self.delte_product_btn.clicked.connect(lambda _, data=prod: self.create_order_button_clicked(data))
            self.table_data.setCellWidget(col_row, 5, self.delte_product_btn)
            
            if user.post_id != 3:
                self.delte_product_btn =  QPushButton('Удалить')
                self.delte_product_btn.clicked.connect(lambda _, id=prod: self.delete_product_button_clicked(id))
                self.table_data.setCellWidget(col_row, 6, self.delte_product_btn)
            
            col_row += 1
            
    def get_all_users(self):
        '''Выводит всех суцествующих пользователей'''
        
        self.clear_table()
        
        col_row = 0
        users = user.get_all_users()['data']
        row = len(users)
        
        self.table_data.setRowCount(row)  
        self.table_data.setColumnCount(3)
        self.table_data.setHorizontalHeaderLabels(
            ['Имя', 'Аддрес', 'Роль']) 
        
        for us in users:
            self.table_data.setItem(col_row, 0, QTableWidgetItem(str(us[1])))
            self.table_data.setItem(col_row, 1, QTableWidgetItem(str(us[2])))
            self.table_data.setItem(col_row, 2, QTableWidgetItem(str(user.get_user_post(us[3]))))
            col_row += 1
            
    def create_product(self):
        '''Открытие окна создания продукта'''
        self.main_window = CreateProductWindow()
        self.main_window.show()
        
    def delete_product_button_clicked(self, id):
        '''Удаление продукта по id при нажатии на кнопку удаления в каталоге'''
        data.delete_product(id)
        self.get_all_products()
        
    def create_order_button_clicked(self, data):
        '''Открытие окна с созданием заказа'''
        print(data)
        self.main_window = CreateOrderWindow(data)
        self.main_window.show()