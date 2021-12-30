#password generator
import random as r

class generatorclass :

    def askbygui(self,getlist):
        self.askq(2,getlist)
        reslist,rawlist,noofdigits=self.askq(2, getlist)
        returnlist=self.seperator(noofdigits, rawlist)
        password=self.passgen(returnlist)
        
        return password 

    def generator(self):
        noofdigit=0
        reslist,rawlist,noofdigits=self.askq(1, [])
        returnlist=self.seperator(noofdigit, rawlist)
        password=self.passgen(returnlist)
        print(password)
        
    def askq(self, option, getlist):
        if option==1:
            noofdigits=int(input("Enter the No. of digits: "))
            print("If you want put 1 otherwise 0...")
            symbols=int(input("Do You want SYMBOLS: "))
            small=int(input("Do You want SMALL LETTERS: "))
            caps=int(input("Do You want CAPS LETTERS: "))
            nums=int(input("Do You want NUMBERS: "))
            
        elif option==2:
            noofdigits=getlist[0]
            symbols=getlist[1]
            small=getlist[2]
            caps=getlist[3]
            nums=getlist[4]

        rawlist=[symbols,small,caps,nums]
        reslist=[]
        for i in rawlist:
            reslist.append(self.boolconverter(i))

        return reslist, rawlist, noofdigits

    def boolconverter(self, get):
        if get==1:
            return True
        elif get==0:
            return False

    def seperator(self, nodigits,rawlist):
        rawsum=sum(rawlist)
        equal=int(nodigits/rawsum)
        extra=int(nodigits%rawsum)
        
        smallcount=0
        capscount=0
        symbolcount=0
        numcount=0

        for i in range(0,len(rawlist)):
            if rawlist[i]==0:
                pass
            else:
                if i==0:
                    symbolcount+=equal
                elif i==1:
                    smallcount+=equal
                elif i==2:
                    capscount+=equal
                elif i==3:
                    numcount+=equal

        returnlist=[symbolcount, smallcount, capscount, numcount]

        for i in range(0,extra):
            while True:
                ran=r.randrange(0,4)
                if rawlist[ran]==0:
                    pass
                else:
                    break
            returnlist[ran]+=1


        return returnlist

    def passgen(self, getlist):
        symbol=['@', '#', '!', '$']
        small=[ 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        caps=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        nums=[ '1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

        totlist=[symbol, small, caps, nums]
        
        #symbolcount, smallcount, capscount, numcount= getlist[0], getlist[1], getlist[2], getlist[3]
        password=""

        while True:
            #totsum=symbolcount+smallcount+capscount+numcount
            totsum=sum(getlist)
            
            if totsum==0:
                break
            else:
                ran=r.randrange(0,4)
                #print(ran)
                if getlist[ran]==0:
                    continue
                elif not getlist[ran]==0:
                    getlist[ran]-=1
                    ran1=r.randrange(0,len(totlist[ran]))
                    passletter=totlist[ran][ran1]
                    password+=passletter

        return password
                    
            
    

a=generatorclass()


if __name__=="__main__":
    a.generator()




