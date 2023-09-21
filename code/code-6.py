# .................... 1. multiplication table

a = int(input("Enter a number : "))

for i in range(1, a + 1):
    print(a, " X ", i, " = ", a * i)

# .................... 2. factorial of a number

a = int(input("Enter a value : "))
factorial = 1

for i in range(1, a + 1):
    factorial = factorial * i 
    # factorial *=i (shortcut)
print(factorial)

# .................... 3. fibonacci series

a = 0
b = 1
# a, b = 0, 1 (shortcut)

for i in range(10):
    print(a, end = " ")
    result = a + b
    a = b
    b = result
print(a) # 0 1 1 2 3 5 8 13 21 34 55

# .................... 4. count numbers digit in a number

# method 1:

a = int(input())
count = 0

while a > 0:
    count = count + 1
    a = a // 10
print(count)

# % = remainder
# / = quotient (floating point, 5/2=2.5)
# // = quotient (floor division, 5//2=2)
# dividend % 10 (last digit)
# dividend / 10 (all digit except last one)

# method 2:

b = input() # len doesn't work on int
print(len(b)) # len function prints length

# .................... 5. armstrong number

# armstrong number = digit1ⁿ + digit2ⁿ... = equal to given number (ⁿ=length)

# method 1:

a = int(input())
num_len = len(str(a))
temp = a
sum = 0

while temp > 0:
    last_digit = temp % 10
    sum = sum + last_digit ** num_len
    temp = temp // 10 
    # temp //= 10 (shortcut)

if sum == a:
    print("armstrong number")
else:
    print("not armstrong number")

# method 2:

a = input()
num_len = len(a)
sum = 0

for i in a:
    sum = sum + int(i) ** num_len
    # sum += int(i) ** num_len (shortcut)

if int(a) == sum:
    print("armstrong number")
else:
    print("not armstrong number")

# .................... 6. reverse a number

a = int(input())
rev_a = 0

while a > 0:
    last_digit = a % 10
    rev_a = rev_a * 10 + last_digit
    a //= 10
print(rev_a)