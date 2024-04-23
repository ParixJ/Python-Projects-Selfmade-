#Program To Sort Array in Acsending Form :

def sorting(array, size):
    
    for s in range(size):
        minimum_value = s

        for i in range(s + 1,size):
            if array[i] < array[minimum_value] :
              minimum_value = i
        tmp = array[s]
        array[s] = array[minimum_value]
        array[minimum_value] = tmp      
        #(array[s], array[minimum_value]) = (array[minimum_value], array[s])

array = [122,42,432,54,123]
size = len(array)
tmp = 0
sorting(array,size)
print(array)