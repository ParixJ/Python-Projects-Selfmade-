
num = int(input("Enter A Number : "))
i = 1
ans = 0
while i <= num :
    if i % 2 != 0 :
        ans += i
    i += 1
print("Sum Of Odd Number Is  : ",ans)