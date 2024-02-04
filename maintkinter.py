import tkinter as tk
from tkinter import messagebox
from tkinter import scrolledtext
import mysql.connector
import datetime
import schedule
import time
import pymongo
import os
import pandas as pd
user_credentials = {}


def create_db():
    conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="password",
    port=1000
    )

    cursor = conn.cursor()
    cursor.execute("CREATE DATABASE IF NOT EXISTS de23db")
    cursor.close()
    conn.close()


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

    cursor.execute("SELECT * FROM users WHERE username = %s AND isActive = '1'", (username,))
    user_data = cursor.fetchone()
    
    if user_data:
        stored_password = user_data[1]
        if password == stored_password:
            root.destroy()
            my_page()
        else: messagebox.showerror("Login Error", "Fel lösenord")
    else: messagebox.showwarning("Not found", "Användaren finns inte")

    conn.close()

def login_win():
    create_db()
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

    search_wall_button = tk.Button(root, text="Sök", command=search)
    search_wall_button.grid(row=7, column=0, pady=10,padx=10, sticky="W")

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
    global surname, lastname, address, phone, username, password, isActive
    surname = surname_entry.get()
    lastname = lastname_entry.get()
    address = address_entry.get()
    phone = phone_entry.get()
    username = addUsername_entry.get()
    password = addPwd_entry.get()
    isActive = 1

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

    cursor.execute("CREATE TABLE IF NOT EXISTS users (username VARCHAR(64) PRIMARY KEY, password VARCHAR(64), isActive INT)")#Lägg till isActive kolumn
    cursor.execute("CREATE TABLE IF NOT EXISTS user_info (username VARCHAR(64) PRIMARY KEY, surname VARCHAR(64), lastname VARCHAR(64), address VARCHAR(64), phone VARCHAR(64))")
    cursor.execute("CREATE TABLE IF NOT EXISTS log (user VARCHAR(64), entry_time VARCHAR(64))")
    cursor.execute("SHOW TABLES")
    cursor.fetchall()


     # För att slippa bli SQL injekterad.
    user_query = "INSERT INTO users (username, password, isActive) VALUES (%s, %s, %s)"
    user_info_query = "INSERT INTO user_info (username, surname, lastname, address, phone) VALUES (%s, %s, %s, %s, %s)"

    cursor.execute(user_query, (username, password, isActive))
    cursor.execute(user_info_query, (username, surname, lastname, address, phone))

    conn.commit()

def my_page():
    log_login()
    global w_title_entry,w_textbox, w_root
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

    w_search_button = tk.Button(w_root, text="Sök meddelande", command=search)
    w_search_button.grid(row=8, column=0, sticky="W", padx=10,pady=10)

    w_alt_button = tk.Button(w_root, text="Ändra uppgifter", command=change)
    w_alt_button.grid(row=9,column=0,sticky="W", padx=10,pady=10)

    w_quit_button = tk.Button(w_root, text="Avsluta", command=w_root.destroy)
    w_quit_button.grid(row=10, column=0,sticky="E", padx=10,pady=10)

    w_root.mainloop()
    return

def log_login():
    clock = str(datetime.datetime.now())
    f = open('log.csv', 'a')
    f.write(f"{username}, {clock}\n")
    f.close()
    store_log()
    

