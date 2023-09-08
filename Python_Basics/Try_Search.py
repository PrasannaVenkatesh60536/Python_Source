try:
    k=open("D:\Python\Data_Struct\demo.txt")
except:
    print('Cannot open the file')
    quit()

count=0
for i in k:
    if i.startswith('p'):
        count = count+1
print(count)
