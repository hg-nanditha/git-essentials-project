"""Calculator module providing basic arithmetic operations."""

def add(a: float, b: float) -> float:
    """Return the sum of a and b."""
    return a + b


def subtract(a: float, b: float) -> float:
    """Return the difference of a and b."""
    return a - b


def multiply(a: float, b: float) -> float:
    """Return the product of a and b."""
    return a * b


def divide(a: float, b: float) -> float:
    """Return the quotient of a divided by b.

    Raises:
        ValueError: If b is zero.
    """
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b


def power(a: float, b: float) -> float:
    """Return a raised to the power of b."""
    return a ** b


def modulo(a: float, b: float) -> float:
    """Return the modulo of a and b.

    Raises:
        ValueError: If b is zero.
    """
    if b == 0:
        raise ValueError("Cannot perform modulo by zero.")
    return a % b


def calculate(operation: str, a: float, b: float) -> float:
    """Perform the specified arithmetic operation on a and b.

    Supported operations: 'add', 'subtract', 'multiply', 'divide', 'power', 'modulo', '+', '-', '*', '/', '**', '%'
    """
    ops = {
        'add': add,
        '+': add,
        'subtract': subtract,
        '-': subtract,
        'multiply': multiply,
        '*': multiply,
        'divide': divide,
        '/': divide,
        'power': power,
        '**': power,
        'modulo': modulo,
        '%': modulo,
    }
    op_func = ops.get(operation.strip().lower())
    if op_func is None:
        raise ValueError(f"Unsupported operation: '{operation}'")
    return op_func(a, b)


if __name__ == "__main__":
    print("Simple Python Calculator")
    print("Operations: +, -, *, /, **, %")
    try:
        num1 = float(input("Enter first number: "))
        op = input("Enter operator (+, -, *, /, **, %): ")
        num2 = float(input("Enter second number: "))
        result = calculate(op, num1, num2)
        print(f"Result: {result}")
    except Exception as e:
        print(f"Error: {e}")
