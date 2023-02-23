

# recursion is defining something in terms of itself


#  example of factorial

# factorial(n) = n * factorial(n-1)

def factorial(n):
    if (n == 0 or n == 1):
        return 1
    else:
        return n * factorial(n-1)

print(factorial(5))

# working:  
# 5 * factorial(4)
# 5 * 4 * factorial(3)
# 5 * 4 * 3 * factorial(2)
# 5 * 4 * 3 * 2 * factorial(1)
# 5 * 4 * 3 * 2 * 1



# calculate fibonachi sequence

# f(0) = 0
# f(1) = 1
# f(2)  = f(0) + f(1)

# f(n) = f(n-1) + f(n-2)

def fibonachi(n):
    
         
    if (n == 0):
            return 0
    elif(n == 1):
            return 1
    else:
            return (fibonachi(n-1) + fibonachi(n-2))
n = int(input("Number: "))
for i in range(n):
    print(fibonachi(i))



# def fib(n):
    
#         if (n <= 1):
#             return n
#         else:
#             return (fib(n-1) + fib(n-2))
# for i in range(8):
#     print(fib(i))


# print(fib(8))