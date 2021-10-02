a,b=0,1
print(a,b,end=" ")
for i in range(0,10):
    c=a+b
    a=b
    b=c
    print(c, end=" ")



x,y=0,1
print(x, end=' ')
while y<100:
    print(y, end=' ')
    x,y=y,x+y




x,y=0,1
print(x, end=' ')
for i in range(10):
    print(y, end=' ')
    x,y=y,x+y