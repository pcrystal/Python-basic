
def calculate():
    op1 = int(input("Enter a whole number: "))
    op2 = int(input("Enter another whole number: "))
    num1 = str.upper(input("Enter an operator (eg.add): "))
    if (num1 == "ADD"):
              results = (op1 + op2)
              print(op1, " + " ,op2, " = ",results)
    elif (num1 == "subtract"):
              results = (op1 - op2)
              print(op1, " - " ,op2, " = ",results)
              
    elif (num1 == "multiply"):
              results = (op1 * op2)
              print(op1, " * ",op2," = ",results)
    elif (num1 == "divide"):
              results = (op1 / op2)
              print(op1, " / ",op2, " = ",results)
    else:
        print("Your command is invalid")
              
calculate()
              