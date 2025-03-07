import random
a=random.randint(1,100)
guess=0
n=-1
while(a!=n):
    
    n=int(input("Guess the number "))
    if(n>a):
        print("Lower number please")
        guess+=1
    elif(n<a):
        print("Higher number please")
        guess+=1
print(f"You guessed the answer correctly in {guess} attempts")
