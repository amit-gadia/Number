import random
b=random.randint(1,100)
con=True
c=0
d=1
print("Choose Number Between 1 To 100 \n3 Chance Left")
a=int(input())
while(con==True and c<3):
    if(a==b):
        print("Guess Successfully "+str(b) )
        d=1
        con=False
    else:
        print("Retry...\n"+str(2-c)+" Chance Left ")
        if(a>b):
            print(str(a)+" Number is Greater")
        else:
            print(str(a)+" Number is Smaller")
        if(c<2):
            a=int(input())
        c=c+1
        d=0
if(d==0):
    print("Not Guess "+str(b))
