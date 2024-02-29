def calculation(x, y, operator):

    if operator == '+':

        total = x + y
        return total

    elif operator == '-':

        total = x - y
        return total
    
    elif operator == 'x':

        total = x * y
        return total
    
    elif operator == '/':

        total = x / y
        return total


num1 = float(input("Please enter a number : "))
num2 = float(input("Please enter a number : "))

operator = input("Enter the math symbol you would like to use : ")

calc = calculation(num1, num2, operator)
print(calc)