from .database.base_manager import DBManager

class User(DBManager):
    def __init__(self):
        super().__init__()
        self.id = int
        self.name = str
        self.addres = str
        self.post_id = int
        self.post = str
    
    #Запросы связанные с пользователем
    def check_user(self, password, login):
        '''Проверка есть ли пользователь'''
        
        req = self.execute("SELECT id, name, addres, post_id "
                        "FROM users "
                        "WHERE password= ? AND login = ? ", 
                        args=(password, login, ), many=False)
        
        if req['code'] == 200:
            self.id = req['data'][0]
            self.name = req['data'][1]
            self.addres = req['data'][2]
            self.post_id = req['data'][3]
            self.post = self.get_post(self.post_id)
            return True
        else:
            return False
        
    def create_user(self, name, addres, login, password, post_id=3):
        '''Создание пользователя'''
        
        req = self.execute("INSERT INTO users(name, addres, login, password, post_id) "
                        "VALUES (?, ?, ?, ?, ?) ", 
                        args=(name, addres, login, password, post_id, ), many=False)
        
        return req
    
    def get_all_users(self):
        '''Получение всех пользователей'''
        req = self.execute("SELECT * "
                        "FROM users ")
        
        if req['code'] == 200:
            return req['data']
        else:
            return None
        
    def get_all_users_by_post(self, post_id):
        '''Получение пользоватей с определенной ролью'''
        req = self.execute("SELECT * "
                        "FROM users "
                        "WHERE post_id= ? ", 
                        args=(post_id, ))
        
        if req['code'] == 200:
            return req['data']
        else:
            return None
    
    def get_user(self, user_id):
        '''Получение пользователя по его id'''
        req = self.execute("SELECT * "
                        "FROM users "
                        "WHERE id= ? ", 
                        args=(user_id, ))
        
        if req['code'] == 200:
            return req['data'][0]
        else:
            return None
    
    def delete_user(self, user_id):
        '''Удаление пользоваеля по его id'''
        
        req = self.execute("DELETE FROM users "
                         "WHERE id = ?",
                        args=(user_id, ))
        
        return req
    
    def update_user(self, id, name, addres, login, password, post_id):
        '''Обновление информации о пользователе'''
        
        req = self.execute("UPDATE users "
                           "SET name = ?, addres = ?, login = ?, password = ?, post_id = ? "
                           "WHERE id = ?", 
                        args=(name, addres, login, password, post_id, id), many=False)
        
        return req
    
    #Запросы связанные с должностями
    def get_post(self, post_id):
        '''Получение должности пользователя по его id'''
        
        req = self.execute("SELECT name "
                        "FROM posts "
                        "WHERE id= ? ", 
                        args=(post_id, ), many=False)
        
        if req['code'] == 200:
            return req['data'][0]
        else:
            return None
        
    def get_all_posts(self):
        '''Получение всех должностей'''
        
        req = self.execute("SELECT * "
                        "FROM posts ")
        
        if req['code'] == 200:
            return req['data']
        else:
            return None
    
user = User()