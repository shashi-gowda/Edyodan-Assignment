# Write a Python program to triple all numbers of a given list of integers. Use Python map.

sample_List=[1, 2, 3, 4, 5, 6, 7]
qube_root=lambda x:x**3
print(list(map(qube_root,sample_List)))








# Write a Python program to triple all numbers of a given list of integers. Use Python map.

def triple(l):
    return l**3
l=[1,2,4]
a=list(map(triple,l))
