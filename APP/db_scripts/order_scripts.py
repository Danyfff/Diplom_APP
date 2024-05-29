from .database.base_manager import DBManager


class Orders(DBManager):
    def __init__(self):
        super().__init__()
        
    #Запросы связанные с заказами
    def get_all_orders(self):
        '''Возвращает список всех существующих заказов'''
        
        req = self.execute("SELECT * "
                "FROM orders ")
        
        if req['code'] == 200:
            return req['data']
        else:
            return
        
    def get_orders_by_seller(self, seller_id):
        '''Возвращает список всех существующих заказов связанных с продавцом'''
        
        req = self.execute("SELECT * "
                "FROM orders "
                "WHERE seller_id = ?",
                args=(seller_id, ))
        
        if req['code'] == 200:
            return req['data']
        else:
            return
        
    def get_orders_by_bayer(self, bayer_id):
        '''Возвращает список всех существующих заказов связанных с покупателем'''
        
        req = self.execute("SELECT * "
                "FROM orders "
                "WHERE bayer_id = ?",
                args=(bayer_id, ))
        
        if req['code'] == 200:
            return req['data']
        else:
            return
        
    def get_orders_by_status(self, status_id):
        '''Возвращает список всех существующих заказов связанных со статусом'''
        
        req = self.execute("SELECT * "
                "FROM orders "
                "WHERE status_id = ?",
                args=(status_id, ))
        
        if req['code'] == 200:
            return req['data']
        else:
            return
    
    def create_order(self, data, price, quantity, product_id, bayer_id, status_id, seller_id=None, comment=None):
        '''Создание нового заказа'''
        
        req = self.execute("INSERT INTO orders(comment, data, price, quantity, product_id, seller_id, bayer_id, status_id) "
                        "VALUES (?, ?, ?, ? ,?, ?, ?, ?) ", 
                        args=(comment, data, price, quantity, product_id, seller_id, bayer_id, status_id, ), many=False)
        
        return req
    
    def update_status_order(self, id, seller_id, status_id):
        '''Обновление статуса заказа и присвоение ему продавца'''
        
        req = self.execute("UPDATE orders "
                           "SET seller_id = ?, status_id = ? "
                           "WHERE id = ?", 
                        args=(seller_id, status_id, id), many=False)
        
        return req
    
    #Запросы связанные со статусами
    def get_status(self, status_id):
        '''Получение статуса по id'''
        
        req = self.execute("SELECT name "
                "FROM statuses "
                "WHERE id = ?",
                args=(status_id, ), many=False)
        
        if req['code'] == 200:
            return req['data'][0]
        else:
            return
    
        
order = Orders()