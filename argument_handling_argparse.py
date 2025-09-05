import argparse

# Create the parser
parser = argparse.ArgumentParser(description="Greet a user with optional enthusiasm")

# Add arguments
parser.add_argument("name", help="The name of the person to greet")
parser.add_argument("-e", "--enthusiastic", action="store_true",
                    help="Add extra enthusiasm to the greeting")

# Parse arguments
args = parser.parse_args()

# Use the arguments
greeting = f"Hello, {args.name}"
if args.enthusiastic:
    greeting += "!!!"

print(greeting)

