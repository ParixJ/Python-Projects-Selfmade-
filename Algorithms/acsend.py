#Array Sorting Program :
#Sorts Given Array In Acsending Form :

array = []
count = int(input("Enter Num Of Keys : "))
tmp = 0

for i in range(count):
    num = int(input("Enter Value : "))
    array.append(num)

print("Array Before Sorting Is : ",array)

size = len(array)

def Sort(size,array,tmp):
    for s in range(size):
        m = s
        for i in range(s+1,size):
            if array[i] < array[s]:
                (array[s],array[i])=(array[i],array[s])

Sort(size,array,tmp)
print("Array After Sorting Is : ",array)