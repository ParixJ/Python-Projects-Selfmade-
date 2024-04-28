
number = int(input(" Enter A Number : "))
rem = 0
ans = 0
count = 0

while number != 0 :
    rem = number % 10 
    if rem % 2 == 0 :
        print ("even number is ", int(rem))
        ans = ans + rem
    number = number // 10 
    count = count + 1
print ("Sum Of Even Number Is : ",ans)
print ("Total Number Of Digit Is : ",count)
