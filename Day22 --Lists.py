# lists are ordered collections of data items
# lists are changable
# a list can have items of diffrent data types


marks = [3, 5, 6, "argon", True, 45, 677, 78, 789]

# to check wether the element is in the list or not

if 7 in marks:
    print("yes")
else:
    print("NO")

if "rgo" in "argon":
    print("yes")
else:
    print("no")

print(marks[1:9:2])

lst = [i for i in range(4)]
lst1 = [i*i for i in range(5)]
print(lst)
print(lst1)

lst3 = [i for i in range(20) if i%2 == 0]
print(lst3)