def change():
    global new_name, new_lastname, new_address, new_phone, c_root
    global c_surname_entry, c_lastname_entry, c_address_entry, c_phone_entry
    c_root = tk.Tk()
    c_root.geometry("800x600")
    c_root.title("Ändra uppgifter")

    c_title_label = tk.Label(c_root, text="Ändra dina personliga uppgifter", font=("Arial",18))
    c_title_label.grid(row=0, column=0, sticky="w", padx=10, pady=5)

    c_surname_label = tk.Label(c_root, text="Nytt förnamn:")
    c_surname_label.grid(row=1, column=0, sticky="w", padx=10, pady=5)

    c_surname_entry = tk.Entry(c_root)
    c_surname_entry.grid(row=2, column=0, padx=10, pady=5)

    c_lastname_label = tk.Label(c_root, text="Nytt Efternamn:")
    c_lastname_label.grid(row=3, column=0, sticky="w", padx=10, pady=5)

    c_lastname_entry = tk.Entry(c_root)
    c_lastname_entry.grid(row=4, column=0, padx=10, pady=5)

    c_address_label = tk.Label(c_root, text="Ny Adress:")
    c_address_label.grid(row=5, column=0, sticky="w", padx=10, pady=5)

    c_address_entry = tk.Entry(c_root)
    c_address_entry.grid(row=6, column=0, padx=10, pady=5)

    c_phone_label = tk.Label(c_root, text="Nytt Telefonnummer:")
    c_phone_label.grid(row=7, column=0, sticky="w", padx=10, pady=5)

    c_phone_entry = tk.Entry(c_root)
    c_phone_entry.grid(row=8, column=0, padx=10, pady=5)

    # Button
    c_send_button = tk.Button(c_root, text="Ändra uppgifter", command=send_change)
    c_send_button.grid(row=9, column=0, pady=10)
    
    c_return_button = tk.Button(c_root, text="Tillbaka", command=c_root.destroy)
    c_return_button.grid(row=10, column=0, pady=10)

    c_del_button = tk.Button(c_root, text="Ta bort konto", command=delete)
    c_del_button.grid(row=11, column=0, pady=10)

    new_name = c_surname_entry.get()
    new_lastname = c_lastname_entry.get()
    new_address = c_address_entry.get()
    new_phone = c_phone_entry.get()
    return new_name, new_lastname, new_address, new_phone


def send_change():
    new_name = c_surname_entry.get()
    new_lastname = c_lastname_entry.get()
    new_address = c_address_entry.get()
    new_phone = c_phone_entry.get()
    conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="password",
    port=1000,
    database = "de23db"
    )
    cursor = conn.cursor()
    
    if new_name != "":
        cursor.execute("UPDATE de23db.user_info SET surname=%s WHERE username=%s", (new_name, username))

    if new_lastname != "":
        cursor.execute("UPDATE de23db.user_info SET lastname=%s WHERE username=%s", (new_lastname, username))

    if new_address != "":
        cursor.execute("UPDATE de23db.user_info SET address=%s WHERE username=%s", (new_address, username))

    if new_phone != "":
        cursor.execute("UPDATE de23db.user_info SET phone=%s WHERE username=%s", (new_phone, username))
    
    conn.commit()
    c_root.destroy()
    messagebox.showinfo("Information","Ändringarna gjorda!")
    return

def wait_hour(): 
    excel()
    store_log()
    file = "log.csv"
    f = open(file, "w+")
    f.close()


def run_schedule(): 
    schedule.every().hour.do(wait_hour)
    while True:
        schedule.run_pending()
        time.sleep(1)

def store_log(): #Stoppar in datan från log filen till databasen
    
    conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="password",
    port=1000,
    database = "de23db"
    )
    cursor = conn.cursor()
    
    with open("log.csv", "r") as file:
        # Iterate through each line in the log file and insert into the database
        for line in file:
            user, entry_time = line.strip().split(",")
            print(user,entry_time)
            # Use parameterized query to prevent SQL injection
            cursor.execute("INSERT INTO log (user, entry_time) VALUES (%s, %s)", (user, entry_time))

    # Commit the changes
    conn.commit()

    # Close the database connection
    cursor.close()
    conn.close()

    
    
       


def the_wall():
     global title, textbox_msg, postedBy
     title = w_title_entry.get()
     postedBy = username
     textbox_msg = w_textbox.get("1.0", tk.END)
     insert_to_wall()

def insert_to_wall():
    myclient = pymongo.MongoClient("mongodb://localhost:27017")
    mydb = myclient["the_wall"]

    mycol = mydb["the_wall_col"]
    mydict = {title:textbox_msg, 'user':postedBy}

    mycol.insert_one(mydict)
    messagebox.showinfo("Meddelande", "Meddelandet skickat till väggen!")

