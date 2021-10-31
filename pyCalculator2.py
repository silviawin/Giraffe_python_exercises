
num1 = float(input("Type the first number: "))
op = input("Enter operator: ")
num2 = float(input("Type the second number: "))

if op == "+":
    print(num1 + num2)
elif op == "-":
    print(num1 - num2)
elif op == "*":
    print(num1 * num2)
elif op == "/ ":
    print(num1 / num2)
else:
    print("Please type valid inputs")


