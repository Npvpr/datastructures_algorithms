# zip returns an iterator of tuples pairing elements of same indexes from 2 iterators
# It will stop at the short iterator's last element

a = [1, 2, 3, 4]
b = [5, 6, 7, 8, 9]

print(zip(a, b))
print(list(zip(a, b)))
