# textedit
A very bad ms word clone.Read the whole markdown to understand the code.
# Download version 1.0.0
[Download](https://github.com/shourgamer2/textedit/releases/download/ver1.0.0/TextEdit.exe)
# Clone 
``` sh 
git clone https://github.com/shourgamer2/textedit
``` 
 # Packages needed to modify this project
Tkinter
``` sh
pip install tkinter
```
Pyinstaller
``` sh 
pip install pyinstaller
```
# Modify 
import all the packages needed
``` python 
# import the packages
from tkinter import *
from tkinter import filedialog
from tkinter import font
```
Config the window
``` python 
# config the window
root = Tk()
root.title('textedit')
root.geometry("1200x660")
```
Create scroll bar
``` python
# create our scroll bar
text_scroll = Scrollbar(my_frame)
text_scroll.pack(side=RIGHT, fill=Y)
```
Create text bot 
``` python 

# create text box
my_text = Text(my_frame, width=97, height=25, font=("Helvetica", 16), selectbackground="red", selectforeground="black", undo=True, yscrollcommand=text_scroll.set)
my_text.pack()
```
Configure scroll bar 
``` python 
# configure our scrollbar
text_scroll.config(command=my_text.yview)    
```
 create menu
 ``` python 
 # create menu 
my_menu = Menu()
root.config(menu=my_menu)
```
Add file menu 
``` python 
# Add file menu 
file_menu = Menu(my_menu, tearoff=False)
my_menu.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="Exit", command=root.quit)
```
Add status bar
``` python 
# Add Status bar to bottom of App
status_bar = Label(root, text='Ready  ', anchor=E)
status_bar.pack(fill=X, side=BOTTOM, ipady=5)

root.mainloop()
```
