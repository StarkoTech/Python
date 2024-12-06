# Comparison Operators: ==, !=, <, >, <=, >=.
# Logical Operators: and, or, not.

x = 20
if x > 15:
    print("x is greater then 15")
elif x > 5:
    print("x is greater than 5 but not greater then 15")
else:
    print("x is 5 or less")

y = 20
z = 40
if x > 5 and y > 15:
    print("Both conditions are true")

x = 20
if x > 10:
    if x < 30:
        print("x is between 10 and 30")

#Exercises
#1 Simple Condition: write program to cheack if a number is positive, or zero.
x = int(input("Enter the Number: "))
if x > 0:
    print("Number is Positive")
elif x == 0:
    print("Number is Zero")
else:
    print("Number is Negative")

#2 Write a program that asks the user for their age and print:
   # "Child" if age is less than 12
   # "Teenager" if age is between 12 and 19.
   # "Adult" if age is 20 or more.
age = int(input("Inter Your Age: "))
if 0 < age < 12:
    print(f"Your age is {age} you are a Child")
elif 12 < age < 19:
    print(f"Your age is {age} you are a Teenager")
elif age >= 20:
    print(f"Your age is {age} you are a Adult")
else:
    print("Invalid Age Intered")
