s = "Welcome to the python world"

print("Original String:", s)

# Find length
print("Length:", len(s))

# Convert to uppercase
print("Uppercase:", s.upper())

# Convert to lowercase
print("Lowercase:", s.lower())

# Get character at a position
print("Character at index 6:", s[6])

# Find position of a word
print("Position of python:", s.find("python"))

# Extract part of string
print("Slice:", s[6:])

# Replace a word
print("Replace:", s.replace("python", "world"))

# Check whether a word exists
print("Contains python:", "python" in s)

# Concatenate two strings
print("Concatenation:", s + "program")

# Remove spaces
s2 = "  Welcome to the python world  "
print("Trim:", s2.strip())

Output:
Original String: Welcome to the python world
Length: 28
Uppercase: WELCOME TO THE PYTHON WORLD
Lowercase: welcome to the python world
Character at index 6: m
Position of python: 15
Slice: to the python world
Replace: Welcome to the world world
Contains python: True
Concatenation: Welcome to the python worldprogram
Trim: Welcome to the python world
