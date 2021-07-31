f=open("1.txt","r")
print(type(f))
f.read()
f.close()
with open('1.txt', 'r') as f:
    print(f.read())
with open('1.txt', 'w') as f:
    f.write("hello,world")
with open('1.txt', 'a') as f:
    f.write("hello,python")