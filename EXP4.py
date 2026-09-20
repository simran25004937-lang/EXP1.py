numbers = [60, 30, 50, 20, 40, 10]

print("Original List:", numbers)

# len()
print("Length of the list:", len(numbers))

# append()
numbers.append(90)
print("After append(90):", numbers)

# insert()
numbers.insert(2, 25)
print("After insert(2, 25):", numbers)

# remove()
numbers.remove(30)
print("After remove(30):", numbers)

# pop()
numbers.pop()
print("After pop():", numbers)

# index()
print("Index of 50:", numbers.index(50))

# count()
print("Count of 50:", numbers.count(50))

# sort()
numbers.sort()
print("After sort():", numbers)

# reverse()
numbers.reverse()
print("After reverse():", numbers)

# extend()
numbers.extend([70, 80])
print("After extend([70, 80]):", numbers)

# copy()
new_list = numbers.copy()
print("Copied List:", new_list)

# clear()
numbers.clear()
print("After clear():", numbers)