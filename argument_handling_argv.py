import sys

# sys.argv is the list of command-line arguments passed to the script
# sys.argv[0] is the script name, sys.argv[1], sys.argv[2], ... are arguments
print("Script name:", sys.argv[0])

if len(sys.argv) > 1:
    print("Arguments passed:")
    for i, arg in enumerate(sys.argv[1:], start=1):
        print(f"  Argument {i}: {arg}")
else:
    print("No additional arguments were passed.")

