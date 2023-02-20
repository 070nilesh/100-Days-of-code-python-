import time

timestamp = time.strftime("%H:%M:%S")
print(timestamp)

Hours = int(time.strftime("%H"))

if(Hours>4 and Hours<12):
    print("Good Morning")
elif(Hours>12 and Hours<16):
    print("Good Afternoon")
elif(Hours>16 and Hours<22):
    print("Good Evening")
else:
    print("Good Night")