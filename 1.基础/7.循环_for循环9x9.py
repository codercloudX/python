end=10
start=0
for i in range(start,end):
    for j in range(1,i+1):
      print("%d * %d = %d" % (j,i,i*j),end="\t")#不换行
    print()