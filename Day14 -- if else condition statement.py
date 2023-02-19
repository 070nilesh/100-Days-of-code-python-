# a = int(input("enter your age: "))
# print("your age is: ",a)

# if(a>=18):
#     print("you can drive")
# else:
#     print("you cannot drive")

    # '''conditional operators:
    # 1. ==
    # 2. >
    # 3. <
    # 4. >=
    # 5. <=
    # 6. != '''

# applePrise = 210
# budget = 200
# if(applePrise<=budget):
#     print("add apples to the cart")
# else:
#     print("do not add apples to the cart")


# num = int(input("enter the value of num: "))

# if(num<0):
#     print("the number is negative")
# elif(num==0):
#     print("the number is 0")
# else:
#     print("the number is positive")


num = int(input("enter the number: "))

if(num<0):
    print("the number is negative")
elif(num>0):
    if(num<=10):
        print("number is between 0 to 10")
    elif(num>10 and num<=20):
        print("number is between 10 to 20")
    else:
        print("number is greater than 20")
else:
    print("the number is zero")