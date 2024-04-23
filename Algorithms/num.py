#Program To Count Even,Odd Number With  Total Number Of Digits :

num = int(input("Enter A Number : "))
rem = 0
odd = 0
even = 0
count = 0
while num > 0 :
    rem = num % 10 
    if rem % 2 == 0 :
        even = even + 1
    else :
        odd = odd + 1 
    num = num // 10
    count = count + 1
print("Total Number Of Even Digit Is : ",even)
print("Total Number Of Odd Digits Is : ",odd    )
print("Total Number Of Digit Is : ",count)