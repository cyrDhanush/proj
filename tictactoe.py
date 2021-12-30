import tkinter
from tkinter import *

root=Tk()
root.geometry(None)
root.title("Tic Tac Toe")
root.config(bg="#AB5EF3")

var1=StringVar()
var2=StringVar()
var3=StringVar()
var4=StringVar()
var5=StringVar()
var6=StringVar()
var7=StringVar()
var8=StringVar()
var9=StringVar()

playerlb=StringVar()
playerlb.set("X have to play")

i=2
count=0
index=0
value=[ "",  "",  "",  "",  "",  "",  "",  "",  "", ""]
winner=""


class ttt():

    def update(ind,p):
        global value
        value[ind]=p
        print(value)

    def check():
        global value
        global winner
        # ROW
        if value[1]==value[2]==value[3]=="X" or value[1]==value[2]==value[3]=="o":
            winner=value[1]
            
        elif value[4]==value[5]==value[6]=="X" or value[4]==value[5]==value[6]=="o":
            winner=value[4]
            
        elif value[7]==value[8]==value[9]=="X" or value[7]==value[8]==value[9]=="o":
            winner=value[7]
            
        # COLUMN
        
        elif value[1]==value[4]==value[7]=="X" or value[1]==value[4]==value[7]=="o" :
            winner=value[1] 
            
        elif value[2]==value[5]==value[8]=="X" or value[2]==value[5]==value[8]=="o":
            winner=value[2]
            
        elif value[3]==value[6]==value[9]=="X" or value[3]==value[6]==value[9]=="o":
            winner=value[3]
            
        # DIAGONAL
        
        elif value[1]==value[5]==value[9]=="X" or value[1]==value[5]==value[9]=="o":
            winner=value[1]
            
        elif value[3]==value[5]==value[7]=="X" or value[3]==value[5]==value[7]=="o":
            winner=value[3]
        else:
            global count
            count+=1
            if count==9:
                winner="Draw"
            print(count)

        if not winner == "":
            print(value[1],value[2],value[3])
            print(value[4],value[5],value[6])
            print(value[7],value[8],value[9])
            root.destroy()
            root1=Tk()
            root1.config(bg="black")
            root1.title(winner)
        #variables and widgets
            winner_char=StringVar()
            if winner=="Draw":
                winner="Draw"
            else:
                winner="The winner is Player {}".format(winner)
            winner_char.set(winner)
            winnerlabel=Label(root1, textvariable=winner_char, bg="black", fg="white")
            quitbutton=Button(root1, text="QUIT", command= root1.destroy, bg="black", fg="white")
        #ui
            winnerlabel.grid(row=0,column=0)
            quitbutton.grid(row=1,column=0)

        
       
        
        
    def playerchoose(index):
        global i
        print(index)
        if i%2==0:
            player="X"
            playeri="X"
            
        else:
            player="o"
            playeri="O"
        i+=1

        

        if index==1:
            b1["state"]=DISABLED
            var1.set(playeri)
            ttt.update(index,player)
        elif index==2:
            b2["state"]=DISABLED
            var2.set(playeri)
            ttt.update(index,player)
        elif index==3:
            b3["state"]=DISABLED
            var3.set(playeri)
            ttt.update(index,player)
        elif index==4:
            b4["state"]=DISABLED
            var4.set(playeri)
            ttt.update(index,player)
        elif index==5:
            b5["state"]=DISABLED
            var5.set(playeri)
            ttt.update(index,player)
        elif index==6:
            b6["state"]=DISABLED
            var6.set(playeri)
            ttt.update(index,player)
        elif index==7:
            b7["state"]=DISABLED
            var7.set(playeri)
            ttt.update(index,player)
        elif index==8:
            b8["state"]=DISABLED
            var8.set(playeri)
            ttt.update(index,player)
        elif index==9:
            b9["state"]=DISABLED
            var9.set(playeri)
            ttt.update(index,player)
       

        if player=="X":
            playerlb.set("O have to play")
        else:
            playerlb.set("X have to play")
    
            
    def changeit(index):
        ttt.playerchoose(index)
        ttt.check()

bgcolor1="#0066ff"
bgcolor="#00a6ff"
color="black"


b1=Button(root,text="",border=1,height=4,width=8,textvariable=var1,command=lambda:ttt.changeit(1), bg=bgcolor1, fg="#ffffff", font=100, disabledforeground=color)
b2=Button(root,text="",border=1,height=4,width=8,textvariable=var2,command=lambda:ttt.changeit(2), bg=bgcolor , fg="#ffffff", font=100, disabledforeground=color)
b3=Button(root,text="",border=1,height=4,width=8,textvariable=var3,command=lambda:ttt.changeit(3), bg=bgcolor1, fg="#ffffff", font=100, disabledforeground=color)
b4=Button(root,text="",border=1,height=4,width=8,textvariable=var4,command=lambda:ttt.changeit(4), bg=bgcolor , fg="#ffffff", font=100, disabledforeground=color)
b5=Button(root,text="",border=1,height=4,width=8,textvariable=var5,command=lambda:ttt.changeit(5), bg=bgcolor1, fg="#ffffff", font=100, disabledforeground=color)
b6=Button(root,text="",border=1,height=4,width=8,textvariable=var6,command=lambda:ttt.changeit(6), bg=bgcolor , fg="#ffffff", font=100, disabledforeground=color)
b7=Button(root,text="",border=1,height=4,width=8,textvariable=var7,command=lambda:ttt.changeit(7), bg=bgcolor1, fg="#ffffff", font=100, disabledforeground=color)
b8=Button(root,text="",border=1,height=4,width=8,textvariable=var8,command=lambda:ttt.changeit(8), bg=bgcolor , fg="#ffffff", font=100, disabledforeground=color)
b9=Button(root,text="",border=1,height=4,width=8,textvariable=var9,command=lambda:ttt.changeit(9), bg=bgcolor1, fg="#ffffff", font=100, disabledforeground=color)

lbl=Label(root,textvariable=playerlb, fg="white", bg="#AB5EF3")
made=Label(root, text="By Dhanush", bg="#AB5EF3", fg="white").grid(row=3,column=2)

b1.grid(row=0,column=0)
b2.grid(row=0,column=1)
b3.grid(row=0,column=2)
b4.grid(row=1,column=0)
b5.grid(row=1,column=1)
b6.grid(row=1,column=2)
b7.grid(row=2,column=0)
b8.grid(row=2,column=1)
b9.grid(row=2,column=2)
lbl.grid(row=3,column=1)

mainloop()
