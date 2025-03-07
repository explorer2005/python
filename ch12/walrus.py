# if(n:=len([1,2,3,4,5,6,7,8,9]))>3:
#     print(f"The list is to long with {n} number of elements ")

# def matchcase(status):
#     match status:
#         case 200:
#             return "ok"
#         case 404:
#             return "error"
#         case _:
#             return "Unknown status"


# print(matchcase(404))

# duct1={"a":1,"b":2}
# duct2={"b":3,"c":4}
# print(duct1)
# print(duct2)
# merge1=duct1|duct2
# merge2=duct2|duct1
# print(merge1)
# print(merge2)

try:
    a=int(input("Enter a number "))
except Exception as e:
    print(e)