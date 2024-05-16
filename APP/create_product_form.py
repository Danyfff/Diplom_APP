from PyQt6.QtWidgets import QMainWindow
from .forms.create_product_form_ui import Ui_CreateProductWindow
from .db_scripts.data_scripts import data


class CreateProductWindow(QMainWindow, Ui_CreateProductWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
        self.setWindowTitle('Добавление товара')
        
        self.categories = data.get_all_categories()
        self.sizes = data.get_all_sizes()
        self.completion_form()
        
        self.clousing_btn.clicked.connect(self.close)
        self.create_btn.clicked.connect(self.create_product)

    def completion_form(self):
        for size in self.sizes.keys():
            self.sizeBox.addItem(str(size))

        for size in self.categories.keys():
            self.categoriesBox.addItem(str(size))
        
    def create_product(self):
        name = self.name_line.text()
        quantity = self.quantitytBox.text()
        size = self.sizes.get(self.sizeBox.currentText())
        categories = self.categories.get(self.categoriesBox.currentText())
        price = self.price_line.text()
        print(data.create_product(name, size, price, quantity, categories))
        self.close()