#import questionspy as q

import sqlite3
import random
import tkinter
from tkinter import *

###### DATA BASE
##VAR
global dbque, dbop1, dbop2, dbop3,dbop4, dbans
dbque=[]
dbop1=[]
dbop2=[]
dbop3=[]
dbop4=[]
dbans=[]



#def data():
connection=sqlite3.connect("quepy.db")
cur=connection.cursor()
cur.execute("""select * from questions""")
tovar=cur.fetchall()
for a in range(len(tovar)):
    dbque.append(tovar[a][0])
    dbop1.append(tovar[a][1])
    dbop2.append(tovar[a][2])
    dbop3.append(tovar[a][3])
    dbop4.append(tovar[a][4])
    dbans.append(tovar[a][5])
#data()

######

root=Tk()
#root.geometry("270x480")
root.geometry(None)
root.title("MCQ's")

questionvar=StringVar()
optionvar1=StringVar()
optionvar2=StringVar()
optionvar3=StringVar()
optionvar4=StringVar()
ansvar=StringVar()


size=60
bgcl="#292929"
bgforopt="#595959"
bgforcons="#333333"

fore="white"

root.config(bg=bgcl)

#####rand

randomnumber=random.randrange(0, len(dbque))
randlist=[]
randlist.append(randomnumber)
qcount=0

#####

score=0
times=1

###Stats

ncorrect=0
nwrong=0
nskipped=0
nnotattended=0

wronglist=[]
skippedlist=[]
notattendedlist=list(range(0,len(dbque)))

###

qframe=Frame(root)
opframe=Frame(root)
lframe=Frame(root)

