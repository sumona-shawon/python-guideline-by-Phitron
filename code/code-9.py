# .................... take multiple input

# string:
a = input().split()
print(a)

# int:
a = list(map(int, input().split())) 
print(a)
# map(2 parameters)
# list prevents converting to strings

# float:
a = list(map(float, input().split()))
print(a)
# without list will return object

# .................... list comprehension part-1

# example-1: iteration through number:
a = [10, 20, 30, 40, 50] # main list
b = [i + 5 for i in a]
print(b)

# example-2: iteration through string:
a = "Hello World"
b = [i for i in a]
# b = list(a) # shortcut
print(b)

# example-3: using range function:
a = [i for i in range(1, 20, 2)]
b = [i for i in range(2, 20, 2)]
# b = list(range(2, 20, 2))
# shortcut (condition isn't applicable here)
print(a)
print(b)

# .................... list comprehension part-2

# example-4: using if:
b = [i for i in range(1, 20) if i % 3 == 0]
print(b)

# example-5: nested if:
# if & if here act like AND, not OR
b = [i for i in range(1, 20) if i%3 == 0 if i%5 == 0]
print(b)

# example-6: nested if-else:
b = ["even" if i%2 == 0 else "Odd" for i in range(20)]
print(b)

# .................... 2D list comprehension

# convert matrix to transpose matrix
matrix = [[1, 2], [3,4], [5, 6], [7, 8]]
res = [[col[row] for col in matrix] for row in range(2)]
print(res)

# breakdown:
# a = []
# for row in range(2):
#   b = []
#   for col in matrix:
#       b.append(col[row])
#   a.append(b)
# print(a)