
#program to input 3 values in 3 different variable and find biggest number of them.

a = int(input("Enter Number A : "))
b = int(input("Enter Number B : "))
c = int(input("Enter Number : "))

if a > b :
    if a > c :
        print("Number A is Bigger")
    else :
        if c > b :
            print ("Number C is bigger")
        else :
            print ("Number B is Bigger")
else :
    if b > c :
        print ("Number B is Bigger")
    else :
        print ("Number C Is Bigger")