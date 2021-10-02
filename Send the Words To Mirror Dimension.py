name=input("enter the string to reverse: ")
name=list(name)
name.reverse()
name=''.join(name)
print(name)


name=input("enter the string to reverse: ")
name=list(name)
name=name[::-1]
name=''.join(name)
print(name)



string=(input('enter the string to be reversed: '))
reverse=''
for i in string:
    reverse=i+reverse
print(reverse)