class quiz():

    def check(self, selectoption):
        global randomnumber
        
        i= randomnumber
        selectopt=selectoption
        
        if dbans[i]==selectopt:
            return True
        
        else:
            return False

    def receiveoption(self, ops):
        global score
        global ncorrect
        global nwrong
        global wronglist
        global notattendedlist
        global randomnumber
        i=randomnumber
        
        selectop=""
        
        if ops==1:
            selectop=optionvar1.get()
            
        elif ops==2:
            selectop=optionvar2.get()
            
        elif ops==3:
            selectop=optionvar3.get()
            
        elif ops==4:
            selectop=optionvar4.get()
            
        b=w.check(selectop)
        
        if b is True:
            ncorrect+=1
            score+=4
            notattendedlist.remove(i)
            
        elif b is False:
            nwrong+=1
            score-=1
            wronglist.append(i)
            notattendedlist.remove(i)
        

        w.randomcaller()

    def randomcaller(self):
        global randomnumber
        global randlist
        global times
        
        while True:
            ran=random.randrange(0, len(dbque))
            
            if times == len(dbque):
                w.finishcom()
                break
                
            else:
                
                if ran in randlist:
                    continue
                
                else:
                    randlist.append(ran)
                    randomnumber=ran
                    times+=1
                    break
        w.setter()

    def setter(self):
        global randomnumber
        global stra, strb, strc, strd
        global qcount
        
        
        i=randomnumber
        qvar=""
        qvar=dbque[i]
        count=1
        finala=""

        if len(qvar)>=40:
            
           for ins in qvar:
               
                if count>40 and ins==" ":
                    finala+=" \n"
                    count=1
                    
                else:
                    finala+=ins
                count+=1
        else:
            spaceneed=40-len(qvar)
            finala = qvar+(" " * spaceneed)



            

        lines = finala.count("\n")
        if not lines>=3:
            nt=3-lines
            finala+="\n"*nt
            
        ##
        randmlist=[]
        while True:
            randno=random.randrange(0,4)
            if randno in randmlist:
                continue
            else:
                randmlist.append(randno)
            if len(randmlist)==4:
                break
        a=randmlist[0]
        b=randmlist[1]
        c=randmlist[2]
        d=randmlist[3]
        
        oplist=[dbop1[i], dbop2[i], dbop3[i], dbop4[i] ]
        
       
       
        stra=oplist[a]
        strb=oplist[b]
        strc=oplist[c]
        strd=oplist[d]
        ##

        
            
        qcount+=1
        finala=str(qcount)+". "+finala

        questionvar.set(finala)
        optionvar1.set(stra)
        optionvar2.set(strb)
        optionvar3.set(strc)
        optionvar4.set(strd)

        
    def skipper(self):
        global randomnumber
        global randlist
        global nskipped
        global skippedlist
        global notattendedlist
        
        nskipped+=1
        randlist.append(randomnumber)
        skippedlist.append(randomnumber)
        notattendedlist.remove(randomnumber)
        w.randomcaller()

    def finishcom(self):
        global score
        global ncorrect
        global nwrong
        global nskipped
        global nnotattended

        #colours
        global bgcl
        global bgforopt
        global bgforcons
        global fore
        global size
        #

        nnotattended=len(dbque)-(ncorrect+nwrong+nskipped)

        score1=str(score)
        root.destroy()
        root1=Tk()
        root1.geometry(None)
        root1.title("Result")
        root1.config(bg= bgcl)

        statslbl=StringVar()
        statsvar="""CORRECT : {}\nWRONG : {}\nSKIPPED : {}\nNOT ATTENDED : {}""".format(ncorrect,nwrong,nskipped,nnotattended)
        statslbl.set(statsvar)

        scrframe=Frame(root1, bg=bgcl)
        statsframe=Frame(root1, bg=bgcl)
        consoleframe=Frame(root1, bg=bgcl)
        
        scrframe.grid(row=0, column=0)
        statsframe.grid(row=1, column=0)
        consoleframe.grid(row=2, column=0)

        scoretxt=StringVar()
        scoretxt.set("TOTAL SCORE : {} out of {}".format(score1, len(dbque)*4))

        scrlabel=Label(scrframe, textvariable=scoretxt, bg=bgcl, fg=fore, font=size)
        scrlabel.grid(row=0, column=0)

        
        
        ###
        lblsts=Label(statsframe, text="################ STATS ################", bg=bgcl, fg=fore, font=size)
        lblsts.grid(row=0, column=0)
        statslabel=Label(statsframe, textvariable=statslbl, bg=bgcl, fg=fore, font=size)
        statslabel.grid(row=1, column=0)
        ###
        
        def callroot2():
            global wronglist
            global skippedlist
            global notattendedlist
            ###colours
            
            global fore
            global bgforcons
            global bgcl

            ###

            size=50
            xsize=60
            
            

            wrongq=""""""
            
            skippedq=""""""
            
            notattendedq=""""""
            
            # wronglist
            n=1
            for call in range(0,len(wronglist)):
                i=wronglist[call]
                wrongq+="""Q {}: {}\nAns    : {}\n\n""".format(n, dbque[i], dbans[i])
                n+=1

            
            #skipped
            n=1
            for call in range(0,len(skippedlist)):
                i=skippedlist[call]
                skippedq+="""Q {}: {}\nAns    : {}\n\n""".format(n, dbque[i], dbans[i])
                n+=1

            #notattended
            n=1
            for call in range(0,len(notattendedlist)):
                i=notattendedlist[call]
                notattendedq+="""Q {}: {}\nAns    : {}\n\n""".format(n, dbque[i], dbans[i])
                n+=1

            
            
            root1.destroy()
            root2=Tk()
            root2.geometry(None)
            root2.title("#### ANSWERS ####")
            root2.config(bg= bgcl)

            misframe=Frame(root2, bg=bgcl)
            
            wrong=StringVar()
            skipped=StringVar()
            notatt=StringVar()

            wrong.set(wrongq)
            skipped.set(skippedq)
            notatt.set(notattendedq)
            
            lbl=Label(root2, text="######## PRACTICE MAKES A MAN PERFECT ########\n\n", bg=bgcl, fg=fore, font=xsize)

            if len(wronglist) >0:
                wronglbl1=Label(misframe, text="#### WRONG ####\n\n", bg=bgcl, fg=fore, font=xsize)
                wronglbl2=Label(misframe, textvariable=wrong, bg=bgcl, fg=fore, font=size )
                wronglbl1.grid(row=0, column=0)
                wronglbl2.grid(row=1, column=0)

            if len(skippedlist) >0:
                skippedlbl1=Label(misframe, text="#### SKIPPED ####\n\n", bg=bgcl, fg=fore, font=xsize)
                skippedlbl2=Label(misframe, textvariable=skipped, bg=bgcl, fg=fore, font=size )
                skippedlbl1.grid(row=2, column=0)
                skippedlbl2.grid(row=3, column=0)

            if len(notattendedlist) >0:
                notattlbl1=Label(misframe,  text="#### NOT ATTENDED ####\n\n", bg=bgcl, fg=fore, font=xsize)
                notattlbl2=Label(misframe, textvariable=notatt, bg=bgcl, fg=fore, font=size )
                notattlbl1.grid(row=4, column=0)
                notattlbl2.grid(row=5, column=0)
            
            finlbl=Label(root2, text="By Dhanush", bg=bgcl, fg=fore, font=size)
            closebutton=Button(root2, text="Close", command=root2.destroy, bg=bgforcons, fg=fore, font=size)
            

            
            
           

            
            lbl.grid(row=0, column=0)
            misframe.grid(row=1, column=0)
            closebutton.grid(row=2, column=0)
            finlbl.grid(row=3, column=0)

        if nskipped+nwrong+nnotattended>0:
            showbut=Button(consoleframe, text="Show mistakes", command=callroot2, bg=bgforcons, fg=fore, font=size)
            showbut.grid(row=0, column=0)
            
        
        closebut=Button(consoleframe, text="Close", command=root1.destroy, bg=bgforcons, fg=fore, font=size)
        closebut.grid(row=0, column=1)
        
        finlbl=Label(root1, text="By Dhanush", bg=bgforcons, fg=fore, font=size)
        finlbl.grid(row=3, column=0)

        

    
        
