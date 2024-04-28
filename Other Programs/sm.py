
n = int(input("Enter A number "))
sum = 0
dig = 0
while (n != 0): 
    sum = n % 10
    if sum % 2 != 0 :
        print ("odd number is ",int(sum))
        dig = dig + sum
    n = n//10
       
print ("sum of odd digit is : ",int(dig))