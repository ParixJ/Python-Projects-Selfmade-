#Returns All The Odd And Even Number Seperately From the User Defined Array

array = []
count = int(input("Enter Number Of Keys : "))

for i in range(count):
    inp = int(input("Enter Key Value : "))
    array.append(inp)

for num in array :
    if num % 2 == 0 :
        continue
    else :
        print("Odd num are",num)

for num in array :
    if num % 2 == 1 :
        continue
    else :
        print("Even num are",num)