w=quiz()
w.setter()


qframe.grid(row=0, column=0)
opframe.grid(row=1, column=0)
lframe.grid(row=2, column=0)


quelabel=Label(qframe, textvariable=questionvar, bg=bgcl, fg=fore, font=size).grid(row=0, column=0)
option1=Button(opframe, textvariable=optionvar1, command=lambda: w.receiveoption(1), bg=bgforopt, border=3, fg=fore, width=20, font=size).grid(row=0, column=0)
option2=Button(opframe, textvariable=optionvar2, command=lambda: w.receiveoption(2), bg=bgforopt, border=3, fg=fore, width=20, font=size).grid(row=1, column=0)
option3=Button(opframe, textvariable=optionvar3, command=lambda: w.receiveoption(3), bg=bgforopt, border=3, fg=fore, width=20, font=size).grid(row=2, column=0)
option4=Button(opframe, textvariable=optionvar4, command=lambda: w.receiveoption(4), bg=bgforopt, border=3, fg=fore, width=20, font=size).grid(row=3, column=0)



close=Button(lframe, text="Close", command=root.destroy,  width=5, bg=bgforcons, fg=fore, font=size)
finish=Button(lframe, text="Finish", command=w.finishcom, width=5, bg=bgforcons, fg=fore, font=size)
skip=Button(lframe, text="Skip", command=w.skipper,       width=5, bg=bgforcons, fg=fore, font=size)
close.grid(row=0, column=0)
finish.grid(row=0, column=1)
skip.grid(row=0, column=2)

finlbl=Label(root, text="By Dhanush", bg=bgforcons, fg=fore, font=size)
finlbl.grid(row=3, column=0)



        



mainloop()





