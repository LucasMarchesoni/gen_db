from tkinter import *
from tkinter import filedialog, messagebox
from tkinter.ttk import Combobox
from tools.database import Database

root = Tk()

class Application():
  def __init__(self):
    self.root = root
    self.screen()
    self.frame()
    self.widgets()
  
    root.mainloop()
  
  def screen(self):
    self.root.title("GenDB")
    self.root.configure(background="#eeeeee")
    self.root.geometry("500x500")
    self.root.resizable(False, False)
    
  def frame(self):
    self.frame_1 = Frame(self.root, bd=4, bg="#eeeeee")
    self.frame_1.place(relx=0.05, rely=0.05, relwidth=0.9, relheight=0.9)
    
  def widgets(self):
    # Buttons
    # Select csv file
    self.btn_select_file = Button(self.frame_1, text="...", bg="#84e", foreground="#fff", command=self.get_file)
    self.btn_select_file.place(relx=0.9, rely=0.05, relwidth=0.1, relheight=0.05)
    
    # Generate DB
    self.btn_generate_db = Button(self.frame_1, text="Generate DB", bg="#84e", foreground="#fff")
    self.btn_generate_db.place(relx=0.6, rely=0.9, relwidth=0.2, relheight=0.1)
    
    # Test connection
    self.btn_test_connection = Button(self.frame_1, text="Test", bg="#84e", foreground="#fff", command=self.test_conn)
    self.btn_test_connection.place(relx=0.1, rely=0.9, relwidth=0.2, relheight=0.1)
    
    # Labels
    self.lb_select_file = Label(self.frame_1, text="Select a CSV File")
    self.lb_select_file.place(relx=0.1, rely=0)
    
    self.lb_db_user = Label(self.frame_1, text="Database User")
    self.lb_db_user.place(relx=0.1, rely=0.10)
    
    self.lb_db_password = Label(self.frame_1, text="Database Password")
    self.lb_db_password.place(relx=0.1, rely=0.20)
    
    self.lb_db_host = Label(self.frame_1, text="Database Host")
    self.lb_db_host.place(relx=0.1, rely=0.30)
    
    self.lb_db_table_name = Label(self.frame_1, text="Table name")
    self.lb_db_table_name.place(relx=0.1, rely=0.40)
    
    self.lb_db_name = Label(self.frame_1, text="Database name")
    self.lb_db_name.place(relx=0.1, rely=0.50)
    
    self.lb_dg_engine = Label(self.frame_1, text="Select a db engine")
    self.lb_dg_engine.place(relx=0.1, rely=0.60)
    
    # Entries
    self.select_file_entry = Entry(self.frame_1)
    self.select_file_entry.place(relx=0.1, rely=0.05, relwidth=0.7, relheight=0.05)
    
    self.db_user_entry = Entry(self.frame_1)
    self.db_user_entry.place(relx=0.1, rely=0.15, relwidth=0.7, relheight=0.05)
    
    self.db_password_entry = Entry(self.frame_1)
    self.db_password_entry.place(relx=0.1, rely=0.25, relwidth=0.7, relheight=0.05)
    
    self.db_host_entry = Entry(self.frame_1)
    self.db_host_entry.place(relx=0.1, rely=0.35, relwidth=0.7, relheight=0.05)
    
    self.db_table_name_entry = Entry(self.frame_1)
    self.db_table_name_entry.place(relx=0.1, rely=0.45, relwidth=0.7, relheight=0.05)
    
    self.db_name_entry = Entry(self.frame_1)
    self.db_name_entry.place(relx=0.1, rely=0.55, relwidth=0.7, relheight=0.05)
    
    # Combobox
    self.cb_db_engine = Combobox(self.frame_1)
    self.cb_db_engine.place(relx=0.1, rely=0.65, relwidth=0.7, relheight=0.05)
    self.cb_db_engine['values'] = ("Postgres", "MySQL", "SQL Server", "SQLite", "Oracle")
    self.cb_db_engine.current(0)
  
  def get_file(self):
   name = filedialog.askopenfilename()
   self.select_file_entry.insert(0, name)
   
  def test_conn(self):
    if (not self.db_user_entry.get() or 
        not self.db_password_entry.get() or 
        not self.db_name_entry.get() or 
        not self.select_file_entry.get() or 
        not self.db_table_name_entry.get() or 
        not self.db_host_entry.get() or 
        not self.cb_db_engine.get()):
      messagebox.showerror("Error", "Please fill all fields")
      return
    
    try:
      database = Database(self.db_user_entry.get(), 
                            self.db_password_entry.get(), 
                            self.db_name_entry.get(), 
                            self.select_file_entry.get(), 
                            self.db_table_name_entry.get(), 
                            self.db_host_entry.get())
        
      result = database.test_conn(self.cb_db_engine.get())
        
      if result:
        messagebox.showinfo("Success", "Connection established successfully")
      else:
        messagebox.showerror("Error", "Connection error")
            
    except FileNotFoundError:
      messagebox.showerror("Error", "File not found. Please check the file path.")
    

Application()