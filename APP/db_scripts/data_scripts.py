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

data = Data()

