
num = int(input("Enter A number "))
rem = 0
ans = 1

while num > 0 :
    rem = num % 10
    print ("rem = ", rem)
    if rem % 2 != 0 :
        ans += rem
    num /= 10

print("Sum Of Odd Number IS : ",int(ans))
