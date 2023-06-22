from tkinter import *
from tkinter.filedialog import *

window = Tk()
window.title("Text Editor")  # Maximize the window to full screen

txt = Text(window, fg='black', bg='light yellow', font='Arial 16')
txt.pack(fill=BOTH, expand=True)

current_file = None

def open_file():
    filepath = askopenfilename(filetypes=[("Text file", "*.txt"), ("All Files", "*.*")])
    if not filepath:
        return
    txt.delete("1.0", END)
    with open(filepath, mode='r', encoding='utf-8') as input_file:
        text = input_file.read()
        txt.insert(END, text)
        window.title(f'Text Editor - {filepath}')
    global current_file
    current_file = filepath

def save_file():
    global current_file
    if current_file:
        with open(current_file, mode='w', encoding='utf-8') as output_file:
            text = txt.get('1.0', END)
            output_file.write(text)
    else:
        filepath = asksaveasfilename(defaultextension='.txt', filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
        if not filepath:
            return
        with open(filepath, mode='w', encoding='utf-8') as output_file:
            text = txt.get('1.0', END)
            output_file.write(text)
            window.title(f'Text Editor - {filepath}')
        current_file = filepath

def change_font_size():
    font_size = size_var.get()
    txt.configure(font=f'Arial {font_size}')

menu = Menu(window)
window.config(menu=menu)
filemenu = Menu(menu)
menu.add_cascade(label='File', menu=filemenu)
filemenu.add_command(label='Open', command=open_file)
filemenu.add_command(label='Save', command=save_file)
filemenu.add_command(label='Save As...', command=save_file)

optionsmenu = Menu(menu)
menu.add_cascade(label='Options', menu=optionsmenu)

size_var = StringVar()
size_var.set('16')

font_size_menu = Menu(optionsmenu)
optionsmenu.add_cascade(label='Font Size', menu=font_size_menu)
font_size_menu.add_radiobutton(label='12', variable=size_var, value='12', command=change_font_size)
font_size_menu.add_radiobutton(label='16', variable=size_var, value='16', command=change_font_size)
font_size_menu.add_radiobutton(label='20', variable=size_var, value='20', command=change_font_size)
font_size_menu.add_radiobutton(label='24', variable=size_var, value='24', command=change_font_size)
window.mainloop()
