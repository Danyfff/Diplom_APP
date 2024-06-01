from PyQt6.QtWidgets import QMainWindow, QTableWidgetItem, QPushButton
from .forms.supply_form_ui import Ui_SupplyWindow
from PyQt6.QtCore import Qt
from .db_scripts.suppli_scripts import suppli
from .db_scripts.product_scripts import product
from datetime import date
import re


class SupplyWindow(QMainWindow, Ui_SupplyWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.get_all_supplies()
        
        self.quantitytBox.setMinimum(1)
        
        self.items = product.get_all_products()
        self.filling_items()
        
        self.create_btn.clicked.connect(self.create_supply)
        self.clousing_btn.clicked.connect(self.close)
    
    def clear_table(self):
        '''Функция для поной отчистки таблицы'''
        self.table_data.clear()
        self.table_data.setRowCount(0)
        self.table_data.setColumnCount(0)
    
    def filling_items(self):
        for item in self.items:
            size = product.get_size(item[2])
            self.categoriesBox.addItem(f'{item[1]}\nid: {item[0]}\nsize: {size}')
            
    def get_activ_item(self):
        item_id = re.search(r'id: (\d+)', self.categoriesBox.currentText())
        return int(item_id.group(1))
            
    def create_supply(self):
        data = date.today()
        quantity = self.quantitytBox.value()
        product_id = self.get_activ_item()
        if quantity and product_id:
            if product.update_quantity_product(product_id, quantity):
                suppli.create_suppli(data, quantity, product_id)
                self.get_all_supplies()
        
    def delte_supply(self, suppli_id, item_id, quantity):
        if product.update_quantity_product(item_id, -quantity):
            suppli.delete_supply(suppli_id)
            self.get_all_supplies()

    def get_all_supplies(self):
        
        self.clear_table()
        col_row = 0
        supplies = suppli.get_all_supplies()
        
        if supplies:
            row = len(supplies)
            
            self.table_data.setRowCount(row) 
            self.table_data.setColumnCount(4)
            self.table_data.setHorizontalHeaderLabels(
                ['Дата', 'Кол-во', 'Товар', '']) 
            
            for supp in supplies:
                    
                
                item = product.get_product(supp[3])
                if item:
                    item = item[1]
                
                self.table_data.setItem(col_row, 0, QTableWidgetItem(str(supp[1])))
                self.table_data.setItem(col_row, 1, QTableWidgetItem(str(supp[2])))
                self.table_data.setItem(col_row, 2, QTableWidgetItem(str(item)))
                self.delte_user_btn =  QPushButton('Удалить')
                self.delte_user_btn.clicked.connect(lambda _, id=supp[0], item_id=supp[3], quantity=supp[2]: self.delte_supply(id, item_id, quantity))
                self.table_data.setCellWidget(col_row, 3, self.delte_user_btn)
                
                col_row += 1
                
        self.table_data.setColumnWidth(2, 100)
        self.table_data.setColumnWidth(1, 50)
        self.table_data.setColumnWidth(0, 75)
        
        column = (0, 1, 2)
        for row in range(self.table_data.rowCount()):
            for col in column:
                item = self.table_data.item(row, col)
                if item:
                    item.setTextAlignment(Qt.AlignmentFlag.AlignHCenter)