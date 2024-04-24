#This Program Is A Simple Calculator That Does 5 Operation On The 2 Number User Enters :

def calculator(a,b):
    add=a+b
    sub=a-b
    prod=a*b
    div=a/b
    mod=a%b
    return add,sub,prod,div,mod

a=int(input("enter a value "))
b=int(input("enter a value "))

ADD,SUB,PROD,DIV,MOD = calculator(a,b)

print ("Addition IS ", ADD)
print ("Substraction is", SUB)
print ("Product is ", PROD)
print ("Division IS", DIV)
print ("Modula is", MOD)