import time
import random

def delay_print(text):
    for c in text:
        print(c, end='', flush=True)
        time.sleep(random.random() * 0.09)
    print()

def first(number1, number2):
    delay_print('\n1. Addition.\n2. Subtraction.\n3. Multiplication.\n4. Division.')
    Oprt = int(input("\nChoose operation: "))

    output = int

    if Oprt == 1:
        output = number1 + number2
    elif Oprt == 2:
        output = number1 - number2
    elif Oprt == 3:
        output = number1 * number2
    elif Oprt == 4:
        output = number1 / number2

    print("Result of operation ({}): {}".format(Oprt, output))

def second(number1, number2):
    if number1 == number2:
        delay_print('\nThe numbers are equal.')
    elif number1 > number2:
        delay_print(f'\nThe number {number1} > {number2}')
    elif number1 < number2:
        delay_print(f'\nThe number {number1} < {number2}')

def third(number1, number2):
    delay_print('\n1. Integer.\n2. Float.')
    sOprt = int(input("Select the type to replace: "))

    if sOprt == 1:
        output1 = int(number1)
        output2 = int(number2)
    elif sOprt == 2:
        output1 = float(number1)
        output2 = float(number2)

    delay_print(f"Result:  \nnumber 1: {output1}, \nnumber 2: {output2}")

num1 = float(input("Type a first number: "))
num2 = float(input("Type a second number: "))

delay_print('\n1. Arithmetic operations.\n2. Comparison operations.\n3. Conversion of data types.')

sOprt = int(input('\nChoose operation: '))

if sOprt == 1 or sOprt == "Arithmetic operations":
    first(num1, num2)
elif sOprt == 2 or sOprt == "Comparison operations":
    second(num1, num2)
elif sOprt == 3 or sOprt == "Conversion of data types":
    third(num1, num2)

