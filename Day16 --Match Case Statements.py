# python 3.10 onwards....
# match case in python is used to compare variables with patterns

x = int(input("Enter the value of x: "))
    # x is the variable we are using to match
match x:
    # for x = o
    case 0:
        print(x," is zero")
    case 4:
        print(x," is 4")
    case _ if(x != 40): # default case is written by underscore
        print(x," is not 40")
    case _ if(x != 50):
        print(x," is not 50")
    case _:
        print(x, "is default")