hidden = input("Enter letter: ")
count = 0
result = {}
with open("message.txt", "r") as fin:
    file_container = fin.readlines()
    for file in file_container:
        file = file.strip()
        if len(file) > 20:
            for letter in file:
                if letter == hidden:
                    count += 1
result[hidden] = count
print(result)