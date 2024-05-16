from PyQt6.QtWidgets import QMainWindow, QTableWidgetItem
from .forms.main_form_ui import Ui_MainWindow
from .db_scripts.user_scripts import user
from .db_scripts.data_scripts import data
from .create_product_form import CreateProductWindow


class MainWindow(QMainWindow, Ui_MainWindow):
    
    main_window: QMainWindow
    
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.get_all_products()
        
        self.setWindowTitle('Главная')
        self.name_text.setText(user.name)
        self.post_text.setText(user.post)
        
        self.products_btn.clicked.connect(self.get_all_products)
        self.create_product_btn.clicked.connect(self.create_product)
        self.users_btn.clicked.connect(self.get_all_users)
        
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
        self.table_data.setColumnCount(5)
        self.table_data.setHorizontalHeaderLabels(
            ['Название', 'Размер', 'Цена', 'Наличие', 'Категория']) 
        
        for prod in products:
            self.table_data.setItem(col_row, 0, QTableWidgetItem(str(prod[1])))
            self.table_data.setItem(col_row, 1, QTableWidgetItem(str(data.get_size_item(prod[2])['data'][0])))
            self.table_data.setItem(col_row, 2, QTableWidgetItem(str(prod[3]) + ' Руб.'))
            self.table_data.setItem(col_row, 3, QTableWidgetItem(str(prod[4])))
            self.table_data.setItem(col_row, 4, QTableWidgetItem(str(data.get_categories_item(prod[5])['data'][0])))
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
        self.main_window = CreateProductWindow()
        self.main_window.show()