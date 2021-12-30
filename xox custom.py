class inputs:             ######## declaration ########
    def __init__(self,dimension,datalist) :
        self.dimension=dimension
        self.datalist=datalist
        self.declare()
        
    
    def declare(self):
        sublist=[]
        for i in range(0,self.dimension):
            for j in range(0,self.dimension):
                sublist.append("N")
            self.datalist.append(sublist)
            sublist=[]
    
    def returnn(self):
        return self.datalist
    
class getuser:             #########  getting input ##########
    def __init__(self,dimension,datalist) :
        self.dimension=dimension
        self.datalist=datalist
    
    def printer(self):
        listt=self.datalist
        length=len(listt[0])
        for n in range(0,len(listt[0])):

            i=listt[n]

            print("-"*((length*4)+1))
            print("| ", end="")

            for j in i:
                if j=="N":
                    var=" "
                else :
                    var=j
                print(var, end=" | ")
            print("\n")
        
        print("-"*((length*4)+1))

        ##for i in self.datalist:
        ##    print(i)
    
    def getinput(self, player):
        while True:
            self.printer()
            print(f"Turn for player: {player}")
            address_y=int(input("Enter the Address(1): "))
            address_x=int(input("Enter the Address(2): "))
            if hischeck(address_y,address_x)==True:
                self.datalist[address_x-1][address_y-1]=player
                break
            else:
                print("Already Entered. Please Try again")
                continue

winner=""  

def allrsame(listt):
    global winner
    length=len(listt)
    first=listt[0]
    flag=True
    for i in range(0,length):
        element=listt[i]
        if element==first and not first=="N":
            pass
        else:
            flag=False
            break
    if flag==True:
        winner=first
    return flag

def hischeck(x,y):
    global historylist
    if [x,y] in historylist:
        return False
    else:
        historylist.append([x,y])
        return True


def makereverse(listt):
    sublist=[]
    for i in range(len(listt)-1,-1,-1):
        sublist.append(listt[i])
    return sublist

class checker:            ######      checker       #########

    def __init__(self, dimension):
        self.dimension=dimension
        #self.datalist=datalist

    def checkrow(self):
        listt=self.datalist
        flag=False
        for i in listt:
            result=allrsame(i)
            if result==True:
                flag=True
                break
        return flag

    def checkcolumn(self):
        listt=self.datalist
        flag=False
        sublist=[]
        for i in range(0,len(listt)):
            for j in listt:
                sublist.append(j[i])
            result=allrsame(sublist)
            sublist=[]
            if result==True:
                flag=True
                break
        return flag

    def checkcross(self):
        size=self.dimension
        listt=self.datalist
        sublist=[]
        sublist2=[]
        reverselist=[]

        ### dimension 1 left to right
        for i in range(0,size):
            sublist.append(listt[i][i])
        ## return allrsame(sublist)

        ### dimension 2 right to left
        for j in listt:
            sublist2.append(makereverse(j))

        for i in range(0,size):
            reverselist.append(sublist2[i][i])
            
        #print(sublist2)
        return allrsame(sublist) or allrsame(reverselist)
        


    def check(self, datalist):
        self.datalist=datalist
        row=self.checkrow()
        column=self.checkcolumn()
        cross=self.checkcross()
        if cross or row or column:
            return True


dimension=int(input("Enter the Dimension (above 2): "))
datalist=[]
historylist=[]

inputobj=inputs(dimension,datalist)    #obj 1

datalist=inputobj.returnn()

userobj=getuser(dimension,datalist)      #obj 2
checkobj=checker(dimension)       #obj 3

playerid=1
while True:
    if playerid%2==0:
        userobj.getinput("X")

    else:
        userobj.getinput("O")

    result=checkobj.check(datalist)

    if result==True:
        userobj.printer()
        print(f"The winner is {winner}")
        break
    
    playerid+=1
print(datalist)
