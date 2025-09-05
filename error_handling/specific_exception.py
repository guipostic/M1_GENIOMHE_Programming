try:
    x = int("abc")
except ValueError:
    print("Caught a ValueError!")
# Other exceptions (like TypeError) will still crash the program.
