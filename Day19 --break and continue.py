# break is used to stop the loop (iteration)
# continue is used to skip the iteration of the loop


# break meanse to leave the loop 
# continue meanse to leave the iteration



for i in range(13):
    if(i == 10):
        break
    print("5 X ", i+1 , " = ", 5 * (i+1))


for a in range(13):
    if(a == 10):
        continue
    print("5 X ", a , " = ", 5 * a)



    # imulating do while loop with python

i = 0
while true:
    print(i)
    i = i+1
    if(1%100 == 0):
        break