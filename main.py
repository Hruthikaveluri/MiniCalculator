# main.py
from app.calculator import add, subtract, multiply, divide

def main():
    print(" Simple Calculator App")
    print("Available operations: add, subtract, multiply, divide")

    # Get user input
    operation = input("Enter operation: ").strip().lower()
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))

    try:
        if operation == "add":
            result = add(a, b)
        elif operation == "subtract":
            result = subtract(a, b)
        elif operation == "multiply":
            result = multiply(a, b)
        elif operation == "divide":
            result = divide(a, b)
        else:
            print("Invalid operation. Please choose from add/subtract/multiply/divide.")
            return

        print(f" Result: {result}")

    except ValueError as e:
        print(f" Error: {e}")
    except Exception as e:
        print(f" Unexpected error: {e}")

if __name__ == "__main__":
    main()