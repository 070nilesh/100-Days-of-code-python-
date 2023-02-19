names = "Argon, Neon"
print(len(names))
print(names[0:5])
print(names[1:5])#including 1 but not 5
print(names[:4])# including 0 but not 4
print(names[:])

#negative slicing

print(names[:-3])
print(names[0:-4])
print(names[-1:-4])
print(names[-4:-1]) # length of the string - 4 = 7  and length of nthe string -1 = 10 so it will be solved by python as from  7th character to 10th character (it will print including 7th character but not the 10 th character)


sv = "harry"
print(sv[-4:-2])