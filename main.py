import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="password",
    port=1000,
    database = "de23db"
)

cursor = conn.cursor()

cursor.execute("CREATE DATABASE IF NOT EXISTS de23db")

cursor.execute("CREATE TABLE IF NOT EXISTS users (id INT PRIMARY KEY, username VARCHAR(64), password VARCHAR(64))")
cursor.execute("CREATE TABLE IF NOT EXISTS user_info (id INT PRIMARY KEY, surname VARCHAR(64), lastname VARCHAR(64), address VARCHAR(64), phone VARCHAR(64))")

cursor.execute("SHOW TABLES")

for table in cursor:
    print(table)

cursor.execute(f"INSERT INTO users (id, username, password) VALUES ('1,{}, {}') ")

conn.commit()