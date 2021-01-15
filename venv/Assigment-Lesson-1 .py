# exercise A
first = 7
second = 44.3
print(first + second)
print(first * second)
print(second / first)

# exercise B
a = 8
a = 17
a = 9
b = 6
c = a+b
b = c+a
b = 8

# result:
a = 9
b = 8
c = 15

# exercise C
name = "jone"
name = 'jone'

# Both are str because there is no difference when used " or '
my_number = 5+5
# print("result is: "+my_number)
# Answer:
# there is no option to concatenate str with int only str with str
# suggest
my_number = 5+5
print(f"result is: {my_number}")

# exercise D
x = 5
y = 2.3
print(x + int(y))
# output: 7


# exercise E
x = 2
y = 7
if x > y:
    print("BIG")
elif x < y:
    print("small")

# exercise F
season = 1
if season == 1:
    print("summer")
elif season == 2:
    print("winter")
elif season == 3:
    print("fall")
elif season == 4:
    print("spring")

# exercise CHALLENGE
a = 8
b = "123"
print(a+int(b))
# or
print(str(a)+b)


# ------------------------------------------
# EXTRA Exercise #1
# 1
number = 5
string = "5"

# 2
result = number == string  # False

# 3
number + int(string)  # 10
# or
str(number) + string  # 55

# 4
five = 5
five_dot = 5.5
five == five_dot  # False

# 5
true = True
false = False
true == false  # False

# 6
hello = "hello"
helloo = "helloo"
hello > helloo  # False

# ---------------------------------------
# EXTRA Exercise #2
name = input("Enter Your Name:")
try:
    age = int(input("Enter YourAge:"))
except ValueError:
    print("age is not an integer!")

work = input("Enter YourWork:")
while name[:1] != 'A':
    name = input("Enter Name:")

