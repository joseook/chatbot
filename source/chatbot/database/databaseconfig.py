import sqlite3
from datetime import datetime

DB_FILE = 'data/feedback.db'

def create_table_if_not_exists():
    """
    Cria a tabela 'feedback' se ela não existir no banco de dados.
    """
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS feedback (
        id INTEGER PRIMARY KEY,
        timestamp TEXT NOT NULL,
        user_input TEXT NOT NULL,
        bot_response TEXT NOT NULL,
        feedback TEXT NOT NULL,
        rating INTEGER,
        comments TEXT
    )
    ''')
    conn.commit()
    conn.close()

def insert_feedback(user_input, bot_response, feedback, rating, comments):
    """
    Insere um registro de feedback no banco de dados.
    """
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute('''
    INSERT INTO feedback (timestamp, user_input, bot_response, feedback, rating, comments)
    VALUES (?, ?, ?, ?, ?, ?)
    ''', (timestamp, user_input, bot_response, feedback, rating, comments))
    conn.commit()
    conn.close()

def query_negative_feedback():
    """
    Consulta feedbacks negativos (por exemplo, feedback = "Não").
    """
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM feedback WHERE feedback = "Não"')
    results = cursor.fetchall()
    conn.close()
    return results
