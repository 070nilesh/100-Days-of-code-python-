# Docstrings are not ignored by the comiler like comments insted the get some special tretement , they are for convenience for working in a team

def square(n):
    """ takes in a integer n and returns the 
    square of n """
    print(n**2)
square(5)
print(square.__doc__)

# used right above the function defenation , and are used to document the function

# PEP -8 (Python enhansment proposal)