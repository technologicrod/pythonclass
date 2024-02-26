'''
Convert the given time to 24-hour format.
'''
a = "07:05:45PM" ## 19:05:45
b = "12:00:00AM" ## 00:00:00
c = "12:45:54PM" ## 12:45:54
d = "09:30:16AM" ## 09:30:16
e = "11:59:59PM" ## 23:59:59

time = s.split(":")

if time[2][2] == "A":
    if time[0] == "12":
        time[0] = "00"
elif time[2][2] == "P":
    if time[0] != "12":
        time[0] = int(time[0])
        time[0] += 12
time[2] = time[2][:2]
newTime = f"{time[0]}:{time[1]}:{time[2]}"
print(newTime)