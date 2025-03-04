import random
'''
1:- Rock
2:- Paper
3:- Scissors

'''
a=random.choice([1,2,3])
b=input("Enter r for rock, s for scissors and p for paper")
s={"r":1,"p":2,"s":3}
rs={1:"ROCK",2:"PAPER",3:"SCISSORS"}
c=s[b]
print(f"Computer choosed {rs[a]}, you choosed {rs[c]}")
if(a==c):print("DRAW")
elif((c==1 and a==2) or (c==2 and a==3) or (c==3 and a==1)):print("LOST")
else:print("VICTORY")