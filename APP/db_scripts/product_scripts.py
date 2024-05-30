from .database.base_manager import DBManager


class Products(DBManager):
    def __init__(self):
        super().__init__()
    
    #Запросы связанные с товарами
    def get_all_products(self):
        '''Возвращает список всех существующих товаров'''
        
        req = self.execute("SELECT * "
                "FROM products ")
        
        if req['code'] == 200:
            return req['data']
        else:
            return
    
    def get_all_products_by_category(self, category_id):
        '''Возвращает список всех существующих товаров'''
        
        req = self.execute("SELECT * "
                "FROM products "
                "WHERE category_id = ?",
                args=(category_id, ))
        
        if req['code'] == 200:
            return req['data']
        else:
            return
    
    def get_product(self, product_id):
        '''Возвращает список всех существующих товаров'''
        
        req = self.execute("SELECT * "
                "FROM products "
                "WHERE id = ?",
                args=(product_id, ))
        
        if req['code'] == 200:
            return req['data'][0]
        else:
            return
    
    def create_product(self, name, size_id, price, quantity_in_stock, category_id):
        '''Создание нового товара'''
        
        req = self.execute("INSERT INTO products(name, size_id, price, quantity_in_stock, category_id) "
                        "VALUES (?, ?, ?, ? ,?) ", 
                        args=(name, size_id, price, quantity_in_stock, category_id, ), many=False)
        
        return req
    
    def delete_product(self, product_id):
        '''Удаление товара по его id'''
        
        req = self.execute("DELETE FROM products "
                         "WHERE id = ?",
                        args=(product_id, ))
        
        return req
    
    def update_product(self, id, name, size_id, price, quantity_in_stock, category_id):
        '''Обновление информации о товаре'''
        
        req = self.execute("UPDATE products "
                           "SET name = ?, size_id = ?, price = ?, quantity_in_stock = ?, category_id = ? "
                           "WHERE id = ?", 
                        args=(name, size_id, price, quantity_in_stock, category_id, id), many=False)
        
        return req
    
    def update_quantity_product(self, id, quantity):
        '''Обновление информации о количестве товара'''
        
        product = self.get_product(id)
        if product:
            quantity = product[4] + quantity
        else:
            return False
        
        req = self.execute("UPDATE products "
                           "SET quantity_in_stock = ? "
                           "WHERE id = ?", 
                        args=(quantity, id), many=False)
        
        return True
    
    #Запросы связанные с категориями
    def get_all_categories(self):
        '''Получение всех существующих категорий'''
        
        req = self.execute("SELECT * "
                "FROM categories ")
        
        if req['code'] == 200:
            return req['data']
        else:
            return
    
    def get_category(self, id_cat):
        '''Получение категорию по его id'''
    
        req = self.execute("SELECT name "
                "FROM categories "
                "WHERE id= ? ",
                args=(id_cat, ), many=False)
        
        if req['code'] == 200:
            return req['data'][0]
        else:
            return
        
    def delete_category(self, id_cat):
        '''Удаление категории по ее id'''
        
        req = self.execute("DELETE FROM categories "
                         "WHERE id = ?",
                        args=(id_cat, ))
        
        return req
    
    #Запросы связанные с размерами
    def get_all_sizes(self):
        '''Получение всех существующих размеров'''
    
        req = self.execute("SELECT * "
                "FROM sizes ")
        
        if req['code'] == 200:
            return req['data']
        else:
            return
    
    def get_size(self, id_size):
        '''Получение размера товара по его id'''
    
        req = self.execute("SELECT name "
                "FROM sizes "
                "WHERE id= ? ",
                args=(id_size, ), many=False)
        
        if req['code'] == 200:
            return req['data'][0]
        else:
            return
    
product = Products()