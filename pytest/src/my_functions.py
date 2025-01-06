def add(*args):
    total = 0
    for arg in args:
        try:
            # Convert string to float if it's a string representation of a number
            if isinstance(arg, str):
                total += float(arg)
            else:
                total += arg
        except ValueError:
            print(f"Warning: '{arg}' is not a number and will be ignored.")
    return total

def divide(a, b):
    try:
        a = float(a)
        b = float(b)
        return a / b
    except ZeroDivisionError:
        return "Error: Division by zero is not allowed."
    except ValueError:
        return "Error: Invalid input. Please provide numbers."