import tkinter
from tkinter import *

class ui:

    def __init__(self, root):
        self.root=root
        
        self.frametxtbox=Frame(root)
        self.keypad=Frame(root)
        self.numpad=Frame(self.keypad)
        self.sidebig=Frame(self.keypad)

        self.frametxtbox.grid(row=0, column=0)
        self.keypad.grid(row=1, column=0)
        self.numpad.grid(row=0, column=0)
        self.sidebig.grid(row=0, column=1)

        self.variables()
        self.elements()
        
        
        
        

    def elements(self):

        numheight=2
        numwidth=5
        sidewidth=numwidth
        sideheight=3

        
        Entry(self.frametxtbox, textvariable= self.textboxvar).grid(row=0, column=0)

        Button(self.numpad, text="-", command=lambda: self.numberbut("-"), height=numheight, width=numwidth).grid(row=0, column=0 )
        Button(self.numpad, text="*", command=lambda: self.numberbut("*"), height=numheight, width=numwidth).grid(row=0, column=1 )
        Button(self.numpad, text="/", command=lambda: self.numberbut("/"), height=numheight, width=numwidth).grid(row=0, column=2 )
        
        Button(self.numpad, text="7", command=lambda: self.numberbut("7"), height=numheight, width=numwidth).grid(row=1, column=0 )
        Button(self.numpad, text="8", command=lambda: self.numberbut("8"), height=numheight, width=numwidth).grid(row=1, column=1 )
        Button(self.numpad, text="9", command=lambda: self.numberbut("9"), height=numheight, width=numwidth).grid(row=1, column=2 )
        Button(self.numpad, text="4", command=lambda: self.numberbut("4"), height=numheight, width=numwidth).grid(row=2, column=0 )
        Button(self.numpad, text="5", command=lambda: self.numberbut("5"), height=numheight, width=numwidth).grid(row=2, column=1 )
        Button(self.numpad, text="6", command=lambda: self.numberbut("6"), height=numheight, width=numwidth).grid(row=2, column=2 )
        Button(self.numpad, text="1", command=lambda: self.numberbut("1"), height=numheight, width=numwidth).grid(row=3, column=0 )
        Button(self.numpad, text="2", command=lambda: self.numberbut("2"), height=numheight, width=numwidth).grid(row=3, column=1 )
        Button(self.numpad, text="3", command=lambda: self.numberbut("3"), height=numheight, width=numwidth).grid(row=3, column=2 )
        Button(self.numpad, text="0", command=lambda: self.numberbut("0"), height=numheight, width=numwidth).grid(row=4, column=0 )
        
        Button(self.numpad, text=".", command=lambda: self.numberbut("."), height=numheight, width=numwidth).grid(row=4, column=1 )
        Button(self.numpad, text="<-", command=self.backspace, height=numheight, width=numwidth).grid(row=4, column=2 )

        Button(self.sidebig, text="+", command=lambda: self.numberbut("+"), height=sideheight, width=sidewidth).grid(row=0, column=0)
        Button(self.sidebig, text="C", command= self.allclear, height=sideheight, width=sidewidth).grid(row=1, column=0)
        Button(self.sidebig, text="Equal", command=self.equalbut, height=sideheight, width=sidewidth).grid(row=2, column=0)

    def variables(self):

        self.textboxvar=StringVar()

    def numberbut(self, number):
        a=self.textboxvar.get()
        res=a+number
        exceptt=["+","-","*","/","."]
        if number not in exceptt:
            resstring=self.check(res)
        else:
            resstring=res
        self.textboxvar.set(resstring)

    def check(self, string):
        operators=["+","-","*","/"]
        if int(string[len(string)-1])==0 and string[len(string)-2] in operators:
            print("runned")
            string=string[:len(string)-1]
        return string

    def equalbut(self):
        cal=self.textboxvar.get()
        self.textboxvar.set("")
        self.textboxvar.set(eval(cal))

    def backspace(self):
        string=self.textboxvar.get()
        resstring=string[:len(string)-1]
        self.textboxvar.set(resstring)
        

    def allclear(self):
        self.textboxvar.set("")
        
    

        

         
        

root=Tk()
root.geometry(None)
a=ui(root)



mainloop()
