from PyQt6.QtWidgets import QMainWindow
from .forms.product_form_ui import Ui_CreateProductWindow
from .db_scripts.product_scripts import product


class ProductWindow(QMainWindow, Ui_CreateProductWindow):
    def __init__(self, product_id=None):
        super().__init__()
        self.setupUi(self)
        
        self.quantitytBox.setMinimum(1)
        self.categories = product.get_all_categories()
        self.sizes = product.get_all_sizes()
        self.completion_form()
        
        if product_id:
            self.update_product_form(product_id)
            self.product_id = product_id
        else:
            self.create_product_form()
        
        self.clousing_btn.clicked.connect(self.close)
        

    def completion_form(self):
        for size in self.sizes:
            self.sizeBox.addItem(str(size[1]))

        for cat in self.categories:
            self.categoriesBox.addItem(str(cat[1]))
        
    def get_activ_size(self):
        for size in self.sizes:
            if size[1] == self.sizeBox.currentText():
                return size
        return None
    
    def get_activ_category(self):
        for cat in self.categories:
            if cat[1] == self.categoriesBox.currentText():
                return cat
        return None
    
    def activ_size(self, id):
        for size in self.sizes:
            if size[0] == id:
                self.sizeBox.setCurrentText(size[1])
                
    
    def activ_category(self, id):
        for cat in self.categories:
            if cat[0] == id:
                self.categoriesBox.setCurrentText(cat[1])
        
    def update_product_form(self, product_id):
        self.create_btn.setText('Сохранить')
        self.create_btn.clicked.connect(self.update_product)
        prod = product.get_product(product_id)
        if prod:
            self.name_line.setText(prod[1])
            self.activ_size(prod[2])
            self.price_line.setText(str(prod[3]))
            self.quantitytBox.setValue(prod[4])
            self.activ_category(prod[5])
            
    def update_product(self):
        name = self.name_line.text()
        quantity = self.quantitytBox.text()
        categories = self.get_activ_category()
        size = self.get_activ_size()
        price = self.price_line.text()
        
        if price:
            price = ''.join(filter(str.isdigit, price))
            if price:
                price = int(price)
                if name and size and categories:
                    product.update_product(self.product_id, name, size[0], price, quantity, categories[0])
                    self.close()
    
    def create_product_form(self):
        self.create_btn.setText('Создать')
        self.create_btn.clicked.connect(self.create_product)
        
    def create_product(self):
        name = self.name_line.text()
        quantity = self.quantitytBox.text()
        categories = self.get_activ_category()
        size = self.get_activ_size()
        price = self.price_line.text()

        if price:
            price = ''.join(filter(str.isdigit, price))
            if price:
                price = int(price)
                if name and size and quantity and categories:
                    product.create_product(name, size[0], price, quantity, categories[0])
                    self.close()