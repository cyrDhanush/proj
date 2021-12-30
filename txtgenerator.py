import pyperclip 
import tkinter
from tkinter import *
from tkinter import messagebox



root=Tk()
root.geometry(None)
root.title("Welcome")

alphabet=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
notinlist=[]
strfinal=""
### variable
namevar=StringVar()
statusvar=StringVar()
###



class alpha:
    def alphab(self, string):
        finalstring=""
        for i in string:
            if i=='a':
                var="AAAAA\nA   A\nAAAAA\nA   A\nA   A"
                finalstring=finalstring + "\n\n" + var
                
            elif i in 'b':
                var="BBBBB\n B  B\n BBBB\n B  B\nBBBBB"
                finalstring=finalstring + "\n\n" + var
            elif i in 'c':
                var="CCCCC\nC    \nC    \nC    \nCCCCC"
                finalstring=finalstring + "\n\n" + var

            elif i in 'd':
                var="DDDDD\n D  D\n D  D\n D  D\nDDDDD"
                finalstring=finalstring + "\n\n" + var

            elif i in 'e':
                var="EEEEE\nE    \nEEEEE\nE    \nEEEEE"
                finalstring=finalstring + "\n\n" + var

            elif i in 'f':
                var="FFFFF\nF    \nFFFF \nF    \nF    "
                finalstring=finalstring + "\n\n" + var

            elif i in 'g':
                var="GGGGG\nG    \nG G G \nG G G \nGGG G"
                finalstring=finalstring + "\n\n" + var

            elif i in 'h':
                var="H   H\nH   H\nHHHHH\nH   H\nH   H"
                finalstring=finalstring + "\n\n" + var
                
            elif i in 'i':
                var="IIIII\n  I  \n  I  \n  I  \nIIIII"
                finalstring=finalstring + "\n\n" + var

            elif i in 'j':
                var="JJJJJ\n  J  \n  J  \n  J  \nJJJ  "
                finalstring=finalstring + "\n\n" + var

            elif i in 'k':
                var="K  K  \nK K   \nKK    \nK K\nK  K  "
                finalstring=finalstring + "\n\n" + var

            elif i in 'l':
                var="L    \nL    \nL    \nL    \nLLLLL"
                finalstring=finalstring + "\n\n" + var

            elif i in 'm':
                var="M   M\nMM MM\nM M M\nM   M\nM   M"
                finalstring=finalstring + "\n\n" + var

            elif i in 'n':
                var="N   N\nNN  N\nN N N\nN  NN\nN   N"
                finalstring=finalstring + "\n\n" + var

            elif i in 'o':
                var="OOOOO\nO   O\nO   O\nO   O\nOOOOO"
                finalstring=finalstring + "\n\n" + var

            elif i in 'p':
                var="PPPPP\nP   P\nPPPPP\nP    \nP    "
                finalstring=finalstring + "\n\n" + var

            elif i in 'q':
                var="QQQQQ\nQ   Q\nQ Q Q\nQQQQQ\n    Q"
                finalstring=finalstring + "\n\n" + var

            elif i in 'r':
                var="RRRRR\nR   R\nRRR  \nR  R  \nR   R"
                finalstring=finalstring + "\n\n" + var

            elif i in 's':
                var="SSSSS\nS    \nSSSSS\n    S\nSSSSS"
                finalstring=finalstring + "\n\n" + var

            elif i in 't':
                var="TTTTT\n  T  \n  T  \n  T  \n  T  "
                finalstring=finalstring + "\n\n" + var

            elif i in 'u':
                var="U   U\nU   U\nU   U\nU   U\nUUUUU"
                finalstring=finalstring + "\n\n" + var

            elif i in 'v':
                var="V   V\nV   V\nV   V\n V V \n  V  "
                finalstring=finalstring + "\n\n" + var

            elif i in 'w':
                var="W   W\nW   W\nW W W\nWW WW\nW   W"
                finalstring=finalstring + "\n\n" + var

            elif i in 'x':
                var="X   X\n X X \n  X  \n X X \nX   X"
                finalstring=finalstring + "\n\n" + var

            elif i in 'y':
                var="Y   Y\n Y Y \n  Y  \n  Y  \n  Y  "
                finalstring=finalstring + "\n\n" + var

            elif i in 'z':
                var="ZZZZZ\n   Z \n  Z  \n Z   \nZZZZZ"
                finalstring=finalstring + "\n\n" + var

            else:
                print(i)
                pass
        return finalstring



class classs:

    def check(self, getname):
        global notinlist, alphabet
        
        for i in getname:
            if i in alphabet:
                pass
            elif not i in alphabet:
                notinlist.append(i)
        if len(notinlist)==0:
            return True
        else:
             return False

    def start(self):
        global notinlist, strfinal
        notinlist.clear()
        
        strname=namevar.get()
        strname=strname.lower()
        if strname=="":
            statusvar.set("Enter any String")
        else:
            result=g.check(strname)
            if result is True:
                strfinal=a.alphab(strname)
                statusvar.set("Generated Succesfully")
                print(strfinal)
            elif result is False:
                stringg=""
                for b in notinlist:
                    stringg+=("\""+b+"\" ")
                
                messagebox.showerror("::::: AVOID :::::","Not fully generated: Try to avoid {}".format(stringg))
                
                statusvar.set("NOT Generated")


    def copy(self):
        pyperclip.copy(strfinal)
        statusvar.set("Copied")

    def clear(self):
        namevar.set("")
        statusvar.set("")
        strfinal=""
        

g=classs()
a=alpha()

frame1=Frame(root)
frame1.grid(row=0,column=0)

frame2=Frame(root)
frame2.grid(row=2, column=0)


labell=Label(frame1, text="String").grid(row=0, column=0)
nameent=Entry(frame1, textvariable=namevar, width=10).grid(row=0, column=1)
statuslbl=Label(root, textvariable=statusvar).grid(row=1, column=0)

genbut=Button(frame2, text="Generate", command=g.start, width=10).grid(row=0, column=0)
copybut=Button(frame2, text="Copy", command=g.copy, width=10).grid(row=1, column=0)
clearbut=Button(frame2, text="Clear", command=g.clear, width=10).grid(row=2, column=0)

mainloop()
