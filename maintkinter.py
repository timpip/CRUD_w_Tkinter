import tkinter as tk
from tkinter import messagebox
import mysql.connector

user_credentials = {}

def login():
    
    global username, password
    username = login_username_entry.get()
    password = login_password_entry.get()
    
    if username == "" and password == "":
        messagebox.showerror('Python Error','Du måste skriva något!')
    elif username == "":
        messagebox.showerror('Pyton Error','Du måste ange ett användarnamn för att kunna logga in.')
    elif password == "":
        messagebox.showerror('Python Error','Vänligen ange ett lösenord.')
    else:
        #Verifiera att kunden finns i db.
        verify_cred()
        
    return
    
def verify_cred():
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="password",
        port=1000,
        database="de23db"
    )
    
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM users WHERE username = %s", (username,))
    user_data = cursor.fetchone()
    
    if user_data:
        stored_password = user_data[2]
        if password == stored_password:
            root.destroy()
            wall()
        else: messagebox.showerror("Login Error", "Fel lösenord")
    else: messagebox.showwarning("Not found", "Användaren finns inte")

    conn.close()

def login_win():
    global login_username_entry, login_password_entry, root
    # Create the login_win window
    root = tk.Tk()
    root.geometry("300x300")
    root.title("Inloggning")

    title_label = tk.Label(root, text="DE23 Portalen!", font=("Arial",18))
    title_label.grid(row=0, column=0, sticky="w", padx=10, pady=5)

    # Username Label and Entry
    login_username_label = tk.Label(root, text="Användarnamn:")
    login_username_label.grid(row=1, column=0, sticky="w", padx=10, pady=5)

    login_username_entry = tk.Entry(root)
    login_username_entry.grid(row=2, column=0, padx=10, pady=5)

    # Password Label and Entry
    login_password_label = tk.Label(root, text="Lösenord:")
    login_password_label.grid(row=3, column=0, sticky="w", padx=10, pady=5)

    login_password_entry = tk.Entry(root, show="*")  # Show asterisks to hide the password
    login_password_entry.grid(row=4, column=0, padx=10, pady=5)

    # Login Button
    login_button = tk.Button(root, text="Logga in", command=login)
    login_button.grid(row=5, column=0, pady=10, padx=10, sticky="W")

    # newUser Button
    newUser_button = tk.Button(root, text="Inget konto?", command=main)
    newUser_button.grid(row=6, column=0, pady=10,padx=10, sticky="W")

    # Start the Tkinter event loop
    root.mainloop()
    return

def main():
    global surname_entry, lastname_entry, address_entry, phone_entry, addUsername_entry, addPwd_entry, m_root
    m_root = tk.Tk()
    m_root.geometry("400x400")
    m_root.title("Information Användare")

    title_label = tk.Label(m_root, text="Fyll i din information", font=("Arial",18))
    title_label.grid(row=0, column=0, sticky="w", padx=10, pady=5)

   
    surname_label = tk.Label(m_root, text="Förnamn:")
    surname_label.grid(row=1, column=0, sticky="w", padx=10, pady=5)

    surname_entry = tk.Entry(m_root)
    surname_entry.grid(row=2, column=0, padx=10, pady=5)

    lastname_label = tk.Label(m_root, text="Efternamn:")
    lastname_label.grid(row=3, column=0, sticky="w", padx=10, pady=5)

    lastname_entry = tk.Entry(m_root)
    lastname_entry.grid(row=4, column=0, padx=10, pady=5)

    address_label = tk.Label(m_root, text="Adress:")
    address_label.grid(row=5, column=0, sticky="w", padx=10, pady=5)

    address_entry = tk.Entry(m_root)
    address_entry.grid(row=6, column=0, padx=10, pady=5)

    phone_label = tk.Label(m_root, text="Telefonnummer:")
    phone_label.grid(row=7, column=0, sticky="w", padx=10, pady=5)

    phone_entry = tk.Entry(m_root)
    phone_entry.grid(row=8, column=0, padx=10, pady=5)

    addUsername_label = tk.Label(m_root, text="Välj användarnamn:")
    addUsername_label.grid(row=1, column=1, sticky="w", padx=10, pady=5)

    addUsername_entry = tk.Entry(m_root)
    addUsername_entry.grid(row=2, column=1, padx=10, pady=5)

    addPwd_label = tk.Label(m_root, text="välj lösenord:")
    addPwd_label.grid(row=3, column=1, sticky="w", padx=10, pady=5)

    addPwd_entry = tk.Entry(m_root, show="*")
    addPwd_entry.grid(row=4, column=1, padx=10, pady=5)

    # Button
    login_button = tk.Button(m_root, text="Skicka in uppgifter", command=user_cred)
    login_button.grid(row=9, column=0, pady=10)

    # if surname_entry == "":
    #     messagebox.showerror('Python Error', 'Du måste fylla i alla fält.')
    # elif lastname_entry == "":
    #     messagebox.showerror('Python Error', 'Du måste fylla i alla fält.')
    # elif address_entry == "":
    #     messagebox.showerror('Python Error', 'Du måste fylla i alla fält.')
    # elif phone_entry == "":
    #     messagebox.showerror('Python Error', 'Du måste fylla i alla fält.')
    # elif addUsername_entry == "":
    #     messagebox.showerror('Python Error', 'Du måste fylla i alla fält.')
    # elif addPwd_entry =="":
    #     messagebox.showerror('Python Error', 'Du måste fylla i alla fält.')
    # else:
    #     return
    return

def user_cred():
    global surname, lastname, address, phone, username, password
    surname = surname_entry.get()
    lastname = lastname_entry.get()
    address = address_entry.get()
    phone = phone_entry.get()
    username = addUsername_entry.get()
    password = addPwd_entry.get()

    print(surname)
    print(lastname)
    print(address)
    print(phone)
    print(username)
    print(password)
    insert_to_db()
    m_root.destroy()
    
def insert_to_db():
    conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="password",
    port=1000,
    database = "de23db"
    )

    cursor = conn.cursor()

    cursor.execute("CREATE DATABASE IF NOT EXISTS de23db")

    cursor.execute("CREATE TABLE IF NOT EXISTS users (id INT AUTO_INCREMENT PRIMARY KEY, username VARCHAR(64), password VARCHAR(64))")
    cursor.execute("CREATE TABLE IF NOT EXISTS user_info (id INT AUTO_INCREMENT PRIMARY KEY, surname VARCHAR(64), lastname VARCHAR(64), address VARCHAR(64), phone VARCHAR(64))")

    cursor.execute("SHOW TABLES")
    cursor.fetchall()

    #cursor.execute(f"INSERT INTO users ( username, password) VALUES ('{username}', '{password}')")
    #cursor.execute(f"INSERT INTO user_info ( surname, lastname, address, phone) VALUES ('{surname}', '{lastname}', '{address}', '{phone}')")

     # För att slippa bli SQL injekterad.
    user_query = "INSERT INTO users (username, password) VALUES (%s, %s)"
    user_info_query = "INSERT INTO user_info (surname, lastname, address, phone) VALUES (%s, %s, %s, %s)"

    cursor.execute(user_query, (username, password))
    cursor.execute(user_info_query, (surname, lastname, address, phone))

    conn.commit()

def wall():
    w_root = tk.Tk()
    w_root.geometry("500x500")
    w_root.title("Väggen")    

    w_title = tk.Label(w_root, text="DE23 Väggen", font=("Arial", 20))
    w_title.pack(padx=10, pady=10)

    


login_win()

