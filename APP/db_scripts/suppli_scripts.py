from .database.base_manager import DBManager


class Supplies(DBManager):
    def __init__(self):
        super().__init__()
    
    #Запросы связанные с товарами
    def get_all_supplies(self):
        '''Возвращает список всех существующих поставок'''
        
        req = self.execute("SELECT * "
                "FROM supplies ")
        
        if req['code'] == 200:
            return req['data']
        else:
            return
        
    def create_suppli(self, data, quantity, product_id):
        '''Создание новой поставки'''
        
        req = self.execute("INSERT INTO supplies(data, quantity, product_id) "
                        "VALUES (?, ?, ?) ", 
                        args=(data, quantity, product_id, ), many=False)
        
        return req
    
suppli = Supplies()