import os

stream = os.popen('ls -l')
output = stream.read()

print("Output of 'ls -l':")
print(output)

