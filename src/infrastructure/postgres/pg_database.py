import psycopg2

class PGDatabase:
    def __init__(self):
        self.connect_params = { 
            'dbname': 'todo',  
            'user': 'postgres',        
            'password': 'postgres',        
            'host': 'localhost',        
            'port': '5432'    }
        
        self.conn = None
        self.create_table()
        
    def connect(self):
        if self.conn is None:
            self.conn = psycopg2.connect(**self.connect_params)
        return self.conn
        
    def crate_table(self):
        with self.connect() as conn:
            cursor = conn.cursor()
            cursor.execute('''
                           CREATE TABLE IF NOT EXISTS tasks
                           (
                               id       SERIAL PRIMARY KEY,
                               title    VARCHAR(255) NOT NULL,
                               priority VARCHAR(255),
                               complete BOOLEAN DEFAULT FALSE
                           )
                           ''')
            
            conn.commit()
            
            
    def execute(self, query: str, params: tuple = ()):
        with self.connect() as conn:
            cursor = conn.cursor()
            cursor.execute(query, params)
            conn.commit