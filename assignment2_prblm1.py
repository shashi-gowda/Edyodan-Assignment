from operator import itemgetter
a=[(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
b=sorted(a,key=itemgetter(1))
print(b)


