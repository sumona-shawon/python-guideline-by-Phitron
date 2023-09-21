# .................... for loop vs while loop

# for loop:
for i in range(10):
    print(i) # 0, 1, 2, 3, 4, 5, 6, 7, 8, 9

# while loop:
i = 0
while i <= 10:
    i = i + 1
    print(i) # 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11

# .................... range function with list

# can't use range in while loop
# without for loop:
list = list(range(10))
print(list) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# with for loop:
for list in range(10):
    print(list) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# .................... parameters in range function (start, end, step)

r1 = list(range(5)) 
r2 = list(range(2, 5))
r3 = list(range(1, 10, 3))
r4 = list(range(-5, 10, 3))

print(r1) # [0, 1, 2, 3, 4]
print(r2) # [2, 3, 4]
print(r3) # [1, 4, 7]
print(r4) # [-5, -2, 1, 4, 7]

# .................... more about for loop

# letter:
m1 = "Hello World"
for letter in m1:
    print(letter) # display every letter

# item:
m2 = ["alu", "peyaj", 3, 2.5, -1, 0]
for item in m2:
    print(item) # display every item

# filter:
m3 = [12, 45, 7, -2, 4, 5, 6]
for i in m3:
    if i <= 10:
        print(i) # 7, -2, 4, 5, 6

# divisible number:
for i in range(50):
    if i % 3 == 0 and i % 5 == 0:
        print(i) # 0, 15, 30, 45

# sum:
sum = 0
for i in range(1, 11):
    sum = sum + i # update variable
print(sum) # 55

# .................... break vs continue

# with for loop:
for i in range(10):
    if i == 5:
        break
    print(i) # 0, 1, 2, 3, 4

for i in range(10):
    if i == 5:
        continue
    print(i) # 0, 1, 2, 3, 4, 6, 7, 8, 9

# with while loop:
a = 0
while a <= 10:
    a = a + 1
    if a == 5:
        break
    print(a) # 1, 2, 3, 4

a = 0
while a <= 10:
    a = a + 1
    if a == 5:
        continue
    print(a) # 1, 2, 3, 4, 6, 7, 8, 9, 10, 11
    # 11 = increments before printing

# .................... infinite loop

# can't run infinite loop with for loop
a = 10
while a == 10:
    print(a) # prints continuously

# another/better way:
while True:
    print("I love Python") # prints continuously

# stops infinite loop in a particular area:
while True:
    b = input("Enter your name : ")
    if b == "Quit" or b == "q":
        break
    print("Hello", b, "good morning.")
    # stops when Quit or q is entered