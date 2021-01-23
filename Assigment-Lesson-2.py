# exercise A
# Create two variables name X and Y.
# Print “BIG” if X is bigger than Y .
# Print “small” if X is smaller than Y.
x = int(input("Enter Number:"))
y = int(input("Enter Number:"))
if x > y:
    print("BIG")
elif x < y:
    print("small")

# ------------------------------------------
# exercise B
for i in range(1, 6):
    print(i)

# ------------------------------------------
# exercise C
# 1. Create a variable and initialize it with a number 1-4.
# 2. Create 4 conditions (if-elif) which will check the variable.
# 3. print the season name accordingly:
# - 1 = summer
# - 2 = winter
# - 3 = fall
# - 4 = spring
season = int(input("Enter Number [1-4]:"))
if season == 1:
    print("summer")
elif season == 2:
    print("winter")
elif season == 3:
    print("fall")
elif season == 4:
    print("spring")
else:
    print("wrong number!!")

# ------------------------------------------
# exercise D
# 1. how many times will the following loop run?  10
# 2. what will be printed last? 10

# ------------------------------------------
# exercise E
# Write a program with variables holding the following:
# 1. Your age.
# 2. First letter of your last name.
# 3. Current shekels-dollar currency.
# 4. Did you flew abroad (true/false)
# 5. Your apartment number.
# Print all variables.
# Add the currency to your age, and check the result.
age = int(input("Enter Your age:"))
lastName = input("Enter last name:")
currency = float(input("Enter Current shekels-dollar currency:"))
flewAbroad = bool(input("Did you flew abroad  (true/false):"))
apartmentNum = int(input("Enter Your apartment number:"))
print(f"Your age: {age}, First letter of your last name: {lastName[0]}")
print(f"current shekels-dollar currency:: {currency}, flew abroad: {flewAbroad}")
sumAge = age + currency
print(f"age + currency = {sumAge}")

# ------------------------------------------
# exercise F
# Create a program which uses input with the following:
# 1. Ask user for his phone number
# 2. Print the words “phone number” and the phone number the user entered.
phoneNumber = input("Enter your phone number:")
print(f"phone number: {phoneNumber}")


# ------------------------------------------
# exercise G
# Write a program with the following:
# 1. Method named printHello() that prints the word “hello”.
# 2. Method named calculate() which adds 5+3.2 and prints the result.
def printHello():
    print("hello")


def calculate():
    print(5 + 3.2)


printHello()
calculate()

# ------------------------------------------
# exercise H
# Write a program with the following:
# 1. Method that receive your name and prints it.
# 2. Method that receive a number, divide it by 2, and prints the result.
inputNumber = int(input("Enter number:"))
inputName = input("Enter name:")


def getName(name):
    print(f"your name: {name}")


def divideNumber(number):
    print(f"{number} - 2 = ", number - 2)


getName(inputName)
divideNumber(inputNumber)

# ------------------------------------------
# exercise I
# Write a program with the following:
# 1. Method that receive two numbers, add them, and return the sum.
# 2. Method that receive two Strings, add space between them, and return one spaced string.
num1, num2 = map(int, input("Enter two numbers: ").split())
str1, str2 = map(str, input("Enter two string:").split())


def num_sum(number1, number2):
    return int(number1) + int(number2)


def str_add_space(string1, string2):
    return string1 + " " + string2


print(f"{num1} + {num2} = ", num_sum(num1, num2))
newString = str_add_space(str1, str2)
print(f"new string {newString}")

# ------------------------------------------
# Challenges:
# ------------------------------------------
# exercise K
# Create a nested for loop (loop inside another loop) to create a pyramid shape:
for i in range(1, 8):
    for x in range(i):
        print("#", end=" ")
    print("")

# ------------------------------------------
# exercise L
# Create a nested for loop to create X shape (width is 7, length is 7):
i = 0
j = 6
for width in range(7):
    for length in range(7):
        if length == i or length == j:
            print("*", end="")
        else:
            print(" ", end="")

    print("")
    i += 1
    j -= 1


# ------------------------------------------
# exercise M
# Write a program with the following:
# 1. Method that gets a number from the user (using input).
# 2. Method that receive the number from the first method, and
#    computes the sum of the digits the integer (e.g. 25 = 7, 2+5=7)

def get_number():
    return input("Enter Number:")


def sum_digits(number):
    sum_dig = 0
    for j in range(len(number)):
        sum_dig += int(number[j])
    return sum_dig


num = get_number()
total_digits = sum_digits(num)
print(f"total digits: {total_digits}")

# ------------------------------------------
# Extra exercise 1
count = 0
while count < 5:
    print(count)
    count += 1
else:
    print("count value reached {count}".format(count=count))

for i in range(1, 10):
    if i % 5 == 0:
        break
    print(i)
else:
    print("this is not printed because for loop is terminated because of break but not due to fail in condition")

# print number 1 to 4 and 'count value reached 5' because the will loop is terminated 6 < 5
# then print 1 to 4  and not print the else because the break in the if , the for loop is not terminated


# ------------------------------------------
# Extra exercise 2
# 1. print the square of all number from 0 to 10
for num in range(0, 11):
    square = num ** 2
    print(f"square of {num} = {square}")

# 2. find the sum of all even number from 0 to 10
sum_num = 0
for num in range(1, 11, 2):
    sum_num += num
print(f"sum of all even number from 0 to 10 = {sum_num}")

# or
sum_num = 0
for num in range(0, 11):
    if num % 2 != 0:
        sum_num += num
print(f"sum of all even number from 0 to 10 = {sum_num}")

# 3. read three numbers (a,b,c) and check how many numbers between a and b are divisible by c
try:
    a, b, c = map(int, input("Enter three numbers: ").split())
except ValueError:
    print("numbers are not an integer!")

number = 0
for z in range(a, b):
    if z % c == 0:
        number += 1

print(f"there is {number} numbers between {a} and {b} are divisible by {c}")
