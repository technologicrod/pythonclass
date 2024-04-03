hidden = ''
with open("message.txt", "r") as fin:
    file_container = fin.readlines()
    for line in file_container:
        for char in line:
            if char.isalpha():
                hidden += char

print(hidden)
