import passwordgenerator

import pyperclip
import tkinter
from tkinter import *


class gui:

    def __init__(self, root):
        self.root=root
        self.f1=Frame(root)
        self.f2=Frame(root)
        self.f3=Frame(root)
        self.f4=Frame(root)

        self.f1.grid(row=0, column=0)
        self.f2.grid(row=2, column=0)
        self.f3.grid(row=3, column=0)
        self.f4.grid(row=4, column=0)
        
        self.decvars()
        self.elements()
        #self.caller()

    def copy(self):
        pyperclip.copy(self.outpass.get())

    def clear(self):
        self.outpass.set("")
        self.passdigit.set(4)
        
        self.symbolvar.set(0)
        self.smallvar.set(1)
        self.capsvar.set(0)
        self.numvar.set(1)

    def caller(self):
        #passlist=[digits, symbols, small, caps, nums]
        passlist=[self.passdigit.get(),
                  self.symbolvar.get(),
                  self.smallvar.get(),
                  self.capsvar.get(),
                  self.numvar.get()]
        password=passwordgenerator.a.askbygui(passlist)
        self.outpass.set(password)

    def decvars(self):
        self.outpass=StringVar()
        self.passdigit=IntVar()
        self.symbolvar=IntVar()
        self.smallvar=IntVar()
        self.capsvar=IntVar()
        self.numvar=IntVar()

        self.passdigit.set(4)
        self.smallvar.set(1)
        self.numvar.set(1)

    
    def elements(self):
        Label(self.f1, text="Enter the No. of Digit ").grid(row=0, column=0)
        Entry(self.f1, textvariable=self.passdigit, width=5).grid(row=0, column=1)
        
        Label(self.root, text="Check if you Want !!").grid(row=1, column=0)

        Checkbutton(self.f2, text="Symbol",        variable=self.symbolvar, offvalue=0, onvalue=1).grid(row=0, column=0)
        Checkbutton(self.f2, text="Small Letters", variable=self.smallvar, offvalue=0, onvalue=1).grid(row=1, column=0)
        Checkbutton(self.f2, text="Caps Letters",  variable=self.capsvar, offvalue=0, onvalue=1).grid(row=2, column=0)
        Checkbutton(self.f2, text="Numbers",       variable=self.numvar, offvalue=0, onvalue=1).grid(row=3, column=0)

        Label(self.f3, textvariable=self.outpass).grid(row=0, column=0)
        
        Button(self.f4, text="Copy", command=self.copy, width=10).grid(row=0, column=0)
        Button(self.f4, text="Generate", command=self.caller, width=10).grid(row=0, column=1)
        Button(self.f4, text="Clear", command=self.clear, width=10).grid(row=0, column=2)
        




root=Tk()
root.geometry(None)
root.title("Password Generator")

aa=gui(root)
mainloop()
