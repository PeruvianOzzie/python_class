def calculate(left: float, right: float, operation: int) -> float:
    calculator = {
        '1' : lambda x, y: x + y,
        '2' : lambda x, y: x - y,
        '3' : lambda x, y: x * y,
        '4' : lambda x, y: x / y,
        '5' : lambda x, y: x ** y,
        '6' : lambda x, y: x % y
    }
    result = calculator[str(operation)](left, right)
    
    if result % 1 == 0:
        return int(result)
    else:
        return result