def search():
    global s_search_entry, s_search_user_entry
    s_root = tk.Tk()
    s_root.geometry("600x500")
    s_root.title("Sök på väggen")

    s_title_label = tk.Label(s_root, text="Sök på väggen", font=("Arial",22))
    s_title_label.grid(row=1, column=0, sticky="w", padx=10, pady=5)

    # s_msg_label = tk.Label(s_root, text=your_string, font=("Arial", 16))
    # s_msg_label.grid(row=2, column=0, sticky="w", padx=10, pady=5)

    s_search_label = tk.Label(s_root, text="Sök på titel", font=("Arial",18))
    s_search_label.grid(row=2, column=0, sticky="w", padx=10, pady=5)

    s_search_entry = tk.Entry(s_root)
    s_search_entry.grid(row=3, column=0, sticky="w", padx=10, pady=5)

    s_search_user = tk.Label(s_root, text="Sök på användare", font=("Arial",18))
    s_search_user.grid(row=4, column=0, sticky="w", padx=10, pady=5)

    s_search_user_entry = tk.Entry(s_root)
    s_search_user_entry.grid(row=5, column=0, sticky="w", padx=10, pady=5)

    s_search_button = tk.Button(s_root, text="Sök på titel", command=show)
    s_search_button.grid(row=6, column=0, sticky="w", padx=10, pady=5)
    
    s_search_button = tk.Button(s_root, text="Sök på användare", command=ushow)
    s_search_button.grid(row=6, column=1, padx=10, pady=5)

def show():
    myclient = pymongo.MongoClient("mongodb://localhost:27017")
    mydb = myclient["the_wall"]  
    mycol = mydb["the_wall_col"]
    title = s_search_entry.get()
    
    query = {title: {"$exists": True}}
    result = mycol.find_one(query)
    
    if result:
        result.pop('_id',None)
        messagebox.showinfo("Resultat", result)
        
    else: messagebox.showerror("Alert", "Inget resultat hittades.")
    myclient.close()

def ushow():
    myclient = pymongo.MongoClient("mongodb://localhost:27017")
    mydb = myclient["the_wall"]  
    mycol = mydb["the_wall_col"]
    uuser = s_search_user_entry.get()

    query = {"user":uuser}
    
    count = mycol.count_documents(query)
    
    if count > 0:
        messagebox.showinfo("Resultat", f"{uuser} har postat {count} inlägg.")
    else:
        messagebox.showerror("Alert", "Inget resultat hittades.")
    myclient.close()

    
def delete():
    erase = messagebox.askokcancel(title="Ta bort konto", message="Är du säker?")
    if erase == True:
        conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="password",
        port=1000,
        database = "de23db"
        )
        cursor = conn.cursor()
        cursor.execute("UPDATE users SET isActive = '0' WHERE username = %s", (username,))
        conn.commit()
        cursor.close()
        conn.close()
        
        w_root.destroy()
        c_root.destroy()
    elif erase == False:
        pass


def excel():
    # Read existing data from Excel file if it exists
    file_path = r"C:\Users\Timot\Documents\Data Engineer 23\4.Programmering inom platform development\testfolder\log_info.xlsx"
    try:
        existing_df = pd.read_excel(file_path)
    except FileNotFoundError:
        existing_df = pd.DataFrame(columns=['year', 'month', 'day', 'hour', 'count'])

    # Read CSV file and perform transformations
    df = pd.read_csv("log.csv", header=None, names=['timestamp'])
    df['timestamp'] = pd.to_datetime(df['timestamp'])
    df['year'] = df['timestamp'].dt.year
    df['month'] = df['timestamp'].dt.month
    df['day'] = df['timestamp'].dt.day
    df['hour'] = df['timestamp'].dt.hour

    # Count occurrences of each unique combination of 'year', 'month', 'day', 'hour'
    count_df = df.groupby(['year', 'month', 'day', 'hour']).size().reset_index(name='count')

    # Append new data to existing data
    combined_df = pd.concat([existing_df, count_df], ignore_index=True)

    # Save the updated data to Excel file
    with pd.ExcelWriter(file_path, engine='openpyxl') as writer:
        combined_df.to_excel(writer, index=False, sheet_name='Sheet1')




if __name__ == '__main__':
    login_win()

if __name__ == "__main__":
    run_schedule()