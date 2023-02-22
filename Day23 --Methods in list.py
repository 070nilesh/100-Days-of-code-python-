l = [4, 5, 3, 8 ,6]
print(l)

# to add an element in the list(at the end of the list)
l.append(7)
print(l)

#to sort the elements in the list

l.sort()
print(l)

# to sort the list in decending order

l.sort(reverse = True)
print(l)

# to print the list in the reverse manner

l.reverse()
print(l)

# to display the index of the particular element(first occurance in the list)

print(l.index(7))

# to count the no.of occurance of the particular element

print(l.count(5))

# to copy a list to another variable

m = l.copy()
m[0] = 0
print(m)

# to insert a element at a particular index

l.insert(1, 34) # insert 34 at index 1
print(l)

# to add a list at the end of the another list

l.extend(m)
print(l)

# to concanite two list withou changing any of them 

k = l + m
print(k)