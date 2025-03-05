# with open ("file.txt") as f:
#     c=f.read()
#     if(c.find("Twie")!=-1):
#         print("FOUND")
#     else:print("NOT FOUND")

# def generate(n):
#     table=""
#     for i in range(1,11):
#         table+=f"{n} X {i} = {n*i}\n"
#     with open(f"python/ch9ps/table_{n}","w") as f:
#         f.write(table)

# for i in range (2,21):
#     generate(i)

# word="donkey"
# with open("python/ch9ps/donkey.txt","r") as  f:
#     content=f.read()
# contentNew=content.replace(word,"RIYA")
# with open("python/ch9ps/donkey.txt","w") as f:
#     f.write(contentNew)

words=["DONKEY", "RIYA", "PK", "NANAOP", "GANDA"]
with open("python/ch9ps/donkey.txt","r") as  f:
    content=f.read()
for word in words:
    content=content.replace(word,"*"*len(word))

with open("python/ch9ps/donkey.txt","w") as f:
    f.write(content)