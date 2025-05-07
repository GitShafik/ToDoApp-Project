import sqlite3

class ToDo:
    def __init__(self):
        self.conn = sqlite3.connect("todo.db")
        self.create_table()
        
    def create_table(self):
        cursor = self.conn.cursor()
        cursor.execute('''
                       CREATE TABLE IF NOT EXISTS tasks
                          (id INTEGER PRIMARY KEY,
                            title TEXT NOT NULL, priority TEXT, completed BOOLEAN DEFAULT 0);
                          ''')  
        self.conn.commit()  
        
    def add_task(self, title, priority):
        if priority not in ["Låg", "Medium", "Hög"]:
            raise ValueError("Ogiltig prioritet. Vänligen välj Låg, Medium eller Hög.")
        cursor = self.conn.cursor()
        cursor.execute('''
                       INSERT INTO tasks (title, priority)
                       VALUES (?, ?);
                       ''', (title, priority))
        self.conn.commit()
        
    def list_tasks(self):
        cursor = self.conn.cursor()
        cursor.execute("select * from tasks")
        return cursor.fetchall()

    def mark_complete(self, task_id):
        cursor = self.conn.cursor()
        cursor.execute('''
                       UPDATE tasks
                       SET completed = 1
                       WHERE id = ?;
                       ''', (task_id,))
        self.conn.commit()