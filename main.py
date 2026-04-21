def add(a,b):
    try:
        return a + b
    except Exception as e:
        print(f"error while adding: {e}")

def subtract(a,b):
    try:
        return a - b
    except Exception as e:
        print(f"error while subtracting: {e}")
    except TypeError as e:
        print(f"error while subtracting: {e}")
def multiply(a,b):
    try:
        return a * b
    except Exception as e:
        print(f"error while multiplying: {e}")
    except TypeError as e:
        print(f"error while multiplying: {e}")
def divide(a,b):
    try:
        return a / b
    except Exception as e:
        print(f"error while dividing: {e}")
    except TypeError as e:
        print(f"error while dividing: {e}")
    except ZeroDivisionError as e:
        print(f"error while dividing: {e}")
if __name__ == '__main__':
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    char = input("Enter operating symbol: ")

    if char == '+':
        print(add(a, b))
    elif char == '-':
        print(subtract(a, b))
    elif char == '*':
        print(multiply(a, b))
    elif char == '/':
        print(divide(a, b))
    else:
        print("Invalid operator")