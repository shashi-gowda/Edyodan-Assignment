numbers=(1, 2, 3, 4, 5, 6, 7, 8, 9)
a,b=0,0
for num in numbers:
    if num%2==0:
        a+=1
    else:
        b+=1
print('even numbers are: ',a)
print('odd numbers are: ',b)