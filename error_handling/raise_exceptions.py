try:
    x = -5
    if x < 0:
        raise ValueError("x must be non-negative!")
except ValueError as e:
    print(f"Caught an error: {e}")

