# .................... problem-1

a = int(input("Enter the length of the rectangle"))
b = int(input("Enter the breadth of the rectangle"))
if a == b:
    print("This is a square")
else:
    print("This is a rectangle")

# .................... problem-2 

a = int(input())
b = int(input())
c = int(input())

# nested if concept:

if a >= b:
    if a >= c:
        print(a, "is the largest number")
    else:
        print(c, "is the largest number")
else:
    if b >= c:
        print(b, "is the largest number")
    else:
        print(c, "is the largest number")

# using logical operators:

if a >= b and a >= c:
    print(a, "is the largest number")
elif b >= a and b >= c:
    print(b, "is the largest number")
else:
    print(c, "is the largest number")

# .................... problem-3

a = int(input())
if a % 2 == 0:
    print(a, "is an even number")
else:
    print(a, "is an odd number")

# .................... problem-4

marks = int(input("Enter your marks: "))
if marks > 90:
    print("Your Grade is A")
elif marks > 80 and marks <= 90:
    print("Your Grade is B")
elif marks >= 60 and marks <= 80:
    print("Your Grade is C")
else:
    print("Your Grade is D")

# .................... problem-5

year = int(input())

# method-1:

if year % 400 == 0:
    print("leap year")
elif year % 100 == 0:
    print("not leap year")
elif year % 4 == 0:
    print("leap year")
else:
    print("not leap year")

# method-2:

if year % 400 == 0 and year % 100 == 0:
    print("leap year")
elif year % 4 == 0 and year != 0:
    print("leap year")
else:
    print("not leap year")