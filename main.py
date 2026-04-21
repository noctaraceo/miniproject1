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

if __name__ == '__main__':
    print(add(2,3))
    print(subtract(8,67))
    print(subtract("hello", 5))