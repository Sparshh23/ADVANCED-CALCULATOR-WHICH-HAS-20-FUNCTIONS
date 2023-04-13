import math
def add(num1, num2):
    return num1 + num2
def subtract(num1, num2):
    return num1 - num2
def multiply(num1, num2):
    return num1 * num2
def divide(num1, num2):
    if num2 == 0:
        return "Error: Division by zero"
    else:
        return num1 / num2
def modulus(num1, num2):
    if num2 == 0:
        return "Error: Division by zero"
    else:
        return num1 % num2
def factorial(num):
    if num < 0:
        return "Error: Invalid input for factorial"
    elif num == 0 or num == 1:
        return 1
    else:
        return num * factorial(num - 1)
def power(num1, num2):
    return num1 ** num2
def square_root(num):
    if num < 0:
        return "Error: Invalid input for square root"
    else:
        return math.sqrt(num)
def cube_root(num):
    return num ** (1/3)
def nth_root(num, n):
    return num ** (1/n)
def logarithm(num, base):
    if num < 0 or base <= 0 or base == 1:
        return "Error: Invalid input for logarithm"
    else:
        return math.log(num, base)
def natural_logarithm(num):
    if num < 0:
        return "Error: Invalid input for natural logarithm"
    else:
        return math.log(num)
def common_logarithm(num):
    if num < 0:
        return "Error: Invalid input for common logarithm"
    else:
        return math.log10(num)
def absolute_value(num):
    return abs(num)
def reciprocal(num):
    if num == 0:
        return "Error: Cannot calculate reciprocal of zero"
    else:
        return 1 / num
def percentage(num, percent):
    return (num * percent) / 100
def inverse_sine(num):
    if num < -1 or num > 1:
        return "Error: Invalid input for inverse sine"
    else:
        return math.asin(num)
def inverse_cosine(num):
    if num < -1 or num > 1:
        return "Error: Invalid input for inverse cosine"
    else:
        return math.acos(num)
def inverse_tangent(num):
    return math.atan(num)
def hyperbolic_sine(num):
    return math.sinh(num)
def calculator():
    print("Welcome to the Python Calculator!")
    while True:
        print("Select an operation:")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Modulus")
        print("6. Factorial")
        print("7. Power")
        print("8. Square Root")
        print("9. Cube Root")
        print("10. Nth Root")
        print("11. Logarithm")
        print("12. Natural Logarithm")
        print("13. Common Logarithm")
        print("14. Absolute Value")
        print("15. Reciprocal")
        print("16. Percentage")
        print("17. Inverse Sine")
        print("18. Inverse Cosine")
        print("19. Inverse Tangent")
        print("20. Hyperbolic Sine")
        print("0. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 0:
            print("Thank you for using the Python Calculator!")
            break
        elif choice == 1:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            result = add(num1, num2)
            print("Result:", result)
        elif choice == 2:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            result = subtract(num1, num2)
            print("Result:", result)
        elif choice == 3:
        
            pass
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    calculator()
