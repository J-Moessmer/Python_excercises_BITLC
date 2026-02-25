#26-02-25_02_editor
#this doesnt work yet
import tkinter as tk
from tkinter import filedialog
window = tk.Tk()

window.title ("Notepad")
window.geometry ("900x600")
text_area=tk.Text(window,wrap="word")
text_area.pack(expand=True, fill="both")

def open_file():
    file=filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
    if file:
        with open(file, "r") as f:
            text_area("1.0", tk.END)
            text_area.insert(tk.END, f.read())
    
def save_file():
    file=filedialog.asksaveasfile(defaultextension=".txt", filetypes=[("Text files", "*.txt")])
    if file:
            with open(file,"w") as f:
                f.write(text_area.get("1.0", tk.END))


menu=tk.Menu(window)
window.config(menu=menu)

file_menu = tk.Menu(menu, tearoff=0)
menu.add_cascade(label="File", menu=file_menu)


file_menu.add_command(label="Open",command=open_file)
file_menu.add_command(label="Save",command=save_file)

window.mainloop()
