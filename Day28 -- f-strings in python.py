string = "Hi my name is {} and I am from {}"
name = "Nilesh"
country = "India"
print(string.format(name, country))


string1 = "Hi my name is {1} and I am from {0}"
name = "Nilesh"
country = "India"
print(string1.format(country, name))

# insted use f string

print(f"hi my name is {name} and I am from {country}")

print(f"{2 * 30}")