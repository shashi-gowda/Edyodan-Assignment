a,b=0,1
print(a,b,end=" ")
for i in range(0,8):
    c=a+b
    a=b
    b=c
    print(c, end=" ")
