import sqlite3 
import tkinter as tk

class CRUDGUI:
    def __init__(self,master):
        self.master = master
        self.master.title("CRUD Database App")
        
        #create UI elements
        self.name_label = tk.Label(self.master, text="Name:")
        self.name_label.grid(row=0, column=0, padx=5, pady=5)
        self.name_entry = tk.Entry(self.master)
        self.name_entry.grid(row=0, column=1, padx=5, pady=5)
        
        self.email_label = tk.Label(self.master, text="Email:")
        self.email_label.grid(row=1, column=0, padx=5, pady=5)
        self.email_entry = tk.Entry(self.master)
        self.email_entry.grid(row=1, column=1, padx=5, pady=5)
        
        self.phone_label = tk.Label(self.master, text="Phone:")
        self.phone_label.grid(row=2, column=0, padx=5, pady=5)
        self.phone_entry = tk.Entry(self.master)
        self.phone_entry.grid(row=2, column=1, padx=5, pady=5)
        
        self.add_button = tk.Button(self.master, text="Add", command=self.add_data)
        self.add_button.grid(row=3, column=0, padx=5, pady=5)
        
        self.update_button = tk.Button(self.master, text="Update", command=self.update_data)
        self.update_button.grid(row=3, column=1, padx=5, pady=5)
        
        self.delete_button = tk.Button(self.master, text="Delete", command=self.delete_data)
        self.delete_button.grid(row=3, column=2, padx=5, pady=5)
        
        self.listbox = tk.Listbox(self.master)
        self.listbox.grid(row=4,column=0, padx=5,pady=5)
        self.listbox.bind("<<ListboxSelect>>", self.load_data)
        
        self.conn = sqlite3.connect("contacts.db")
        self.cur = self.conn.cursor()
        self.cur.execute("""CREATE TABLE IF NOT EXISTS contacts
                            (id INTEGER PRIMARY KEY,
                            name TEXT NOT NULL,
                            email TEXT NOT NULL,
                            phone TEXT NOT NULL)""")
        self.conn.commit()
        #load data from database
        self.load_listbox()
        
    def load_listbox(self):
        self.listbox.delete(0, tk.END)
        self.cur.execute("SELECT * FROM contacts")
        rows = self.cur.fetchall()
        for row in rows:
            self.listbox.insert(tk.END, row[1])
    
    def load_data(self, event):
        try:
            index = self.listbox.curselection()[0]
            name = self.listbox.get(index)
            self.cur.execute("SELECT * FROM contacts WHERE name=?", (name,))
            row = self.cur.fetchone()
            self.name_entry.delete(0, tk.END)
            self.name_entry.insert(0, row[1])
            self.email_entry.delete(0, tk.END)
            self.email_entry.insert(0, row[2])
            self.phone_entry.delete(0, tk.END)
            self.phone_entry.insert(0, row[3])
        except IndexError:
            pass
        
    def add_data(self):
        name = self.name_entry.get()
        email = self.email_entry.get()
        phone = self.phone_entry.get()
        self.cur.execute("INSERT INTO contacts(name,email,phone) VALUES(?,?,?)", (name,email,phone))
        self.conn.commit()
        self.load_listbox()
        
    def update_data(self):
        try:
            index = self.listbox.curselection()[0]
            name = self.listbox.get(index)
            new_name = self.name_entry.get()
            new_email = self.email_entry.get()
            new_phone = self.phone_entry.get()
            self.cur.execute("UPDATE contacts SET name=?, email=?, phone=? WHERE name=?",(new_name, new_email, new_phone, name))
            self.conn.commit()
            self.load_listbox()
        except IndexError:
            pass
        
    def delete_data(self):
        try:
            index = self.listbox.curselection()[0]
            name= self.listbox.get(index)
            self.cur.execute("DELETE FROM contacts WHERE name=?", (name,))
            self.conn.commit()
            self.load_listbox()
        except IndexError:
            pass
    
    def __del__(self):
        self.conn.close()
        
if __name__ =="__main__":
    root= tk.Tk()
    app = CRUDGUI(root)
    root.mainloop()
