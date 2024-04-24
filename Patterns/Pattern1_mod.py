#Program to Make A Pyramid Pattern Based On User Defined Input :

val = int(input("Enter A Number Greater Than One : "))
i = 1
while i <= val :
    k = 1
    while k <= i :
        print(f"* ",end="")
        k = k + 1
    print("")
    i = i + 1