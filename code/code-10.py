# .................... swap two list elements

a = [11, 12, 13, 15, 16, 10]
temp = a[0] # saves to new variable before any changes

# a[len(a)] - 1 or,
a[0] = a[-1] # 11 = 10
a[-1] = temp # 10 = 11

print(a) # [10, 12, 13, 15, 16, 11]

# .................... count unique element in an list

a = [1,2,2,3,3,3,4,5,6]
b = []
count = 0

for i in a:
    if i not in b: # if not present in b then add, otherwise ignore
        count += 1 # counting every time after adding a value
        b.append(i) # adds according to condition: [1,2,3,4,5,6]

print(count) # 6 (total unique value)

# .................... extract elements from a list

test_list = [4, 6, 4, 3, 3, 4, 3, 4, 3, 8]
k = 3
res = []

for i in test_list:
    freq = test_list.count(i) # counts during iteration
    if freq > k and i not in res: # adds i if freq>3 & not already present in res
        res.append(i) # 4=4>3, 6=1<3, 3=4>3, 8=1<3
print(res) # [4, 3]

# .................... create list using list comprehension

a = [[j for j in range(5) if i!=j] for i in range(5)]
print(a)

# 1st iteration = i in range(5) / outer list
# 2nd iteration = j in range(5) / inner list
# during the inner loop: (i=j) = ignored element (prints the rest)