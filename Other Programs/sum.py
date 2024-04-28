
num = int(input("Enter A number"))
rem = 0
ans = 0
while num > 0 :
    rem = num % 10
    ans += rem
    num /= 10
print ("Sum Of Digits : ", int (ans))

