from .database.base_manager import DBManager

class User(DBManager):
    def __init__(self):
        super().__init__()
        self.id = int
        self.name = str
        self.addres = str
        self.post_id = int
        self.post = str
    
    def get_user_post(self, id_user):
        '''Получение '''
        
        req = self.execute("SELECT name "
                        "FROM posts "
                        "WHERE id= ? ", 
                        args=(id_user, ), many=False)
        
        return req['data'][0]
    
    
    def check_user(self, password: str, login: str):
        '''Проверка есть ли пользователь
        
        Response from the database:
        ['data'][0] = id;
        ['data'][1] = name;
        ['data'][2] = addres;
        ['data'][3] = post_id'''
        
        req = self.execute("SELECT id, name, addres, post_id "
                        "FROM users "
                        "WHERE password= ? AND login = ? ", 
                        args=(password, login, ), many=False)
        
        if req['code'] == 200:
            self.id = req['data'][0]
            self.name = req['data'][1]
            self.addres = req['data'][2]
            self.post_id = req['data'][3]
            self.post = self.get_user_post(self.post_id)
            req['data'] = {'id': self.id, 'name': self.name, 'addres': self.addres, 'post_id': self.post}
        
        return req
        
    def create_user(self, password: str, login: str):
        '''Созжание пользователя'''
        req = self.execute("INSERT INTO users(login, password, post_id) "
                        "VALUES (?, ?, 3) ", 
                        args=(login, password, ), many=False)
        
        return req
    
    def get_all_users(self):
        '''Созжание пользователя'''
        req = self.execute("SELECT id, name, addres, post_id "
                        "FROM users ")
        
        return req
    
user = User()