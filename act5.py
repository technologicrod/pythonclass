'''
Create a code that accepts a string input named as "x". Check the string
and output the character that has the most repetition inside the string
and the number of times it appeared in the string.
'''

#x = "aaabbcc" #outputs a 3
#x = "xyzabc" #outputs a 1
#x = "1233211" #outputs 1 3
#x = "7sjk355ddfsshs" #outputs s 4
#x = "xyxyxyxyx" #outputs x 5
letter = ""
counter = 0

for i in range(len(x)):
    newcounter = 0
    for j in range(len(x)):
        if x[i] == x[j]:
            newcounter += 1
    if newcounter > counter:
        counter = newcounter
        letter = x[i]
print(letter, counter)