# -*- coding: utf-8 -*-
"""
Created on Wed Jan 22 19:31:26 2020

@author: EGLOBAL
"""

import tkinter as tk
top = tk.Tk()
#top.mainloop()

var = tk.StringVar() 
label = tk.Message(top, textvariable = var, relief = tk.RAISED )

var.set("Hey!? How are you doing?")
label.pack()
top.mainloop()


from PIL import Image, ImageTk
from tkinter import scrolledtext
window = tk.Tk()
window.title("Welcome")
window.geometry('390x300')
lbl = tk.Label(window, text = "Whay's my favorite video", font = ("Arial bold", 20))
ima = ImageTk.PhotoImage(Image.read( r'C:\src1\for_new_course\some.jpg'))
def clicked():
    ImageTk.PhotoImage(Image.open(ima))     
button = tk.Button(window, text = 'click to find out', bg = 'red', fg = 'green', command = clicked)
button.grid(column = 0, row =1)
lbl.grid(column =0, row = 0)
window.mainloop()



from tkinter import * 
from tkinter.ttk import *
  
root = Tk() 
Label(root, text = 'GeeksforGeeks', font =('Verdana', 15)).pack(side = TOP, pady = 10) 
  
# Creating a photoimage object to use image 
photo = PhotoImage(file = r'some.jpg') 
photoimage = photo.subsample(3, 3) 
  
# here, image option is used to 
# set image on button 
# compound option is used to align 
# image on LEFT side of button 
Button(root, text = 'Click Me !', image = photoimage,compound = LEFT).pack(side = TOP) 
  
mainloop() 

from tkinter import *  
from PIL import ImageTk,Image  
root = Tk()  
canvas = Canvas(root, width = 300, height = 300)  
canvas.pack()  
img = ImageTk.PhotoImage(Image.open("some.jpg"))  
canvas.create_image(20, 20, anchor=NW, image=img) 
root.mainloop() 









#command = clicked)
#from tkinter import *
#root = Tk()
#root.title("Creater window")
#
#def Img():
#    r = Toplevel()
#    r.title("My image")
#    canvas = Canvas(r, height=600, width=600)
#    canvas.pack()
#    my_image = PhotoImage(file=r'C:\src1\for_new_course\lena.png', master= root)
#    canvas.create_image(0, 0, anchor=NW, image=my_image)
#    r.mainloop()
#
#btn = Button(root, text = "Click Here to see creator Image", command = Img)
#btn.grid(row = 0, column = 0)
#
#root.mainloop()

import tkinter as tk 
window = tk.Tk()
window.title("welcome to this page")
window.geometry('350x390')
lbl = tk.Label(window, text = "hello", font = ("Arial bold", 20))
txt = tk.Entry(window, width = 10, state = 'disabled')
print(txt)
txt.grid(column = 1, row = 0)
def clicked():
    res = "Welcome to " + txt.get()
    lbl.configure(text = res)
button = tk.Button(window, text = "Click me", bg = 'orange', fg = 'red', command = clicked)

button.grid(column = 1, row = 100)
lbl.grid(column = 0, row = 0)
window.mainloop()

    
import tkinter.ttk as tkk
window = tk.Tk()
window.title("welcome to this page")
window.geometry('350x300')

combo = tkk.Combobox(window)
combo['value'] = (1, 2, 3, 4, 5, 'TEXT' )
combo.current(1)
combo.grid(column = 0, row = 0)
chk_state = tk.BooleanVar()
chk_state.set(True)
chk = tkk.Checkbutton(window, text = 'choose', var = chk_state)
chk.grid(column = 1, row = 0)
combo.mainloop()


import tkinter as tk
window = tk.Tk()
window.title("welcome to my house")
window.geometry('350x300')
br = tk.IntVar()  #tk.BooleanVar()
rad1 = tk.Radiobutton(window, text = 'first', value = 1, variable = br)
rad2 = tk.Radiobutton(window, text = 'second', value = 2, variable = br)
rad3 = tk.Radiobutton(window, text = 'third', value = 3, variable = br)
def clicked():
    print(br.get())
button = tk.Button(window, text = 'Click Me', command = clicked)
rad1.grid(column = 0, row = 0)
rad2.grid(column = 1, row = 0)
rad3.grid(column = 2, row = 0)
button.grid(column = 3, row = 0)
window.mainloop()


from tkinter import scrolledtext
window = tk.Tk()
window.title("Welcome")
window.geometry('390x300')
txt = scrolledtext.ScrolledText(window, width = 40, height = 10)
txt.insert(INSERT, 'you can insert your text here')
#txt.delete(1.0, END)
txt.grid(column = 0, row = 0)
window.mainloop()


from tkinter import messagebox
window = tk.Tk()
window.title('welcome')
window.geometry('350x300')

def clicked():
    messagebox.showinfo(title = 'Error', message = 'you need to insert only numbers' )
def clicked_error():
    messagebox.showerror(title = 'Error', message = 'you cant do it' )
def clicked_warning():
    messagebox.showwarning(title = 'Error', message = 'you need to insert only letter' )

bu = tk.Button(window, text = 'Click me', command = clicked)
bu1 = tk.Button(window, text = 'Hello', command = clicked_error)
bu2 = tk.Button(window, text = 'What', command = clicked_warning)

bu.grid(column = 0, row = 0)
bu1.grid(column = 1, row = 0)
bu2.grid(column = 2, row = 0)
window.mainloop()


from tkinter import messagebox 
res = messagebox.askquestion('Message title','Message content') 
res = messagebox.askyesno('Message title','Message content') 
res = messagebox.askyesnocancel('Message title','Message content') 
res = messagebox.askokcancel('Message title','Message content') 
res = messagebox.askretrycancel('Message title','Message content')





