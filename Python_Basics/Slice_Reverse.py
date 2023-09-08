'''a="Hello World"
d=a[:7]
print(d)

a="Hello World"
d=a[1:7]
print(d)

#reverse
rev="Hello"
rev1=rev[::-1]
print(rev1)

rev="Hello"
rev1=rev[::2]
print(rev1)'''

#parsing
data='from prasanna@gmail.com'
atpos=data.find('p')
print(atpos)
stpos=data.find('@')
print(stpos)
print(data[atpos:stpos])
print(data[atpos:atpos+3])

'''fruit='bananna'
print('a' in fruit)

if 'n' in fruit:
    print('Verified')

p='perfect'
print(p.upper(),p.lower())

p='    hello   '
print(p.strip())'''