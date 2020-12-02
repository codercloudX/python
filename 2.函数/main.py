from mutiply import mutiply
from swap import swap
x=10
y=6
z=mutiply(x,y)
print("%d * %d = %d" % (x,y,z),end="")

print()
x,y=swap(x,y)

print("x=%d  y=%d" % (x,y))