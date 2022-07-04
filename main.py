while True :
    #NUMBERS
    num1 = input("Enter number: ")
    num2 = input("Enter another number: ")

    addSubtract = input("+,-,/, or x?")
    #ADD
    if addSubtract == '+':
        result = float(num1) + float(num2)
    #SUBTRACT
    if addSubtract == '-':
        result = float(num1) - float(num2)
    #DIVIDE
    if addSubtract == '/':
        result = float(num1) / float(num2)
    #MULTIPLY
    if addSubtract == 'x' or '*':
        result = float(num1) * float(num2)
    print(result)

