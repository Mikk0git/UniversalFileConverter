import tkinter as tk
from tkinter import ttk
from tkinter import filedialog

class App():
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("600x450")
        self.root.title("UniversalFileConverter")
        self.mainframe = tk.Frame(self.root, background="gray")
        self.mainframe.pack(fill='both',expand=True)

        #Text
        self.text = ttk.Label(self.mainframe, text="Universal File Converter", background="gray", font=("Comic Sans MS", 30))
        self.text.grid(row=0, column=0, padx=70)

        #Button
        set_text_button = ttk.Button(self.mainframe, text="Convert!!")
        set_text_button.grid(row=2, column=0, pady=10)

        # Upload Button
        upload_button = ttk.Button(self.mainframe, text="Upload File", command=self.upload_file)
        upload_button.grid(row=1, column=0, pady=10)

        self.root.mainloop()
        return
    
    def upload_file(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            print("Selected file: ", file_path)


    
    
if __name__ =='__main__':
    App()