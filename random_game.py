import random
print("WELCOME TO THE GAME WORLD")
a=input("R U A BEGINNER?")
a=a.lower()
if a=="yes":
    s=10
    s=int(s)
    print("FOR A BETTER EXPERIENCE 10$ ARE PROVIDED FOR U")
else:
    s=int(input("how much amount do u have?"))

while True:
    n=int(input("\nGuess a number between 0 to 5:"))
    if n<=5 and n>=0:
        r=random.randint(0,5)
    
        if s==0:
            print("!!insufficient balance!!!\n\nbetter next time")
            break
        elif r==n:
            s=s+1
            print("correct\nu have won 1 $\nnow u have "+str(s)+"$")
        elif s>=20:
            s=s+100
            print("GREAT JOB\n YOU HAVE WON 100$")
        else:
            s=s-1
            print("wrong\nu lost 1 $\nnow u have "+str(s)+"$")
    else:
        print("!!!invalid!!!")


