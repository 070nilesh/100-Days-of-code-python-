# a function is a block of code that performs a specific tast when it is called

def calculateGmean(a,b):
    mean = a*b/a+b
    print(mean)

def is_greater(a,b):
    if(a>b):
        print("first number is greater than second")
    elif(a == b):
        print(" both the numbers are equal to each other")
    else:
        print("second number is greater than first")    


def is_lesser(a,b):
    pass # this indicates that we will write the body of the function later....and the code should not return an error

a = 10
b = 20

calculateGmean(a,b)
is_greater(a,b)

c= 23
d = 34

calculateGmean(c,d)
is_greater(c,d)