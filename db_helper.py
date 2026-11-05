import mysql.connector
from config import DB_HOST, DB_USER, DB_PASSWORD, DB_NAME

def get_connection():
    return mysql.connector.connect(
        host=DB_HOST,
        user=DB_USER,
        password=DB_PASSWORD,
        database=DB_NAME
    )

def add_task(title, description=""):
    conn = get_connection()
    cursor = conn.cursor()
    query = "INSERT INTO tasks (title, description) VALUES (%s, %s)"
    cursor.execute(query, (title, description))
    conn.commit()
    cursor.close()
    conn.close()

def get_all_tasks():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True) # Returns rows as dictionaries
    cursor.execute("SELECT * FROM tasks ORDER BY created_at DESC")
    tasks = cursor.fetchall()
    cursor.close()
    conn.close()
    return tasks

def update_task_status(task_id, is_completed):
    conn = get_connection()
    cursor = conn.cursor()
    query = "UPDATE tasks SET is_completed = %s WHERE id = %s"
    cursor.execute(query, (is_completed, task_id))
    conn.commit()
    cursor.close()
    conn.close()

def delete_task(task_id):
    conn = get_connection()
    cursor = conn.cursor()
    query = "DELETE FROM tasks WHERE id = %s"
    cursor.execute(query, (task_id,))
    conn.commit()
    cursor.close()
    conn.close()
