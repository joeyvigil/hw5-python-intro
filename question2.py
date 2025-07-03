def main():
    while(True):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        print("Choose operation:\n1. Add\n2. Subtract\n3. Multiply\n4. Divide")
        operation = float(input ("Enter choice (1-4): "))
        if(operation==1):
            print(f"{num1} + {num2} = {add(num1,num2)}\n")
        elif(operation==2):
            print(f"{num1} - {num2} = {subtract(num1,num2)}\n")
        elif(operation==3):
            print(f"{num1} x {num2} = {multiply(num1,num2)}\n")
        elif(operation==4):
            print(f"{num1} / {num2} = {divide(num1,num2)}\n")

def add(a,b):
    return a+b

def subtract(a,b):
    return a-b

def divide(a,b):
    if(b!=0):
        return a/b
    return "Error: Cannot divide by zero!"

def multiply(a,b):
    return a*b

main()