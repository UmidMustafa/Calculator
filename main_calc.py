import calculation as c
def main():
    print('Welcome to the calculator!!!')
    my_calc = c.Calculator()
    
    # Calculator functions
    print('1. Add')
    print('2. Subtract')
    print('3. Multiply')
    print('4. Divide')
    print('5. Square Root')
    print('6. Power')
    print('7. Factorial')
    print('8. Modulo')
    print('9. Exit')

    # Getting choice
    choice = input('Enter your choice: ') 
    
    # Performing operation

    # Addition
    if choice == '1':
        num1 = float(input('Enter first number: '))
        num2 = float(input('Enter second number: '))
        print(f'Result: {my_calc.add(num1, num2)}')
    
    # Subtraction
    elif choice == '2':
        num1 = float(input('Enter first number: '))
        num2 = float(input('Enter second number: '))
        print(f'Result: {my_calc.substract(num1, num2)}')
    
    # Multiplication
    elif choice == '3':
        num1 = float(input('Enter first number: '))
        num2 = float(input('Enter second number: '))
        print(f'Result: {my_calc.multiply(num1, num2)}')
    
    # Division
    elif choice == '4':
        num1 = float(input('Enter first number: '))
        num2 = float(input('Enter second number: '))
        print(f'Result: {my_calc.divide(num1, num2)}')
    
    # Square Root
    elif choice == '5':
        num = float(input('Enter a number: '))
        print(f'Result: {my_calc.squareroot(num)}')
    
    # Power
    elif choice == '6':
        num1 = float(input('Enter first number: '))
        num2 = float(input('Enter second number: '))
        print(f'Result: {my_calc.power(num1, num2)}')
    
    # Factorial
    elif choice == '7':
        num = int(input('Enter a number: '))
        print(f'Result: {my_calc.factorial(num)}')
    
    # Modulo
    elif choice == '8':
        num1 = float(input('Enter first number: '))
        num2 = float(input('Enter second number: '))
        print(f'Result: {my_calc.modulo(num1, num2)}')
    
    # Exit
    elif choice == '9':
        print('Exiting calculator...')
        exit()
    
    # Invalid choice
    else:
        print('Invalid choice. Please try again.')
        main()
    

if __name__ == '__main__':
    main()
    
