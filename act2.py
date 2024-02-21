'''
User must input range for printing each integer.
if the number is an even number, inlude "is an even number" after the number,
if the number is an odd number, inlude "is an odd number" after the number,
if the number is divisible by 3, inlude "Hello" after the number,
if the number is divisible by 5, inlude "World" after the number,
if the number is divisible by both 3 and 5, inlude "Hello World" after the number.
'''

rangeValue = int(input("Enter range: "))
x = " is an odd number"
y = " is an even number"
a = " Hello"
b = " World"
15
for i in range(1, rangeValue + 1):
    if i % 2 == 0:
        if i % 3 == 0 and i % 5 == 0:
            print(i , y , a , b)
        elif i%5 == 0:
            print(i , y , b)
        elif i % 3 == 0:
            print(i , y , a)
        else:
            print(i , y)
    else:
        if i % 3 == 0 and i % 5 == 0:
            print(i , x , a , b)
        elif i%5 == 0:
            print(i , x , b)
        elif i % 3 == 0:
            print(i , x , a)
        else:
            print(i , x)