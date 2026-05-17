def find_max(numbers):
    max_val = numbers[0]
    for n in numbers:
        if n < max_val:  # bug: should be >
            max_val = n
    return max_val


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b
