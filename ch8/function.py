# def hello():
#     a1=int(input("Enter the number 1 "))
#     a2=int(input("Enter the number 2 "))
#     a3=int(input("Enter the number 3 "))
#     print((a1+a2+a3)/3)
# hello()

# hello()
# hello()
# hello()
# hello()
# hello()
# def greet(name):
#     print("Good day, ",name)
# l=["DHRUV","RIYA","ESHA","ANKUSH"]
# for i in range (len(l)):
#     greet(l[i])
#     i=i+1

def greet(name,ending=name):
    print("Good day , ",name)
    print(ending)
    return "done"
a=greet("DHRUV")
print(a)
b=greet("DHRUV","RIYA")
print(b)