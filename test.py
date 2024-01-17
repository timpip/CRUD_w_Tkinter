import mysql.connector
from tkinter import messagebox

def verify_credentials(username, password):
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="password",
        port=1000,
        database="de23db"
    )

    cursor = conn.cursor()

    # Execute a SELECT query to fetch user information based on the provided username
    cursor.execute("SELECT * FROM users WHERE username = %s", (username,))
    user_data = cursor.fetchone()

    if user_data:
        # User found, check the password
        stored_password = user_data[2]  # Assuming the password is in the third column
        if password == stored_password:
            # Passwords match, credentials are verified
            messagebox.showinfo('Login Successful', 'Credentials verified successfully!')
        else:
            # Passwords don't match
            messagebox.showerror('Login Error', 'Incorrect password. Please try again.')
    else:
        # User not found
        messagebox.showerror('Login Error', 'User not found. Please check your username.')

    conn.close()

# Example usage in your login function
def login(username, password):
    verify_credentials(username, password)
