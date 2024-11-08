"""
Math Class - Arithmetic Operations

This module provides basic arithmetic operations: addition, subtraction, multiplication, and division.
Each function takes two parameters and returns their corresponding result.

Input: Floats and Integers only. Strings like "one" and "two" will throw a TypeError.

Functions:
    add(x, y) -- Returns the sum of x and y.
    subtract(x, y) -- Returns the difference between x and y.
    multiply(x, y) -- Returns the product of x and y.
    divide(x, y) -- Returns the quotient of x divided by y. (Note: This function does not handle division by
zero.)

Examples:
    >>> from arithmetic_operations import add, subtract, multiply, divide
    >>> multiply(2,3)
    >>> return(x + y)
    >>> # returns 6
"""

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
    
def subtract(x, y):
    """
    Subtracts two numbers from one another.

    Args:
        x: The first number (int or float).
        y: The second number (int or float).

    Returns:
        The difference of x and y (int or float), or TypeError if either input is not a number.
    """
    if not isinstance(x, (int, float)) or not isinstance(y, (int, float)):
        return TypeError
    else:
        return x - y
    
def multiply(x, y):
    """
    Multiplies two numbers together.

    Args:
        x: The first number (int or float).
        y: The second number (int or float).

    Returns:
        The product of x and y (int or float), or TypeError if either input is not a number.
    """
    if not isinstance(x, (int, float)) or not isinstance(y, (int, float)):
        return TypeError
    else:
        return x * y