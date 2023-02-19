# operations on a string

a = "!!!! a r g o n !!!!"
print(len(a))

# strings are immuatable

print(a.upper())
print(a.lower())
print(a.rstrip("!"))
print(a.replace("argon", "neon"))
print(a.split(" "))

heading = "introduction To pyThon"
print(heading.capitalize())

print(a.count("!"))

str1 = "he's name is don. he is a good man"
print(str1.find("is"))

an = "fsgdfasjgiuyhjf"
print(an.isalnum())# checks wether the character in the string are alpha numeric or not

a = "hjgjdfbjhguy234\n"
print(a.isalpha())# checks if only alphabets are present

print(an.islower())# checks wether the string is in lowercase

print(a.isprintable())

print(str1.isspace())

# startswith and endswith

print(str1.title())