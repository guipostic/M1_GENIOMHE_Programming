
alphabet = ["A", "C", "G", "T"]

def generate_tuples(prefix, length):
    if length == 0:
        print(prefix)
    else:
        for base in alphabet:
            generate_tuples(prefix + base, length - 1)

n = 4 # Sequence length
generate_tuples("", n)

