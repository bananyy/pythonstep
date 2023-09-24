while True:
    number1_str = input('Type a first number: ')
    number2_str = input('Type a second number: ')

    if not number1_str.isdigit() or not number2_str.isdigit():
        print("Write a number")
    else:
        number1 = int(number1_str)
        number2 = int(number2_str)
        break
    
print('\n1. Addition - "+"')
print('2. Subtraction - "-"')
print('3. Multiplication - "*"')
print('4. Division - "/"')

Oprt = input('\nChoose operation: ')

if Oprt == "1" or "+":
    output = number1 + number2
elif Oprt == "2"or "-":
    output = number1 - number2
elif Oprt == "3"or "*":
    output = number1 * number2
elif Oprt == "4" or "/":
   output = number1 / number2

print("Result of operation ({}): {}".format(Oprt, output))