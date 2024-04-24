
i = 1

def func(i):
    while i <= 5 :
        j = 1
        while j <= i :
            print(f"* ",end="")
            j = j + 1
        print("")
        i = i + 1
func(i)