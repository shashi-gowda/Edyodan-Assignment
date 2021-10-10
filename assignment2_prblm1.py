a=[(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
def last(n):
    return n[-1]
def sort(a):
    return sorted(a,key=last)
print('sorted:', sort(a))
sorted: [(2, 1), (1, 2), (2, 3), (4, 4), (2, 5)]


