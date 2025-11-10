

print("This is the GAME OF NIM 🐉 🐉 🐉 ")
def play(check):
    caves=[]
    num=int(input("Enter the number caves"))
    if num<=0:
        print("Cannot be less than 1, game ends")
        quit()
    i=0
    while i<num:
        g=int(input(f"Enter the number of dragon in the cave number-{(i+1)}: "))
        if g<=0:

            print("There cannot be 0 or less dragons")
            continue

        caves.append(g)
        i+=1
    print("Bot Decides when to play")
    global s
    s=caves[0]


    b=0
    first=0
    def update(s):
        s = caves[0]
        i = 1
        while i < len(caves):
            s = s ^ caves[i]
            i += 1
        return s

    s=update(s)
    if check=='n':
        if s==0:
            print("Bot Wants to play first")
            first+=1
        elif s!=0:
            print("Bot Wants to play second")
            first+=2
    elif check=='y':
        if s!=0:
            print("Bot Wants to play first")
            first+=1
        elif s==0:
            print("Bot Wants to play second")
            first+=2



    kill=0
    Cavenum=0
    def killFunc(s):
        k=0

        for i in caves:
            if i^s<i:
                kill=i - (i^s)
                while k<len(caves):

                    if caves[k]==i:
                        Cavenum=k
                        break
                    k+=1
                # dragons[cave_num] = dragon[cave_num] - kill
                break
            else:
                Cavenum=0
                for i in caves:
                    if i!=0:

                        kill=1
                        Cavenum=caves.index(i)
                        break



        return kill, Cavenum

    def Prnt():
        i=0
        while i<len(caves):

            k=1
            print(f"Total Dragons in Cave No. {i+1}-> {caves[i]}:   ", end="")
            while k<=caves[i]:
                print("🐉 ",end="")

                k+=1

            print()
            i+=1
    v=0
    Prnt()

    def check(v):
        if caves==[0]*len(caves):
            if len(caves)==1 or len(caves)==0:
                print("Bot Wins")
                quit()
            if v == 2:
                print("Bot Wins")
                quit()
            elif v == 1:
                print("Player Wins")
                quit()
        else:
            return
    def playerRep():
        print("That's not possible, Try again")
        a=int(input("How many dragons do you want to kill, Human"))
        b=int(input("Which cave, Human"))
        b=b-1
        return a,b


    while caves!=[0]*len(caves):

        if first==1:
            print("Bot's Turn")
            x1,x2=killFunc(s)


            print(f"The Bot Has Killed {x1} dragons ",end="")
            print(f"From Cave Number {x2+1}")
            if caves[x2] - x1 < 0 or caves[x2]==0:
                print("Not possilbe, Bot plays again!")
                continue

            else:
                caves[x2] = caves[x2] - x1

                check(v)
                Prnt()
                print("\n")
                s = update(s)
            v = 1#player's turn
            y1 = int(input("How many dragons do you want to kill, Human"))
            y2 = int(input("Which cave, Human"))
            y2=y2-1
            if caves[y2] - y1 < 0:
                while caves[y2]- y1<0:
                    y1,y2=playerRep()
                    continue
            if y1 == 0:
                print("Trying to be Sneaky?")
                y1, y2 = playerRep()

            if y2 < 0:
                print("Thats not a bug in this code")
                y1, y2 = playerRep()

            caves[y2] = caves[y2] - y1
            check(v)
            s = update(s)
            Prnt()
            print("\n")
            v = 2 #Next turn is bot's
            continue
        elif first==2:
            y1 = int(input("How many dragon do you want to kill, Human"))
            y2 = int(input("Which cave, Human"))
            y2 = y2 - 1
            if caves[y2] - y1 < 0:
                while caves[y2] - y1 < 0:
                    y1, y2 = playerRep()
                    continue
            if y1==0:
                print("Trying to be Sneaky?")
                y1, y2 = playerRep()

            if y2<0:
                print("Thats not a bug in this code")
                y1, y2 = playerRep()

            caves[y2] = caves[y2] - y1
            check(v)
            s = update(s)
            Prnt()
            print("\n")

            v = 2#bot's turn

            print("Bot's Turn")
            x1, x2 = killFunc(s)

            print(f"The Bot Has Killed {x1} dragons ", end="")
            print(f"From Cave Number {x2 + 1}")
            if caves[x2] - x1 < 0 or caves[x2] == 0:
                print("Not possible, Bot plays again!")
                continue

            else:
                caves[x2] = caves[x2] - x1

                check(v)
                Prnt()
                print("\n")
                s = update(s)
                v = 1  # player's turn is next
            continue
    #if value of v is 2, then it means that bot will play next. If one, then it means player will play next
print("You will need to enter an amount of caves")
print("In each cave, you will need to enter an amount of dragons")
print("When its your chance, you need to kill some amount of dragons from 1 of the caves")
print("The one to kill the last dragon wins!")
print("Impossible level: Very hard to beat. Wins almost all the times")
print("Hard level - Easier to beat, but one mistake might cost you")
check = ""
while not(check=='n' or check=='y'):
    check=input("Do you want to play the impossible level or not?, 'y' for yes and 'n' for no")
if check=='n':
    play(check)
elif check=='y':
    play(check)




