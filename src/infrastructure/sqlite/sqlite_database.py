import sqlite3
from typing import Tuple

class SQLiteDatabase:
    def __init__(self, db_name = 'todo.db'):
        self.db_name = db_name
        self.conn = None
        self.create_table()
        
        
    def connect(self):
        if self.conn is None:
            self.conn = sqlite3.connect(self.db_name)
        return self.conn
        
        
    def create_table(self):
        with self.connect() as conn:
            cursor = conn.cursor()
            cursor.execute('''
                       CREATE TABLE IF NOT EXISTS tasks
                       
                          (id           INTEGER PRIMARY KEY,
                            title       TEXT NOT NULL, 
                            priority    TEXT, 
                            completed   BOOLEAN DEFAULT 0)
                          ''')  
            conn.commit()
        
    def execute(self, query: str, params: Tuple = ()):
        pass
    
    def execute_many(self, query: str, params: Tuple = ()):
        with self.connect() as conn:
            cursor = conn.cursor()
            cursor.execute(query, params)
            return cursor.fetchall()
        
        
    def execute_one(self, query: str, params: Tuple = ()):
        with self.connect() as conn:
            cursor = conn.cursor()
            cursor.execute(query, params)
            return cursor.fetchone()
    
    def insert(self, query: str, params: Tuple =()) -> int:
        with self.connect() as conn:
            cursor = conn.cursor()
            cursor.execute(query, params)
            conn.commit()
            return cursor.lastrowid