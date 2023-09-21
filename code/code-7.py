# .................... problem 1

n = int(input())

for row in range(n):
    if row % 2 == 0:
        result = 1
    else:
        result = 0
    for col in range(row + 1):
        print(result, end = " ")
        if result == 1:
            result = 0
        else:
            result = 1
    print()

# .................... problem 2

n = int(input())

for row in range(1, n+1):
    for col in range(row):
        print('*', end = ' ')
    print()

for row in range(n):
    for col in range(row, n-1):
        print('*', end = ' ')
    print()

# .................... problem 3

a = int(input())

for i in range(1, a + 1):
    print(a*i, end = ' ')

# .................... problem 4

a = input()
sum = 0

for i in a:
    sum = sum + int(i)
print(sum)

# .................... problem 5

a = input()
num_len = len(a)
sum = 0

for i in a:
    sum = sum + int(i) ** num_len
print(sum)

# .................... extra: tried to explore

# single digit sum
a = input()
sum = 0
for i in a:
    sum = sum + int(i)

if sum >= 10:
    b = str(sum)
    sum2 = 0
    for j in b:
        sum2 = sum2 + int(j)
    print(sum2)
else:
    print(sum)