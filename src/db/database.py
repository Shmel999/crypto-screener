import sqlite3

class Database:
    def __init__(self, db_name='favorites.db'):
        self.connection = sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()
        self.create_table()

    def create_table(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS favorites (
            user_id INTEGER,
            item TEXT,
            PRIMARY KEY (user_id, item)
        )''')
        self.connection.commit()

    def add_favorite(self, user_id, item):
        try:
            self.cursor.execute('INSERT INTO favorites (user_id, item) VALUES (?, ?)', (user_id, item))
            self.connection.commit()
        except sqlite3.IntegrityError:
            print('This item is already in favorites.')

    def remove_favorite(self, user_id, item):
        self.cursor.execute('DELETE FROM favorites WHERE user_id = ? AND item = ?', (user_id, item))
        self.connection.commit()

    def get_favorites(self, user_id):
        self.cursor.execute('SELECT item FROM favorites WHERE user_id = ?', (user_id,))
        return self.cursor.fetchall()

    def close(self):
        self.connection.close()