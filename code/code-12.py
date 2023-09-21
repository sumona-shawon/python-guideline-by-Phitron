# .................... string formatting (immutable to dynamic)

# method 1 (format):

name = "Rahim"
age = 20

template_string = "I am {}. I am {} years old.".format(name, age)
print(template_string)

template_string = "I am {1}. I am {0} years old.".format(age, name)
print(template_string)

template_string = "I am {first_name}. I am {user_age} years old.".format(user_age = 25, first_name = 'Karim')
print(template_string)

# method 2 (f-strings):

name = "Rahim"
age = 20

string = f"I am {name}. I am {age} years old."
print(string)

string = f"I am {name}. I am {age+5} years old."
print(string)

# .................... string concatenation (add to strings)

# add two strings:
a = "Hello"
b = "xyz"
c = a + " " + b
print(c)

# print multiple times:
print("Hi" * 3)
print(("Hi" + " ") * 3)

# .................... string sorting

# input a2b1c3, output aabccc

a = input()
res = ""

for i in range(0, len(a), 2):
    # res = res + a[i]
    print(f"{a[i]} {a[i+1]}")
    res = res + a[i] * int(a[i+1])

result = sorted(res, key=str.casefold)
res_string = "".join(result) # list to string
print(res_string)

# .................... palindrome string checking

a = input("Enter string : ")

if a == a[::-1]:
    print("Yes")
else:
    print("No")

# .................... string reversing using list

a = input("")
a = a.split(" ")
print(a)
result = ""

for i in a:
    result += i[::-1] + " "
print(result)