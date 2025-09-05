# Input list
items = ["A", "B", "C", "D"]

# Generate combinations manually
result = []
for i in range(len(items)):
    for j in range(i + 1, len(items)):
        result.append(items[i] + items[j])

print(result)

