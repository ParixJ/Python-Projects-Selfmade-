

def func():
    val = int(input("Enter A Number Greater Than One : "))
    i = 1
    while i <= val :
        j = 1 
        while j <= i :
            print(f"* ",end="")
            j = j + 1
        print("")
        i = i + 1
func()