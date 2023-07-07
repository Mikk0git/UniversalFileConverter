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


        # Upload Button
        upload_button = ttk.Button(self.mainframe, text="Upload File", command=self.upload_file)
        upload_button.grid(row=1, column=0, pady=10)
        
        #File text
        self.file_ext_text = ttk.Label(self.mainframe, text="", background="gray", font=("Comic Sans MS",10))
        self.file_ext_text.grid(row=2, column=0)

        #Convert Button
        set_text_button = ttk.Button(self.mainframe, text="Convert!!")
        set_text_button.grid(row=3, column=0, pady=10)

        self.root.mainloop()
        return
    
    def upload_file(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            print("Selected file: ", file_path)
            

            letter = ""
            i=1
            file_ext = ""
            while letter != ".":
                letter = file_path[len(file_path)-i]
                file_ext = letter + file_ext 
                i += 1
            print(file_ext)


            self.file_ext_text.config(text="Your file extention is: "+ file_ext)
            


    def convert(self):
        print("cats are awesome")
    
    
if __name__ =='__main__':
    App()