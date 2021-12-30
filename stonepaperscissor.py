import tkinter
import random
from tkinter import *

root=Tk()
root.geometry(None)
root.title("Stone Paper Scissor")

butframe=Frame(root)
resultframe=Frame(root)
modeframe=Frame(root)

butframe.grid(row=0, column=0)
resultframe.grid(row=1, column=0)
modeframe.grid(row=2, column=0)

####### Variables

playerscore=0
compscore=0
target=0


####### tk variables

resultvar=StringVar()
targetvarlbl=StringVar()
statusvar=StringVar()
targetvar=IntVar()
targetvar.set(0)

#######

if target==0:
    targetvarlbl.set("Infinite")
        

class caller:
    def getinfo(self, choice):
        global playerscore, compscore
        c1=choice
        c2=random.randrange(1,4)
        res=s.check(c1, c2)
        
        if res==0:
            a="Draw"
            pass
        elif res==1:
            playerscore+=1
            a="Player"
        elif res==2:
            a="Computer"
            compscore+=1
            
        statusvar.set(a)

        s.fillscore()

        if target==0:
            pass
        else:
            s.checktarget()
        

    def fillscore(self):
        global playerscore, compscore
        
        string="Player: {}\nComputer: {}".format(str(playerscore), str(compscore))
        
        resultvar.set(string)

        
        
        
        
    def check(self, p1, p2):
        if p1 == p2 :
            return 0
        elif (p1==1 and p2==3) or (p1==3 and p2==2) or (p1==2 and p2==1) :
            return 1
        elif (p1==2 and p2==3) or (p1==3 and p2==1) or (p1==1 and p2==2):
            return 2

    def checktarget(self):
        global target, playerscore, compscore

        if playerscore>=target:
            winner="Player"
            a.newwincaller(winner)
        elif compscore>=target:
            winner="Computer"
            a.newwincaller(winner)
        elif compscore==target==player:
            winner="Draw"
            a.newwincaller(winner)
        
        else:
            pass

    def settarget(self):
        global target, playerscore, compscore
        target=targetvar.get()

        if target<playerscore and target<compscore:
            targetvarlbl.set("Target is less than score")
        else:
            if target==0:
                targetvarlbl.set("Infinite")
            else:
                targetvarlbl.set("Score Target: {}".format(target))

    def setinfinite(self):
        global target
        target=0
        targetvar.set(target)
        targetvarlbl.set("Infinite")
        
    def complete(self):
        global playerscore, compscore

        if playerscore>compscore:
            winner="Player"
        elif playerscore<compscore:
            winner="Computer"
        elif playerscore==compscore:
            winner="Draw"
        a.newwincaller(winner)

    def reset(self):
        statusvar.set("")
        resultvar.set("")
        s.setinfinite()

        global playerscore, compscore
        playerscore=0
        compscore=0
        

        


class newwin():
    def newwincaller(self, winner):
        root.destroy()
        
        window=Tk()
        window.geometry(None)
        window.title("::::: Congratulations :::::")

        if winner=="Draw":
            strr="Draw"
        else:
            strr="{} won the match".format(winner)
        lbl=Label(window, text=strr).grid(row=0, column=0)
        
        
        
        
s=caller()
a=newwin()

stonebut=Button(butframe, text="Stone", width=15, command=lambda:s.getinfo(1)).grid(row=0, column=0)
paperbut=Button(butframe, text="Paper", width=15, command=lambda:s.getinfo(2)).grid(row=1, column=0)
scissorbut=Button(butframe, text="Scissor", width=15, command=lambda:s.getinfo(3)).grid(row=2, column=0)

resultboard=Label(resultframe, text="", textvariable=resultvar).grid(row=0, column=0)
targetlbl=Label(resultframe, text="", textvariable = targetvarlbl).grid(row=1, column=0)
statuslbl=Label(resultframe, text="", textvariable = statusvar).grid(row=2, column=0)

targetentry=Entry(modeframe, width=18, textvariable=targetvar).grid(row=0, column=0)
targetbut=Button(modeframe,   text="Set Target",   width=15, command=s.settarget).grid(row=1, column=0)
infinitebut=Button(modeframe, text="Set Infinite", width=15, command=s.setinfinite).grid(row=2, column=0)
combut=Button(modeframe,      text="Complete",     width=15, command=s.complete).grid(row=1, column=1)
resetbut=Button(modeframe,    text="Reset",        width=15, command=s.reset).grid(row=2, column=1)


mainloop()
