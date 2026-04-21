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
    print(add(2,3))
    print(subtract(8,67))
    print(subtract("hello", 5))