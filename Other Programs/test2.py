
def fun(a,b):
    if a > b :
        print (" Number 1 is bigger than Number 2 so Addition of Both Number Is - ")
        ans = a + b
    else :
       print (" Number 1 is Smaller than Number 2 so Difference Between Both Number Is - ")
       ans = a - b
    return ans

a = int(input(" Enter number 1 "))
b = int(input(" Enter number 2 "))

print ( fun(a,b) )