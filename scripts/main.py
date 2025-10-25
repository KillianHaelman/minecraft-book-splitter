import tkinter as tk
from tkinter import filedialog
from textwrap import wrap

class ui:
    def __init__(self):
        self.file_path = ''
        self.window = tk.Tk()

        self.window.geometry("800x500")
        self.window.title = "Minecraft Book Splitter"


        self.ui_title = tk.Label(self.window, text="Minecraft book splitter", font=('Old English Text MT', 30))
        self.ui_title.pack(padx=20, pady=20)

        self.input_box = tk.Text(self.window, height=5, font=('arial', 11))
        self.input_box.pack(padx=10, pady=10)

        self.choosefile_button = tk.Button(self.window, text='Choose File', command=self.open_file)
        self.choosefile_button.pack()

        self.chooseoutput_button = tk.Button(self.window, text='Choose output folder', command=self.open_output_path)
        self.chooseoutput_button.pack()

        self.confirm_button = tk.Button(self.window, text='confirm', command=self.show_confirm_text)
        self.confirm_button.pack()

        self.confirm_label = tk.Label(self.window, text="Awaiting input", font=("arial", 11))
        self.confirm_label.pack(padx=10,pady=10)

        self.window.mainloop()
    
    def open_file(self):
        self.file_path = filedialog.askopenfilename()
        print(self.file_path)

    def open_output_path(self):
        self.write_file_path = filedialog.askdirectory() + "/output.txt"
        print(self.write_file_path)

    def show_confirm_text(self):
        self.final_content = ''
        if len(self.file_path) > 0:
            with open(self.file_path, 'r') as file:
                content = file.read()
            split_content = wrap(content, 256)
        elif len(self.input_box.get("1.0",'end-1c')) > 0:
           split_content = wrap(self.input_box.get("1.0",'end-1c'), 256)
        else:
            return
        for i in split_content:
            self.final_content += f"{i}\n"
            self.final_content += '=' * 75
            self.final_content += '\n'
        with open(self.write_file_path, 'w') as file: #Write it to a new file, and confirm this to the user
            file.write(self.final_content)
            self.confirm_label.config(text=f"Your file has been succesfully split. You can find it under the location {self.write_file_path}!", fg="green")
    
        
ui()