# .................... Comment
# This is single line comment.
"""
This is multi-line comment.
Python will ignore it.
"""

# .................... if statement:
a = 5
b = 2
if a > b:
    print("a is greater than b")

# .................... if-else statement:
rain = True
if rain == True:
    print("School e jabo na.")
else:
    print("School e jabo.")

# .................... if-elif-else statement:
print(10-4 == 6 and 10-5 == 15) # False
print(10-4 == 6 or 10-5 == 15) # True
print(not (10-5 == 15)) # True

# .................... problem:
marks = 85
if marks >= 90 and marks <= 100:
    print("2 ta candy pabe")
elif marks >= 80 and marks <= 89:
    print("1 ta candy pabe")
else:
    print("kichu e pabe na")

# .................... Typecasting
age = int(input())
weight = float(input())
# str and int can't be compared so used int, float

if age >= 18:
    print("you are adult")
else:
    print("you are child")

print(weight)
print(int(weight))
print(type(weight)) # check type

new_weight = int(weight)
print(new_weight)
print(type(new_weight)) # display int

new_new_weight = float(new_weight)
print(new_new_weight)
print(type(new_new_weight)) # display float

# .................... problem-1
length = int(input())
breadth = int(input())
if length == breadth:
    print("It's a square")
else:
    print("It's not a square")

# .................... problem-2
a = int(input())
b = int(input())
c = int(input())
if a > b and a > c:
    print("a is the largest number")
elif b > a and b > c:
    print("b is the largest number")
else:
    print("c is the largest number")

# .................... problem-3
num = int(input())
if num % 2 == 0:
    print(num, "is even")
else:
    print(num, "is odd")

# .................... problem-4
mark = int(input())
if mark > 90:
    print("your grade is A")
elif mark > 80 and mark < 90:
    print("your grade is B")
elif mark >= 60 or mark <= 80:
    print("your grade is C")
else:
    print("your grade is D")

# .................... problem-5
year = int(input())
if (year % 400 == 0 and year % 100 == 0):
    print(year, "is a leap year")
elif (year % 4 == 0 and year % 100 != 0):
    print(year, "is a leap year")
else:
    print(year, "is not a leap year")