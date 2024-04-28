n = int(input("Enter A number "))
sum = 0
dig = 0
while (n != 0): 
    sum = n % 10
    if sum % 2 == 0 :
        print ("even number is ",int(sum))
        dig = dig + sum
    n = n//10
       
print ("sum of even digit is : ",int(dig))