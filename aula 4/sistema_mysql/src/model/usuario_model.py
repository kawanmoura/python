import mysql.connector

class UsuarioModel:
    def __init__(self):
        self.conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="sistema"
        )
        self.cursor = self.conn.cursor(dictionary=True)

    def get_all_users(self):
        self.cursor.execute("SELECT * FROM usuarios")
        return self.cursor.fetchall()

    def insert_user(self, nome, idade, email):
        sql = "INSERT INTO usuarios (nome, idade, email) VALUES (%s, %s, %s)"
        val = (nome, idade, email)
        self.cursor.execute(sql, val)
        self.conn.commit()
        return self.cursor.lastrowid

    def close_connection(self):
        self.cursor.close()
        self.conn.close()
