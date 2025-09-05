# mymath.py
def add(a, b):
    return a + b

def square(x):
    return x * x

if __name__ == "__main__":
    print("Testing add:", add(2, 3))
# If you import mymath in another file, the test won’t run.
# When it’s imported, __name__ is the module’s name.
# NOTE: A package is a collection of modules inside a folder, with a special __init__.py file.
