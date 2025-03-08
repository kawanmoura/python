import mysql.connector

class UsuarioModel:
    def __init__(self):
        self.conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="root",
            database="marea_toca_tudo"
        )
        self.cursor = self.conn.cursor(dictionary=True)

    def get_all_users(self):
        self.cursor.execute("SELECT * FROM usuarios")
        return self.cursor.fetchall()

    def email_exists(self, email):
        sql = "SELECT * FROM usuarios WHERE email = %s"
        self.cursor.execute(sql, (email,))
        return self.cursor.fetchone() is not None

    def insert_user(self, nome, idade, email):
        if self.email_exists(email):
            raise ValueError("Email já cadastrado.")
        sql = "INSERT INTO usuarios (nome, idade, email) VALUES (%s, %s, %s)"
        val = (nome, idade, email)
        self.cursor.execute(sql, val)
        self.conn.commit()
        return self.cursor.lastrowid

    def delete_user_by_id(self, user_id):
        sql = "DELETE FROM usuarios WHERE id = %s"
        self.cursor.execute(sql, (user_id,))
        self.conn.commit()
        return self.cursor.rowcount

    def update_user_by_id(self, user_id, nome, idade, email):
        sql = "UPDATE usuarios SET nome = %s, idade = %s, email = %s WHERE id = %s"
        self.cursor.execute(sql, (nome, idade, email, user_id))
        self.conn.commit()
        return self.cursor.rowcount

    def get_user_by_id(self, user_id):
        sql = "SELECT * FROM usuarios WHERE id = %s"
        self.cursor.execute(sql, (user_id,))
        return self.cursor.fetchone()

    def close_connection(self):
        self.cursor.close()
        self.conn.close()
