from .database.base_manager import DBManager

class Data(DBManager):
    def __init__(self):
        super().__init__()
    
    def get_all_products(self):
        '''Возвращает список всех существующих товаров'''
        
        req = self.execute("SELECT * "
                "FROM products ")
        
        return req
    
    def get_categories_item(self, id_item):
        '''Получение категории товара по его id'''
    
        req = self.execute("SELECT name "
                "FROM categories "
                "WHERE id= ? ",
                args=(id_item, ), many=False)
        
        return req
    
    def get_size_item(self, id_item):
        '''Получение размера товара по его id'''
    
        req = self.execute("SELECT name "
                "FROM sizes "
                "WHERE id= ? ",
                args=(id_item, ), many=False)
        
        return req
    
    def get_all_categories(self):
        '''Получение всех существующих категорий'''

        categories = {}
        
        req = self.execute("SELECT * "
                "FROM categories ")
        
        if req['code'] == 200:
            for cat in req['data']:
                categories[cat[1]] = cat[0]
                
            return categories
    
    def get_all_sizes(self):
        '''Получение всех существующих размеров'''
        
        sizes = {}
    
        req = self.execute("SELECT * "
                "FROM sizes ")
        
        if req['code'] == 200:
            for cat in req['data']:
                sizes[cat[1]] = cat[0]
                
            return sizes
        
    def create_product(self, name, size_id, price, quantity, category_id):
        '''Создание нового товара'''
        
        req = self.execute("INSERT INTO products(name, size_id, price, quantity_in_stock, category_id) "
                        "VALUES (?, ?, ?, ? ,?) ", 
                        args=(name, size_id, price, quantity, category_id, ), many=False)
        
        return req
    
    def delete_product(self, id_product):
        '''Удаление товара по его id'''
        
        req = self.execute("DELETE FROM products "
                         "WHERE id = ?",
                        args=(id_product, ))
        
        return req
        
data = Data()


