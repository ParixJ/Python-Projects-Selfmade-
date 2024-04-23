#Program To Return And New Even Number Array From User Defined Array :
array = []
num = int(input("Enter Number Of Keys : "))

for a in range(num):
    integer = int(input("Enter Value : "))
    array.append(integer)

print("Original Array",array)

size = len(array)
evenarr = []

for b in range(size):
    if array[b] % 2 == 0 :
        evenarr.append(array[b])

print("Even Numbers From 1st Array",evenarr)