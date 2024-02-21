##must output the unique number in an array.
##means the number should not have duplicates in the array.

x = [0, 0, 1, 2, 1, 3, 3, 5, 5] ##gets 2
y = [1, 1, 1, 2, 2, 3, 3, 4, 4, 9] ##gets 9

for i in range(len(x)):
    counter = 0
    for j in range(len(x)):
        if x[i] == x[j]:
            counter += 1
    if counter == 1:
        print(x[i])