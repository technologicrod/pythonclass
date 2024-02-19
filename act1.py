'''Strings from the 1st array should be compared to the queries, or the 2nd array.
should count how many times the elements of the 2nd array present in the 1st array.
use the 2nd array as the basis for counting, then outputs its result to a new arary.
'''
x = ["aba", "baba", "aba", "xzxb"]
y = ["aba", "xzxb", "ab"]
## [2, 1, 0]

a = ["xzz", "xy", "xyz", "yyy", "yyy", "yyy", "xyz"]
b = ["xy", "xyz", "yyy"]
##[1, 2, 3]
counterarr = []

for i in range(len(b)):
    count = 0
    for j in range(len(a)):
        if b[i] == a[j]:
            count += 1

    counterarr.append(count)
print(counterarr)
