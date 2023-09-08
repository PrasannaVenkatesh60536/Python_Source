f=open("D:\Python\Data_Struct\demo.txt")
t=f.read()
print(len(t))
print(t[:5])
k=input("Enter the Single char=")
if k in t:
    print("Yes Authorized")
else:
    print("Not Applicable")

