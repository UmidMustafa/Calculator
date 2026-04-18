import math

class Calculator:
    def __init__(self):
        pass

    def add(self, a, b):
        return a + b

    def substract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        return a / b
    
    def squareroot(self, a):
        return a ** 0.5

    def power(self, a, b):
        return a ** b
    
    def factorial(self, a):
        return math.factorial(a) 
    
    def modulo(self, a, b):
        return a % b