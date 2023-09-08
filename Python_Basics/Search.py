i=open("D:\Python\Data_Struct\demo.txt")
for k in i:
    k=k.rstrip()
    if k.startswith("Pr"):
        continue
    print(k)

