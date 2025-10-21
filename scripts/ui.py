import tkinter as tk
from textwrap import wrap
write_file_path = "output.txt"

class ui:
    def __init__(self):
        self.window = tk.Tk()

        self.window.geometry("800x500")
        self.window.title = "Minecraft Book Splitter"


        self.ui_title = tk.Label(self.window, text="Minecraft book splitter", font=('Old English Text MT', 30))
        self.ui_title.pack(padx=20, pady=20)

        self.input_box = tk.Text(self.window, height=5, font=('arial', 11))
        self.input_box.pack(padx=10, pady=10)

        self.confirm_button = tk.Button(self.window, text='confirm', command=self.show_text)
        self.confirm_button.pack()

        self.confirm_label = tk.Label(self.window, text="Awaiting input", font=("arial", 11))
        self.confirm_label.pack(padx=10,pady=10)

        self.window.mainloop()
    
    def show_text(self):
        self.final_content = ''
        split_content = wrap(self.input_box.get("1.0",'end-1c'), 256)
        for i in split_content:
            self.final_content += f"{i}\n"
            self.final_content += '=' * 75
            self.final_content += '\n'
        with open(write_file_path, 'w') as file: #Write it to a new file, and confirm this to the user
            file.write(self.final_content)
            self.confirm_label.config(text=f"Your file has been succesfully split. You can find it under the name {write_file_path} in the minecraft-book-splitter folder!", fg="green")
    
        
ui()