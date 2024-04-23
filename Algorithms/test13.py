#Program Takes User Defined Array And Sorts To Acsending Form

def sorting(lst, size):
    
    for s in range(size):
        minimum_value = s

        for i in range(s + 1,size):
            if lst[i] < lst[minimum_value] :
              minimum_value = i
        (lst[s], lst[minimum_value]) = (lst[minimum_value], lst[s])

lst = []
n = int(input("Enter number of elements : "))
 
for i in range(0, n):
    ele = int(input())
    lst.append(ele)

print("Before Sorting Element Value Is : ")
print(lst)

size = len(lst)
tmp = 0
sorting(lst,size)
print(lst)
