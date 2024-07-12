def safe_divide(numerator, denominator):
    result = None
    try:
        result = float(numerator) / float(denominator)
        return f"The result of the division is {result}"
    except ZeroDivisionError as e:
        return "Error: Cannot divide by zero."
    except ValueError as f:
        return "Error: Please enter numeric values only."
