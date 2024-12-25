# 1. Variables and Data Types
# 1. Write a program to store your name, age, and country in variables and print them.
name = "Suraj"
age = 28
country = "India"
print(name, age, country)

# 2. Wirte a program to swap the values of two variables wityhout a third variable.
a = 10
b = 20
b, a = a, b
print(a, b)

# 2. Basicx Input and Output
# 3. Write a program that asks the user for their name and print a personalized greeting.
'''
name = input("Enter Your Nmae: ")
print("Hello!",name,", Wecome To Python Programming.")
'''

# 4. Write a program that takes inpute for two numbers and print their sum, difference, product and quotient.
'''
num1 = int(input("Enter First Number: "))
num2 = int(input("Enter Second Number: "))
sum = num1 + num2
diff = num1 - num2
prod = num1 * num2
quot = num1/ num2
print(f"Sum of Two Numbers is {sum}")
print(f"Difference of Two Numbers is {diff}")
print(f"Product of Two Numbers is {prod}")
print(f"Quotient of Two Numbers is {quot}")
'''

# 3. Stinrgs 
# 5. Write a program to reverse a string using slicing.
string = "Hello World"
print(string[::-1])
# Explination: The slicing [::] allows you to define the start, stop and step. By using [::-1], you reverse the string.

# 6. Write a program  to reverse a string using a loop.
string = "World Hello"
rev_str = ""
for char in string:
    rev_str = char + rev_str
print(rev_str)

# 7. Write a program to check if a string using a reverse() and join() method.
