import sqlite3
import os
from .settings import DATA_PATH, DB_PATH


class DBManager:
    def __init__(self):
        self.db_path = DB_PATH
        if not self.check_base():
            self.create_base()
            
            
    # Проверка есть ли БД
    def check_base(self) -> bool:
        return os.path.exists(self.db_path)

    # Подключение к бд
    def connect_to_base(self):
        conn = sqlite3.connect(self.db_path)
        cur = conn.cursor()
        return conn, cur

    # Создание бд
    def create_base(self):
        conn, cur = self.connect_to_base()
        try:
            cur.executescript(open(DATA_PATH, encoding="utf-8").read())
            conn.commit()
            print('Tables are created')
        except sqlite3.Error as ex:
            print(ex)
        finally:
            conn.close()

    # выполнение скрипта SQL
    def execute(self, query: str, args=(), many: bool = True):
        conn, cur = self.connect_to_base()
        try:
            res = cur.execute(query, args)
            result = res.fetchall() if many else res.fetchone()
            conn.commit()
            last_row_id = cur.lastrowid
            if result == None or result == []:
                return {"code": 201, 'lastrowid': last_row_id}
            else:
                return {"code": 200, "data": result, 'lastrowid': last_row_id}
        except sqlite3.Error as er:
            print(str(er))
            return {"code": 400}
        finally:
            conn.close()