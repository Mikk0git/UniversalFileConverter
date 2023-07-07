import tkinter as tk
from tkinter import ttk

class App():
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("600x450")
        self.root.title("UniversalFileConverter")
        self.mainframe = tk.Frame(self.root, background="gray")
        self.mainframe.pack(fill='both',expand=True)
        self.root.mainloop()
        return
    
if __name__ =='__main__':
    App()