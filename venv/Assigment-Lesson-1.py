# exercise A
# 1. Create a variable name first with value 7.
first = 7
# 2. Create a variable name second with value 44.3.
second = 44.3
# 3. Print result of adding first to second.
print(first + second) # 51.3
# 4. Print result of multiplying first by second
print(first * second) # 310.0999
# 5. Print result of dividing second by first
print(second / first) # 6.3

# ------------------------------------------
# exercise B
# What will be the value of a, b, c at the end?
a = 8
a = 17
a = 9
b = 6
c = a+b
b = c+a
b = 8

# Answer:
a = 9
b = 8
c = 15

# ------------------------------------------
# exercise C
# Is there difference between the two line below? Why?
name = "jone"
name = 'jone'
# Answer: Both are str because there is no difference when used " or '

# What is the issue with the code below?
# my_number = 5+5
# print("result is: "+my_number)
# Answer:
# there is no option to concatenate str with int only str with str
# suggest an edit:
my_number = 5+5
print(f"result is: {my_number}")

# ------------------------------------------
# exercise D
# what will be output
x = 5
y = 2.3
print(x + int(y))
# Answer: 7

# ------------------------------------------
# exercise E
# 1. Create two variables name X and Y.
# 2. Print “BIG” if X is bigger than Y .
# 3. Print “small” if X is smaller than Y.
x = 2
y = 7
if x > y:
    print("BIG")
elif x < y:
    print("small")

# ------------------------------------------
# exercise F
# 1. Create a variable and initialize it with a number 1-4.
# 2. Create 4 conditions (if-elif) which will check the variable.
# 3. print the season name accordingly:
# - 1 = summer
# - 2 = winter
# - 3 = fall
# - 4 = spring
season = 1
if season == 1:
    print("summer")
elif season == 2:
    print("winter")
elif season == 3:
    print("fall")
elif season == 4:
    print("spring")

# ------------------------------------------
# CHALLENGE exercise
# Fix the following code, without changing a or b
# a = 8
# b = "123"
# print(a+b)
# fixed code:
a = 8
b = "123"
print(a+int(b))
# or
print(str(a)+b)


# ------------------------------------------
# EXTRA Exercise #1
# create 2 vars, with the value: "5" and 5
number = 5
string = "5"

# save the boolean result of the comparsion of the above vars
result = number == string  # False

# sum the two vras
number + int(string)  # 10
# or
str(number) + string  # 55

# check if 5 is larges then 5.5
five = 5
five_dot = 5.5
five > five_dot  # False

# check if True is False
true = True
false = False
true == false  # False

# check if "hello" is larges then "helloo"
hello = "hello"
helloo = "helloo"
hello > helloo  # False

# ---------------------------------------
# EXTRA Exercise #2
# recive from a user 3 input Name, Age, Work
# check if the name start with "A"
# check if Age is number(integer)
# if the Name is not start with "A", keep asking for the name input
name = input("Enter Your Name:")
try:
    age = int(input("Enter YourAge:"))
except ValueError:
    print("age is not an integer!")

work = input("Enter YourWork:")
while name[:1] != 'A':
    name = input("Enter Name:")

