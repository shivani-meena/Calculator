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
    print("the subtraction of",a,"-",b,"is","=",subtract(a,b))
elif choise=="3":
    print("the multiplication of",a,"*",b,"is","=",multiply(a,b))
elif choise=="4":
    print("the division of",a,"/",b,"is","=",division(a,b))
else:
    print("invalid input")

