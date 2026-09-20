Aim

To write a Python program to demonstrate various list and related functions in Python.

Algorithm
  
Start
Create and initialize a list of numbers.
Find the length of the list using len().
Add an element to the end of the list using append().
Insert an element at a specific position using insert().
Remove an element using remove().
Remove the last element using pop().
Find the position of an element using index().
Count the occurrence of an element using count().
Sort the list using sort().
Reverse the list using reverse().
Add multiple elements using extend().
Create a copy of the list using copy().
Remove all elements using clear().
Display all the results.
Stop.

Code:
  
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



Output:

Original List: [60, 30, 50, 20, 40, 10]
Length of the list: 6
After append(90): [60, 30, 50, 20, 40, 10, 90]
After insert(2, 25): [60, 30, 25, 50, 20, 40, 10, 90]
After remove(30): [60, 25, 50, 20, 40, 10, 90]
After pop(): [60, 25, 50, 20, 40, 10]
Index of 50: 2
Count of 50: 1
After sort(): [10, 20, 25, 40, 50, 60]
After reverse(): [60, 50, 40, 25, 20, 10]
After extend([70, 80]): [60, 50, 40, 25, 20, 10, 70, 80]
Copied List: [60, 50, 40, 25, 20, 10, 70, 80]
After clear(): []
