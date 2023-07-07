import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from tkinter import Listbox
import ffmpeg


class App():
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("600x450")
        self.root.title("UniversalFileConverter")
        self.mainframe = tk.Frame(self.root, background="gray")
        self.mainframe.pack(fill='both', expand=True)

        #Text
        self.text = ttk.Label(self.mainframe, text="Universal File Converter", background="gray", font=("Comic Sans MS", 30))
        self.text.grid(row=0, column=0, padx=70)

        # Upload Button
        upload_button = ttk.Button(self.mainframe, text="Upload File", command=self.upload_file)
        upload_button.grid(row=1, column=0, pady=10)
        
        #File text
        self.file_ext_text = ttk.Label(self.mainframe, text="", background="gray", font=("Comic Sans MS",10))
        self.file_ext_text.grid(row=2, column=0)

        #List of avalible formats
        self.format_list = Listbox(self.mainframe ,height=5,font=("Comic Sans MS",10))
        self.format_list.grid(row=3, column=0)

        #Convert Button
        set_text_button = ttk.Button(self.mainframe, text="Convert!!",command=self.convert)
        set_text_button.grid(row=4, column=0, pady=10)

        #Conversion text
        self.conversion_text = ttk.Label(self.mainframe, text="", background="gray", font=("Comic Sans MS",10))
        self.conversion_text.grid(row=5, column=0)

        # Variable to store file path
        self.file_path = ""
        self.file_ext = ""

        self.root.mainloop()

    def upload_file(self):
        self.file_path = filedialog.askopenfilename()
        if self.file_path:
            print("Selected file: ", self.file_path)
            self.format_list.delete(0, 'end')

            letter = ""
            i=1
            self.file_ext = ""
            while letter != ".":
                letter = self.file_path[len(self.file_path)-i]
                self.file_ext = letter + self.file_ext 
                i += 1
            print(self.file_ext)

            letter = ""
            i = 1
            file_name = ""
            while letter != "/" and letter != "\\":
                letter = self.file_path[len(self.file_path) - i]
                file_name = letter + file_name
                i += 1
            print(file_name)

            self.file_ext_text.config(text=file_name)

            match self.file_ext:
                case ".png":
                    self.format_list.insert(1, ".jpg")
                    self.format_list.insert(2, ".webp")
                    self.format_list.insert(3, ".gif")
                    self.format_list.insert(4, ".bmp")
                    self.format_list.insert(5, ".tiff")
                case ".jpg" | ".jpeg":
                    self.format_list.insert(1, ".png")
                    self.format_list.insert(2, ".webp")
                    self.format_list.insert(3, ".gif")
                    self.format_list.insert(4, ".bmp")
                    self.format_list.insert(5, ".tiff")
                case ".webp":
                    self.format_list.insert(1, ".png")
                    self.format_list.insert(2, ".jpg")
                    self.format_list.insert(3, ".gif")
                    self.format_list.insert(4, ".bmp")
                    self.format_list.insert(5, ".tiff")
                case ".mp4":
                    self.format_list.insert(1, ".mov")
                    self.format_list.insert(2, ".avi")
                    self.format_list.insert(3, ".wmv")
                    self.format_list.insert(4, ".flv")
                    self.format_list.insert(5, ".mkv")
                case ".mov":
                    self.format_list.insert(1, ".mp4")
                    self.format_list.insert(2, ".avi")
                    self.format_list.insert(3, ".wmv")
                    self.format_list.insert(4, ".flv")
                    self.format_list.insert(5, ".mkv")
                case ".mkv":
                    self.format_list.insert(1, ".mp4")
                    self.format_list.insert(2, ".avi")
                    self.format_list.insert(3, ".wmv")
                    self.format_list.insert(4, ".flv")
                    self.format_list.insert(5, ".mp3")
                    self.format_list.insert(6, ".wav")
                    self.format_list.insert(7, ".aac")
                    self.format_list.insert(8, ".ogg")
                case ".mp3":
                    self.format_list.insert(1, ".wav")
                    self.format_list.insert(2, ".aac")
                    self.format_list.insert(3, ".ogg")
                case ".wav":
                    self.format_list.insert(1, ".mp3")
                    self.format_list.insert(2, ".aac")
                    self.format_list.insert(3, ".ogg")
                case ".aac":
                    self.format_list.insert(1, ".mp3")
                    self.format_list.insert(2, ".wav")
                    self.format_list.insert(3, ".ogg")
                case ".ogg":
                    self.format_list.insert(1, ".mp3")
                    self.format_list.insert(2, ".wav")
                    self.format_list.insert(3, ".aac")

    def convert(self):
        selected_indices = self.format_list.curselection()
        if selected_indices:
            selected_index = selected_indices[0]
            selected_format = self.format_list.get(selected_index)
            input_file = self.file_path
            output_file = self.file_path.replace(self.file_ext, f"{selected_format}")

            conversion = ffmpeg.input(input_file)
            conversion = ffmpeg.output(conversion, output_file)
            ffmpeg.run(conversion, overwrite_output=True)
            self.conversion_text.config(text=output_file)


        else:
            print("No format selected.")


if __name__ =='__main__':
    App()
