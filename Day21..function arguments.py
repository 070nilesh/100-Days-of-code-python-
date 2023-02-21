# the are 4 types of arguments that we can provide in a function
# 1. default argumenta
# 2. keyword arguments
# 3. veriable length arguments
# 4. required arguments

# default arguments

# inthis the function will asum the values wich are provided default if the values are not provided
def average(a = 9, b = 3):
    print("average: ", (a+b)/2)
average()

#keyword arguments

def avg(a, b):
    print("avg: ", (a+b)/2)
avg(b = 4, a = 3)

# required argument 
# in this if the values are not provided in the default section the need to be provided in the arguments other the code will not run and will throw an error

def avgg(*numbers):
    sum = 0
    for i in numbers:
        sum = sum + i
    print("avgg: ", sum/len(numbers))

avgg(2,3,4,5,6)
