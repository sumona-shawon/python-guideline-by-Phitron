# .................... nested loop

# end parameter prints in a single line:

for i in range(1, 6):
    for j in range(1, 6):
        print(i * j, end = " ")
    print()

    # 1 2 3 4 5
    # 2 4 6 8 10
    # 3 6 9 12 15
    # 5 10 15 20 25

# .................... pattern printing

# problem 1:

for row in range(8):
    for col in range(row):
        print("#", end = ' ')
    print()

    # 
    # # 
    # # #
    # # # #
    # # # # #
    # # # # # #
    # # # # # # #

# problem 2:

# need ASCII to write alphabets
# chr prints alphabet (65 = A, 97 = a)

for row in range(5):
    for col in range(row + 1):
        print(chr(97 + row), end = " ")
    print()

    # a
    # b b
    # c c c
    # d d d d
    # e e e e e

# .................... traversing nested list

bazar_list = [["alu", "peyaj"], [12, 15, 20], ["pizza", 2.5, 30]]

for item in bazar_list:
    for mini_item in item:
        print(mini_item)
        # displays every item