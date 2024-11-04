def add(x, y):
    """
    Adds two numbers together.

    Args:
        x: The first number (int or float).
        y: The second number (int or float).

    Returns:
        The sum of x and y (int or float), or TypeError if either input is not a number.
    """
    if not isinstance(x, (int, float)) or not isinstance(y, (int, float)):
        return TypeError
    else:
        return x + y