try:
    import toss as t
except:
    print("Not found")
import random
import tkinter
from tkinter import *
from tkinter import messagebox

openvar="ok"
if t.openvar=="ok":

    root=Tk()
    root.geometry(None)
    root.title("Hand Cricket")

    statusframe=Frame(root)
    butframe=Frame(root)
    compframe=Frame(statusframe)
    playerframe=Frame(statusframe)

    compframe.grid(row=0, column=0)
    playerframe.grid(row=0, column=1)

    statusframe.grid(row=1, column=0)
    butframe.grid(row=2, column=0, padx=10)

    ######getting variables from toss

##    tossresult   = "Bowling"
##    playerwicket = 3
##    playername   = "CSK"


    tossresult   = t.tossresult
    playerwicket = t.playerwicket
    playername   = t.playername
    times=1
    playerscore=0
    compscore=0

    if tossresult=="Bowling":
        compplay="Batting"
        player="Bowling"
    elif tossresult=="Batting":
        compplay="Bowling"
        player="Batting"
        
    compwicket=playerwicket

    ######tkinter variable
    compstatus=StringVar()
    playerstatus=StringVar()
    
    compremplayer=StringVar()
    compremplayer.set("Remaining Players\n       --")
    
    playerremplayer=StringVar()
    playerremplayer.set("Remaining Players\n       --")
    
    compstw=StringVar()
    compstw.set("Scores to win\n      --")
    
    playerstw=StringVar()
    playerstw.set("Scores to win\n      --")
    
    compscorevar=StringVar()
    compscorevar.set("Current Score\n      --")
    
    playerscorevar=StringVar()
    playerscorevar.set("Current Score\n      --")

    compstatus.set(compplay)
    playerstatus.set(player)
    
    ######
    totalwicket=playerwicket
    ######
    class play:
        def getrun(self, getvalue):
            global times
            global compplay, player
            global playerscore, compscore
            global compwicket, playerwicket
            
            given=getvalue
            randd=s.compturn()
            ## first time
            if times==1:
                print("1st time")
                if player=="Batting":
                    if given==randd:
                        if playerwicket>=2:
                            playerwicket-=1
                        else:
                            playerwicket=0
                            times=2
                            s.changeplayer()
                    else:
                        playerscore+=given

                elif player=="Bowling":
                    if given==randd:
                        if compwicket>=2:
                            compwicket-=1
                        else:
                            compwicket=0
                            times=2
                            s.changeplayer()
                    else:
                        compscore+=randd
            #second time
            elif times==2:
                print("2nd time")
                if player=="Batting":
                    
                    if given==randd:
                        if playerwicket>1:
                            playerwicket-=1
                        else:
                            #complete game
                            playerwicket=0
                            s.complete()
                            pass
                    else:
                        playerscore+=given
                        if playerscore>compscore:
                            s.complete()
                        
                    playerstw.set("Scores to win\n      {}".format(str(compscore-playerscore)))
                    
                elif player=="Bowling":
                    
                    if given==randd:
                        if compwicket>1:
                            compwicket-=1
                        else:
                            #complete game
                            compwicket=0
                            s.complete()
                            pass
                    else:
                        compscore+=randd
                        if compscore>playerscore:
                            s.complete()
                        
                    playerstw.set("Scores to win\n      {}".format(str(playerscore-compscore)))
            ###
            compremplayer.set("Remaining Players\n       {}".format(str(compwicket)))
            playerremplayer.set("Remaining Players\n       {}".format(str(playerwicket)))
            compstatus.set(compplay)
            playerstatus.set(player)
            compscorevar.set("Current Score\n      {}".format(str(compscore)))
            playerscorevar.set("Current Score\n      {}".format(str(playerscore)))
            
            ###

                
                
        def changeplayer(self):
            global compplay, player

            if player=="Batting":
                player="Bowling"
                compplay="Batting"
            elif player=="Bowling":
                player="Batting"
                compplay="Bowling"
                
            
            
        def compturn(self):
            listt=[1,2,3,4,5,6,10,12]
            return listt[random.randrange(0,len(listt))]

        def complete(self):
            global compscore , playerscore

            if compscore>playerscore:
                #compwin
                s.resultt("Computer")
            elif playerscore>compscore:
                #playerwins
                s.resultt("Player")
            elif playerscore==compscore:
                #draw
                s.resultt("Draw")
            
                
        def resultt(self, winner):
            global compscore, playerscore
            
            root.destroy()
            window=Tk()
            window.geometry(None)
            window.title("Result")
            
            string=""

            if winner=="Player":
                string="$$$$ Congratulations $$$$ You WON the match by {} Runs".format(abs(compscore-playerscore))
                
            elif winner=="Computer":
                string="!!! Sorry !!! You LOST the match by {} Runs".format(abs(compscore-playerscore))

            elif winner=="Draw":
                string="WOW .. Its a Draw"

            Label(window, text=string).grid(row=0, column=0)
            Button(window, text="Close", command=window.destroy).grid(row=1, column=1, pady=50)
                
        
    s=play()
    ######
    
    Label(root, text="Total no. of Wickets: {}".format(totalwicket)).grid(row=0, column=0)

    ###compframe
    Label(compframe, text="Computer").grid(row=0, column=0)
    Label(compframe, textvariable=compstatus).grid(row=1, column=0)
    Label(compframe, textvariable=compremplayer).grid(row=2, column=0)
    Label(compframe, textvariable=compscorevar).grid(row=3, column=0)
    Label(compframe, textvariable=compstw).grid(row=4, column=0)
    ###playerframe
    Label(playerframe, text=playername).grid(row=0, column=0)
    Label(playerframe, textvariable=playerstatus).grid(row=1, column=0)
    Label(playerframe, textvariable=playerremplayer).grid(row=2, column=0)
    Label(playerframe, textvariable=playerscorevar).grid(row=3, column=0)
    Label(playerframe, textvariable=playerstw).grid(row=4, column=0)
    ###butframe
    Button(butframe, text="1" , height=3, width=6, command=lambda: s.getrun(1)).grid(row=0, column=0)
    Button(butframe, text="2" , height=3, width=6, command=lambda: s.getrun(2)).grid(row=0, column=1, padx=10)
    Button(butframe, text="3" , height=3, width=6, command=lambda: s.getrun(3)).grid(row=0, column=2)
    Button(butframe, text="4" , height=3, width=6, command=lambda: s.getrun(4)).grid(row=0, column=3, padx=10)
    Button(butframe, text="5" , height=3, width=6, command=lambda: s.getrun(5)).grid(row=1, column=0, pady=10)
    Button(butframe, text="6" , height=3, width=6, command=lambda: s.getrun(6)).grid(row=1, column=1, padx=10, pady=10)
    Button(butframe, text="10", height=3, width=6, command=lambda: s.getrun(10)).grid(row=1, column=2, pady=10)
    Button(butframe, text="12", height=3, width=6, command=lambda: s.getrun(12)).grid(row=1, column=3, padx=10, pady=10)
    ###
    
else:
    pass

mainloop()
