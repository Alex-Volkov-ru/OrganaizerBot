import sqlite3

class Database():
    def __init__(self, db_name):
        self.connection = sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()
        self.create_db()

    def create_db(self):
        try:
            query = ("CREATE TABLE IF NOT EXISTS users("
                     "id INTEGER PRIMARY KEY,"
                     "user_name TEXT,"
                     "user_phone TEXT,"
                     "telegram_id TEXT);"
                     
                     "CREATE TABLE IF NOT EXISTS transactions("
                     "id INTEGER PRIMARY KEY,"
                     "date_transaction TEXT,"
                     "amount INTEGER,"
                     "wallet_id INTEGER,"
                     "categories INTEGER);"
                     
                     "CREATE TABLE IF NOT EXISTS wallet("
                     "id INTEGER PRIMARY KEY,"
                     "id_user INTEGER,"
                     "Balance INTEGER);"
                     
                     "CREATE TABLE IF NOT EXISTS categories("
                     "id INTEGER PRIMARY KEY,"
                     "description TEXT,"
                     "category TEXT);")
            self.cursor.executescript(query)
            self.connection.commit()
        except sqlite3.Error as Error:
            print('Ошибка при создании:', Error)
    def add_user(self, user_name, user_phone, telegram_id):
        self.cursor.execute(f'INSERT INTO users (user_name,user_phone,telegram_id) VALUES (?,?,?)', (user_name, user_phone, telegram_id))
        self.connection.commit()
    def select_user_id(self, telegram_id):
        users = self.cursor.execute("SELECT * FROM users WHERE telegram_id = ?", (telegram_id,))
        return users.fetchone()
    def db_select_all(self, table):
        result = self.cursor.execute("SELECT * FROM {}".format(table))
        return result.fetchall()
    def __del__(self):
        self.cursor.close()
        self.connection.close()