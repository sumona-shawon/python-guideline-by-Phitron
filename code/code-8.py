# .................... indexing

# check value:
a = [11, 15, 20, 1.5, "alu"]
print(a[4]) # alu

# replace value:
a[4] = "peyaj"
print(a[4]) # peyaj

# .................... types of indexing

a = [12, 20, 34, "Phitron"]

# positive indexing:
print(a[0]) # 12
# negative indexing:
print(a[-3]) # 20

# highest negative index = length
print(len(a)) # -4
print(a[-4]) # 12

# change/replace value:
a = [12, 20, 34, "Phitron"]
a[-3] = 500 # changed in memory
# checking if change was saved:
if 20 in a:
    print("Found")
else:
    print("Not Found")
# Found

# .................... traversing:
a = [12, 20, 34, "Phitron"]
# old way
for i in a:
    print(i) # 12, 20, 34, Phitron

# new way
for i in range(len(a)):
    print(a[i]) # 12, 20, 34, Phitron

for i in range(-1, -len(a)-1, -1):
    print(a[i]) # Phitron, 34, 20, 12

# .................... indexing in nested list
b = [[12, 13], [18, 23, "Phitron"], [-1, -19]]

# check value:
print(b[0][1]) # 13

# replace value:
b[0][1] = 500
print(b[0][1]) # 500

# .................... list slicing

a = [12, 13, 14, "Phitron", "Mango", [12.5, 19]]

print(a[::]) # prints full list
print(a[1::]) # skip 12
print(a[2::4]) # 14

print(a[::-1]) # reverse a list (new technique)
print(a[-1:-3:-1]) # negative index needs step: [[12.5, 19], 'Mango']
print(a[-1:-1:-1]) # empty list

# .................... list methods

# add two lists:
a = [1, 2, 3]
b = [4, 5, 6]
c = a + b
print(c) # [1, 2, 3, 4, 5, 6]

# string into list:

s = "Hello World!"
print(list(s)) # ['H', 'e', 'l', 'l', 'o', ' ', 'W', 'o', 'r', 'l', 'd', '!']

# append() = add element at the end of list:
a = [12, 24, 13, 45]
a.append(100)
a.append("Phitron")
print(a) # [12, 24, 13, 45, 100, 'Phitron']

# insert() = add element at specified position:
a = [1, 2, 3, 4, 5]
a.insert(2, 100)
a.insert(10, 200) 
# highest index = length
# anything higher will be added at last
print(a) # [1, 2, 100, 3, 4, 5, 200]

# copy() = copy the list:
a = [1, 2, 3, 4, 5]
b = a.copy()
# b = a # shortcut way
print(b) # [1, 2, 3, 4, 5]

# count() = count an element:
a = [1, 2, 2, 2, 2, 4, 5, 5, 6]
print(a.count(2)) # 4

# extend() = add multiple elements:
a = [12, 2, 5, 6]
a.extend([32, 90])
# a = a + [32, 90] # shortcut
print(a) # [12, 2, 5, 6, 32, 90]

# pop() = remove last element:
a = [1, 2, 3, 4, 5]
a.pop()
print(a) # [1, 2, 3, 4]

# remove() = remove particular element:
a = [1, 2, 3, 4, 5]
a.remove(4)
print(a) # [1, 2, 3, 5]

# clear() = remove all elements:
a = [1, 2, 3, 4, 5]
a.clear()
print(a) # []

# reverse() = reverse objects of list:
a = [1, 2, 3, 4, 5] # copy to keep this unchanged
# print(a[::-1]) # old
a.reverse()
print(a) # [5, 4, 3, 2, 1]

# sort() = sort the list:
a = [32, 0, -1, 3]
# a.sort() # ascending by default
# a.sort(reverse=False) # ascending
a. sort(reverse=True) # descending
print(a) # [32, 3, 0, -1]

# max() = maximum element:
a = [1, 2, 3, 4, 5]
print(max(a)) # 5