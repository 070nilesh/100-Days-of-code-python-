# if you want to add or remove any item from the tuple you cannot do it you first need to convert the tuple to the list and then perform the operation

countries = ("spain", "italy", "India", "England", "Germany")
print(countries)

temp = list(countries)
temp.append("Russia") # to add an item 
temp.pop(3)          # to remove item
temp[2] = "Finland"   # to change the item

countries = tuple(temp)
print(countries)

# we can concinate two tuples directly without converting them into list , because of the fact that we are not changing the tuples we are just adding two tuples and saving them into another tuple

# to count the no.of occurances of the element
tup = (1,2,3,3,4,5,4,5,6,5,6,7)
print(tup.count(5))

#returns the index at which the element is present
print(tup.index(5))