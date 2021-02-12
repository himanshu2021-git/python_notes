#GUI...[Graphical User Interface]

#Day 31 OOPs for encapsulation and data abstraction.....
"""
from tkinter import *
root=Tk() #here we use root which help to make blank window
root.title("My Window")
#root.iconbitmap("icon's oath  ico file")
root["bg"]="skyblue"
root.geometry("400x400")#width x height
#FIX RESOLTUION
root.resizable(width= False,height=False)
root.mainloop()#execution directly open the window without open idle

"""

#adding buttons
#labels
#Entry box
#Option menu
#checckbox
#Listbox
#Radio button
#SCroll BAr
#Sliders



#row we create button and also observe the working of place,pack and grid

import tkinter as tk
ms=tk.Tk() #blank window
ms.geometry("800x500")

def Button1():
    btn1=tk.Button(ms,text="Button 1",bg="red",fg="white",width=10,height=2,activebackground="yellow",bd=8,font="Times").pack()#RELIEF AND JUSTIFY--reliif doesnt worked beacuse of borders

    btn2=tk.Button(ms,text="Button 2",bg="pink",fg="white",width=10,height=2,activebackground="green",relief="sunken").pack()

    btn3=tk.Button(ms,text="Button 3",bg="green",fg="white",width=10,height=2,activebackground="blue",relief="raised").pack()

    btn4=tk.Button(ms,text="Button 4",bg="orange",fg="white",width=10,height=2,activebackground="red",relief="groove").pack()

    btn5=tk.Button(ms,text="Button 5",bg="blue",fg="white",width=10,height=2,activebackground="orange",relief="solid").pack()

    btn6=tk.Button(ms,text="Button 6",bg="purple",fg="white",width=10,height=2,activebackground="pink",relief="flat").pack()

    btn7=tk.Button(ms,text="Button 7",bg="brown",fg="white",width=10,height=2,activebackground="purple").pack()

Button1()
