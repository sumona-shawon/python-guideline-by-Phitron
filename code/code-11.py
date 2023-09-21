# .................... declare string

a = 'Hello Rina'
a = "Hello Rina"
c = ''' This is a multi line string.
    This isn't a multi line comment,
    as it has been saved in a variable named c '''

# .................... indexing

# get element:
a = "Hello world"
print(a[0]) # positive: H
print(a[-1]) # negative: d

# .................... immutable
a[-1] = "D" 
print(a) # error
# doesn't support assignment operator
# can't change a string

# .................... print elements:

a = "Hello world"

# way-1:
for i in a:
    print(i)
    print(i, end = " ") # prints in a line

# way-2:
for i in range(len(a)):
    print(a[i])
    print(a[i], end = " ") # prints in a line

# .................... case related methods:

a = "hello world PYTHON ẞ"

b = a.lower()
print(b)
# hello world python ß
# converts string to lowercase

c = a.upper()
print(c)
# HELLO WORLD PYTHON ẞ
# converts string to uppercase

d = a.title()
print(d)
# Hello World Python ẞ
# words start with uppercase, rest are lowercase

e = a.capitalize()
print(e)
# Hello world python ß
# first character is uppercase, rest are lowercase

f = a.swapcase()
print(f)
# HELLO WORLD python ß
# converts uppercase to lowercase & vice-versa

g = a.casefold()
print(g)
# hello world python ss
# string to lowercase, but works in other languages too

# .................... check type:

a = "hello"
b = "HELLO"
c = "Hello"
d = "15"
print(a.islower())
print(b.isupper())
print(c.istitle()) 
print(d.isdigit())

# .................... replace string:

a = "Hollo"
b = a.replace(a[1], 'e') # replace all
c = a.replace('o', 'e') # replace all
d = a.replace('o', 'e', 1) # replace specific times

print(b) # Helle
print(c) # Helle
print(d) # Hello

# .................... string/list conversion:

# join (works on string):
a = ["h", "e" "l", "l", "o", "1", "0", "0"] 
print("".join(a)) # hello100

# list vs split:
a = "hello"
print(list(a)) # ['h', 'e', 'l', 'l', 'o']
print(a.split()) # ['hello']