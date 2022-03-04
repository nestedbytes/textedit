# import the packages
from tkinter import *
from tkinter import filedialog
from tkinter import font
# config the window
root = Tk()
root.title('textedit')
root.geometry("1200x660")

# create main frame
my_frame = Frame(root)
my_frame.pack(pady=5)

# create our scroll bar
text_scroll = Scrollbar(my_frame)
text_scroll.pack(side=RIGHT, fill=Y)


# create text box
my_text = Text(my_frame, width=97, height=25, font=("Helvetica", 16), selectbackground="red", selectforeground="black", undo=True, yscrollcommand=text_scroll.set)
my_text.pack()

# configure our scrollbar
text_scroll.config(command=my_text.yview)    

# create menu 
my_menu = Menu()
root.config(menu=my_menu)

# Add file menu 
file_menu = Menu(my_menu, tearoff=False)
my_menu.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="Exit", command=root.quit)




# Add Status bar to bottom of App
status_bar = Label(root, text='Ready  ', anchor=E)
status_bar.pack(fill=X, side=BOTTOM, ipady=5)



root.mainloop()