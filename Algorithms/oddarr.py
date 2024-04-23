#This Program Creates A New Array Of Odd Number From The User Defined Array :

array = []
num = int(input("Enter Value Of Total Keys : "))

for a in range(num):
    ele = int(input("Enter Key Value : "))
    array.append(ele)

print("Original Array",array)

size = len(array)
oddarr = []

for b in range(size):
    if array[b] % 2 == 1 :
        oddarr.append(array[b])

print("Odd Numbers From 1st Array",oddarr)