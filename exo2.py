# Path to your text file
filename = "book.txt"

# Read file
with open(filename, "r", encoding="utf-8") as f:
    text = f.read()

# Lowercase everything
text = text.lower()

# Remove punctuation manually (keep only letters and spaces)
cleaned = ""
for ch in text:
    if ch.isalpha() or ch.isspace():
        cleaned += ch
    # else drop it (punctuation, digits, etc.)

# Split into words
words = cleaned.split()

# Count words using a dictionary
counts = {}
for w in words:
    if w in counts:
        counts[w] += 1
    else:
     counts[w] = 1

# Sort by frequency (highest first)
sorted_counts = sorted(counts.items(), key=lambda x: x[1], reverse=True)

# Show top N words
top_n = 20
for word, freq in sorted_counts[:top_n]:
    print(word, freq)

