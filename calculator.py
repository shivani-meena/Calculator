def add(a,b):
    return a+b
def subtract(a,b):
    return a-b
def multiply(a,b):
    return a*b
def division(a,b):
    return a/b

print("oprations")
print("1.add")
print("2.subtract")
print("3.multipy")
print("4.divide")

a=int(input("enter first number"))
b=int(input("enter second number"))
choise=input("choise operation you want to perform")

if choise=="1":
    print("the addition of",a,"+",b,"is","=",add(a,b))
elif choise=="2":
    print(a,"-",b,"=",subtract(a,b))
elif choise=="3":
    print(a,"*",b,"=",multiply(a,b))
elif choise=="4":
    print(a,"/",b,"=",division(a,b))
else:
    print("invalid input")


# # def add(a,b,c):
# #     if c=="+":
# #         return a+b
# a=int(input("first number"))
# b=int(input("second number"))
# c=input("operator")
# print(add(a,b,c))

# def add(a,b,c):
#     if c=="-":
#         return a-b
# a=int(input("first number"))
# b=int(input("second number"))
# c=input("operator")
# print(add(a,b,c))

# def add(a,b,c):
#     if c=="*":
#         return a*b
# a=int(input("first number"))
# b=int(input("second number"))
# c=input("operator")
# print(add(a,b,c))

# def add(a,b,c):
#     if c=="/":
#         return a/b
# a=int(input("first number"))
# b=int(input("second number"))
# c=input("operator")
# print(add(a,b,c))


# def add(a,b):
#     return a+b
# def subtract(a,b):
#     return a-b
# def multiply(a,b):
#     return a*b
# def divison(a,b):
#     return a/b

# a=int(input("enter first number"))
# b=int(input("enter second number"))

# choise=input("enter operation")

# if choise=="+":
#     print(a,"+",b,"=",add(a,b))
# elif choise=="-":
#     print(a,"-",b,"=",subtract(a,b))