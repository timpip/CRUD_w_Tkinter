import tkinter as tk
from tkinter import messagebox


class myGUI:

    def __init__(self):

        self.root = tk.Tk()
        self.root.geometry("500x500")
        self.root.title("DE23 portalen")

        #Sätter label
        self.label = tk.Label(self.root, text=" portalen", font=("Arial",18))
        self.label.pack(padx=10, pady=10)

        #Sätter textbody
        self.textbody = tk.Text(self.root, height=5, font=("Arial", 16))
        self.textbody.pack(padx=10, pady=10)

        #skapar en variebel för status på knapp
        self.check_state = tk.IntVar()
        
        #Skapar check button 
        self.check = tk.Checkbutton(self.root, text= "Show Message Box", font=("Arial", 16), variable=self.check_state)
        self.check.pack(padx=10, pady=10)

        #Skapar knapp
        self.button = tk.Button(self.root,text= "Show Message", font=("Arial", 18), command = self.show_message)
        self.button.pack(padx=10, pady=10)


        self.root.mainloop()

    def show_message(self):
        if self.check_state.get() == 0:
            print(self.textbody.get('1.0', tk.END))
        else: 
            messagebox.showinfo(title="Message", message=self.textbody.get('1.0', tk.END))


myGUI()

import tkinter as tk
from tkinter import messagebox
import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="name",
    password="pass"
)

# Skapar en programruta som döps till root
root = tk.Tk()

# Bestämmer storlek och namn på rutan
root.geometry("500x500")
root.title("Bankomat")

# Skapar en fast märkning  med bestämd storlek och font
label = tk.Label(root, text="BANKOMAT!", font=('Arial', 18))
label.pack(padx=20, pady=20)

#Skapar en textruta som man kan skriva i programmet med font och storlek
textbox= tk.Text(root, height=3, font=('Arial',16))
textbox.pack(padx=10)

#Skapar en mindre textruta med bara en rad
# myentry = tk.Entry(root)
# myentry.pack(padx=20)

#Lägger till knapp
button = tk.Button(root, text="Klicka här!", font=("Arial", 18))
button.pack(padx=10,pady=30)

#Grid
buttonframe = tk.Frame(root)
buttonframe.columnconfigure(0, weight=1)
buttonframe.columnconfigure(1, weight=1)
buttonframe.columnconfigure(2, weight=1)

#Skapar knappar
btn1 = tk.Button(buttonframe, text="1", font=("Arial",18))
btn1.grid(row=0,column=0, sticky=tk.W+tk.E)

btn2 = tk.Button(buttonframe, text="2", font=("Arial",18))
btn2.grid(row=0,column=1, sticky=tk.W+tk.E)

btn3 = tk.Button(buttonframe, text="3", font=("Arial",18))
btn3.grid(row=0,column=2, sticky=tk.W+tk.E)

btn4 = tk.Button(buttonframe, text="4", font=("Arial",18))
btn4.grid(row=1,column=0, sticky=tk.W+tk.E)

btn5 = tk.Button(buttonframe, text="5", font=("Arial",18))
btn5.grid(row=1,column=1, sticky=tk.W+tk.E)

btn6 = tk.Button(buttonframe, text="6", font=("Arial",18))
btn6.grid(row=1,column=2, sticky=tk.W+tk.E)
# Packar in det ovan i programmet och fill="x" betyder att knapparna ska stretcha sig.
buttonframe.pack(fill="x")


#Placerad knapp, bra för widgets, man får exakt var man vill ha den
# placeradkapp = tk.Button(root, text="Placerad Knapp")
# placeradkapp.place(x=200, y=200, height=100, width=100)

root.mainloop()

def error_msg():
    win = tk.Tk()
    win.geometry("700x300")
    messagebox.showerror('Python Error','Du måste skriva något!')
    label.pack(padx=10,pady=10)

    win.mainloop()

error_msg()