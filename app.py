from tkinter import *
from tkinter import filedialog

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
    self.btn_select_file = Button(self.frame_1, text="...", bg="#84e", foreground="#fff")
    self.btn_select_file.place(relx=0.9, rely=0.1, relwidth=0.1, relheight=0.05)
    
    # Generate DB
    self.btn_generate_db = Button(self.frame_1, text="Generate DB", bg="#84e", foreground="#fff")
    self.btn_generate_db.place(relx=0.6, rely=0.9, relwidth=0.2, relheight=0.1)
    
    self.btn_test_connection = Button(self.frame_1, text="Test", bg="#84e", foreground="#fff")
    self.btn_test_connection.place(relx=0.2, rely=0.9, relwidth=0.2, relheight=0.1)
    
    # Labels
    self.lb_select_file = Label(self.frame_1, text="Select a CSV File")
    self.lb_select_file.place(relx=0.1, rely=0.05)
    
    self.lb_db_user = Label(self.frame_1, text="Database User")
    self.lb_db_user.place(relx=0.1, rely=0.2)
    
    # Entries
    self.select_file_entry = Entry(self.frame_1)
    self.select_file_entry.place(relx=0.1, rely=0.1, relwidth=0.7, relheight=0.05)
    
    self.db_user_entry = Entry(self.frame_1)
    self.db_user_entry.place(relx=0.1, rely=0.25, relwidth=0.7, relheight=0.05)

Application()