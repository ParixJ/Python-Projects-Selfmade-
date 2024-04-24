#Simple Calculator Which Takes 2 Numbers From User And Asks For Which Operation To Do :

opp = input("Enter A Operator : + - * / ")
num1 = float(input("Enter 1st Number : "))
num2 = float(input("Enter 2nd Number : "))

if opp == "+":
    print(num1 + num2)
elif opp == "-":
    print(num1 - num2)
elif opp == "*":
    print(num1 * num2)
elif opp == "/":
    print(num1 / num2)