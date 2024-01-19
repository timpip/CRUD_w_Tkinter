import tkinter as tk
from tkinter import messagebox
import mysql.connector
import datetime
import time
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
            my_page()
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

    addPwd_label = tk.Label(m_root, text="Välj lösenord:")
    addPwd_label.grid(row=3, column=1, sticky="w", padx=10, pady=5)

    addPwd_entry = tk.Entry(m_root, show="*")
    addPwd_entry.grid(row=4, column=1, padx=10, pady=5)

    # Button
    login_button = tk.Button(m_root, text="Skicka in uppgifter", command=verify_fill)
    login_button.grid(row=9, column=0, pady=10)

    
    return



def verify_fill():
    complete_form = [surname_entry.get()
                    ,lastname_entry.get()
                    ,address_entry.get()
                    ,phone_entry.get()
                    ,addUsername_entry.get()
                    ,addPwd_entry.get()]

    for input in complete_form:
        if input =="":
            messagebox.showerror("Python Error", "Du måste fylla i alla fält.")
            return
        else: pass
    user_cred()
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

def my_page():
    log_login()
    global w_title_entry,w_textbox
    w_root = tk.Tk()
    w_root.geometry("800x600")
    w_root.title("Min sida")

    buttonframe = tk.Frame(w_root)
    buttonframe.columnconfigure(0, weight=1)
    buttonframe.columnconfigure(1, weight=1)
    

    w_title = tk.Label(w_root, text="Min sida", font=("Arial", 20))
    w_title.grid(row=1, column=0,sticky="W",padx=10, pady=10)

    w_label = tk.Label(w_root, text="Posta på väggen", font=("Arial", 16))
    w_label.grid(row=2, column=0,sticky="W", padx=10, pady=10)

    w_title_label = tk.Label(w_root, text="Titel", font=("Arial", 12))
    w_title_label.grid(row=3, column=0,sticky="W", padx=10, pady=10)
    
    w_title_entry = tk.Entry(w_root)
    w_title_entry.grid(row=4, column=0,sticky="W",padx=20, pady=10)

    w_msg_label = tk.Label(w_root, text="Meddelande", font=("Arial", 12))
    w_msg_label.grid(row=5, column=0,sticky="W", padx=10, pady=10)

    w_textbox= tk.Text(w_root, height=5, font=('Arial',12))
    w_textbox.grid(row=6, column=0,sticky="W",padx=10, pady=10,columnspan=1)

    w_send_button = tk.Button(w_root, text="Skicka meddelande", command=the_wall)
    w_send_button.grid(row=7, column=0, sticky="W", padx=10,pady=10)

    w_alt_button = tk.Button(w_root, text="Ändra uppgifter", command=verify_fill)
    w_alt_button.grid(row=8,column=0,sticky="W", padx=10,pady=10)

    w_quit_button = tk.Button(w_root, text="Avsluta", command=w_root.destroy)
    w_quit_button.grid(row=9, column=0,sticky="E", padx=10,pady=10)
    return

def log_login():
    clock = str(datetime.datetime.now())
    f = open('log_login.csv', 'a')
    f.write(f"{username}, {clock}\n")
    f.close()
    send_log()

def send_log():
    #time.sleep(3600)
    conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="password",
    port=1000,
    database = "de23db"
    )
    cursor = conn.cursor()
    
    # Create the 'log' table if it doesn't exist
    cursor.execute("CREATE TABLE IF NOT EXISTS log (user VARCHAR(64), time VARCHAR(64))")
    cursor.execute("SHOW TABLES")
    cursor.fetchall()

    # Open the log file
    with open("log_login.csv", "r") as file:
        # Iterate through each line in the log file and insert into the database
        for line in file:
            user, time = line.strip().split(",")  # Assuming CSV format

            # Use parameterized query to prevent SQL injection
            cursor.execute("INSERT INTO log (user, time) VALUES (%s, %s)", (user, time))

    # Commit the changes
    conn.commit()

    # Close the database connection
    cursor.close()
    conn.close()



    



def the_wall():
     title = w_title_entry.get()
     textbox_msg = w_textbox.get("1.0", tk.END)
     print(title)
     print(textbox_msg)

if __name__ == '__main__':
    login_win()