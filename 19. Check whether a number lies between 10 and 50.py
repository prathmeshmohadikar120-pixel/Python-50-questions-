a = float(input("Enter the first number: "))
b = float(input("Enter the second number: "))
operator = input("Enter an operator : ")

if operator == '+':
    result = a + b
    print(f"{a} + {b} = {result}")
elif operator == '-':
    result = a - b
    print(f"{a} - {b} = {result}")
elif operator == '*':
    result = a * b
    print(f"{a} * {b} = {result}")
elif operator == '/':
    result = a / b
    print(f"{a} / {b} = {result}")

else:
    print("wrong input / invlid")
