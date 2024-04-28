#Program To Return Area Of A Circle :
radius = int(input("Enter Radius in cm :  "))
pi = 3.14

def func(radius,pi):
    ans = pi * radius * radius
    return ans

ans = func(radius,pi)

print("area of circle is - ",ans)