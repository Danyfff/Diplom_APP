from PyQt6.QtWidgets import QMainWindow, QTableWidgetItem, QPushButton
from .forms.category_form_ui import Ui_CategoryWindow
from PyQt6.QtCore import Qt
from .db_scripts.product_scripts import product



class CategoryWindow(QMainWindow, Ui_CategoryWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
        self.get_all_categories()
        
        self.create_btn.clicked.connect(self.create_category)
        self.clousing_btn.clicked.connect(self.close)
    
    def clear_table(self):
        '''Функция для поной отчистки таблицы'''
        self.table_data.clear()
        self.table_data.setRowCount(0)
        self.table_data.setColumnCount(0)

    def create_category(self):
        name = self.name_input.text()
        if name:
            product.create_category(name)
            self.get_all_categories()

    def save_category(self):
        name = self.name_input.text()
        if name:
            product.update_category(self.category_id, name)
            self.name_input.setText('')
            self.create_btn.setText('Создать')
            self.create_btn.disconnect()
            self.create_btn.clicked.connect(self.create_category)
            self.get_all_categories()
            
    
    def change_category(self, category_id, name):
        self.category_id = category_id
        self.name_input.setText(name)
        self.create_btn.setText('Сохранить')
        self.create_btn.disconnect()
        self.create_btn.clicked.connect(self.save_category)

    def delte_category(self, category_id):
        product.delete_category(category_id)
        self.get_all_categories()

    def get_all_categories(self):
        self.clear_table()
        col_row = 0
        self.categories = product.get_all_categories()
        
        if self.categories:
            row = len(self.categories)
            
            self.table_data.setRowCount(row) 
            self.table_data.setColumnCount(4)
            self.table_data.setHorizontalHeaderLabels(
                ['Название', 'Кол-во т.', '', '']) 
            
            for cat in self.categories:
                
                col_itens = product.get_all_products_by_category(cat[0])
                if col_itens:
                    col_itens = len(col_itens)
                else:
                    col_itens = 0
                    
                self.table_data.setItem(col_row, 0, QTableWidgetItem(str(cat[1])))
                self.table_data.setItem(col_row, 1, QTableWidgetItem(str(col_itens)))
                self.change_category_btn =  QPushButton('Изменить')
                self.change_category_btn.clicked.connect(lambda _, id=cat[0], name=cat[1]: self.change_category(id, name))
                self.table_data.setCellWidget(col_row, 2, self.change_category_btn)
                self.delte_category_btn =  QPushButton('Удалить')
                self.delte_category_btn.clicked.connect(lambda _, id=cat[0]: self.delte_category(id))
                self.table_data.setCellWidget(col_row, 3, self.delte_category_btn)
                
                col_row += 1
                
        self.table_data.setColumnWidth(0, 100)
        self.table_data.setColumnWidth(1, 60)
                
        for row in range(self.table_data.rowCount()):
            item = self.table_data.item(row, 1)
            if item:
                item.setTextAlignment(Qt.AlignmentFlag.AlignHCenter)