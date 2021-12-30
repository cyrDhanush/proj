### __variables__   tossresult, playerwicket, playername

import random
import tkinter
from tkinter import *
from tkinter import messagebox

firstwin=Tk()
firstwin.geometry(None)
firstwin.title("Toss")

frame1=Frame(firstwin)
frame1.grid(row=0, column=0)

teem=Frame(frame1)
wicketframe=Frame(frame1)

tossframe=Frame(firstwin)
choiceframe=Frame(tossframe)

choiceframe.grid(row=2, column=0, pady=10)
teem.grid(row=0, column=0, padx=10)
wicketframe.grid(row=0, column=1)
tossframe.grid(row=1, column=0)

########

teemnamevar=StringVar()
tosservar=StringVar()
playervar=IntVar()
playervar.set("")

#######

tosslist=["Batting", "Bowling"]
tossstr=""
noplayers=0
tossok=""

########

def toss():
    global tosslist, tossstr
    global tossok

    tb["state"]=DISABLED
    tos=random.randrange(0,2)
    if tos==0:
        tossstr=tosslist[random.randrange(0,2)]
        tosservar.set(tossstr)
        tossok="ok"
        print("1")
    elif tos==1:
        bat["state"]=NORMAL
        bowl["state"]=NORMAL
        print("2")
        
        
        

        
    
    

def touch(getinfo):
    global tossstr, tossok
    if getinfo==1:
        tossstr="Batting"
    elif getinfo==2:
        tossstr="Bowling"
    
    tosservar.set(tossstr)
    tossok="ok"
    
    
        
    
    

def confirm():
    global tossstr, noplayers
    global tossok

    global tossresult, playerwicket, playername, openvar

    try:
        if playervar.get()<=0:
            noplayers=1
        else:
            noplayers=playervar.get()
        status="ok"
    except:
        messagebox.showerror("Sorry", "Enter the no of \nPlayers in your Teem")

    if teemnamevar.get()=="":
        messagebox.showerror("Sorry", "Enter your teem name")
    else:
        st1="ok"
        
    if status=="ok" and tossok=="ok" and st1=="ok":
        tossresult=tossstr
        playerwicket=noplayers
        playername=(teemnamevar.get()).capitalize()
        openvar="ok"
        firstwin.destroy()

        print(tossresult,playerwicket,playername,sep="\n")
    else:
        ##warning
        
        messagebox.showerror("Sorry", "Click Toss to Continue")
        
##
teemnamelbl=Label(teem, text="Name of \nYour Teem")
teemnameentry=Entry(teem, textvariable=teemnamevar)

teemnamelbl.grid(row=0, column=0)
teemnameentry.grid(row=1, column=0)
##
wicketlbl=Label(wicketframe, text="No. of players\nin your teem")
wicketentry=Entry(wicketframe, textvariable=playervar)

wicketlbl.grid(row=0, column=0)
wicketentry.grid(row=1, column=0)
##
tosslbl=Label(tossframe, textvariable=tosservar)
tb=Button(tossframe, text="Toss", command=toss, width=11)

tosslbl.grid(row=0, column=0)
tb.grid(row=1, column=0)
##
bat=Button(choiceframe, text="Batting", command=lambda: touch(1), state=DISABLED)
bowl=Button(choiceframe, text="Bowling", command=lambda: touch(2), state=DISABLED)

bat.grid(row=0, column=0)
bowl.grid(row=0, column=1)
##
confirmbut=Button(firstwin, text="Confirm", command=confirm, width=11)
confirmbut.grid(row=3, column=0)
##
mainloop()
