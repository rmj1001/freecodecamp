def number_pattern(n):
    if not isinstance(n, int):
        return "Argument must be an integer value."
    if n < 1:
        return "Argument must be an integer greater than 0."

    digits = []

    for digit in range(1, n + 1):
        digits.append(digit)

    return " ".join(str(digit) for digit in digits)
