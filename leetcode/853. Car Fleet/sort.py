# If 2 dimensional iterators are sorted, the first index values are compared

a = [[1, 8], [2, 7], [3, 6], [4, 5]]
b = [(1, 8), (2, 7), (3, 6), (4, 5)]

print(sorted(a, reverse=True))
print(sorted(b, reverse=True))
