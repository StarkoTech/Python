# 1. Variables and Data Types
# 1. Write a program to store your name, age, and country in variables and print them.
'''
name = "Suraj"
age = 28
country = "India"
print(name, age, country)
'''
# 2. Wirte a program to swap the values of two variables wityhout a third variable.
'''
a = 10
b = 20
b, a = a, b
print(a, b)
'''
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
'''
string = "Hello World"
print(string[::-1])
'''
# Explination: The slicing [::] allows you to define the start, stop and step. By using [::-1], you reverse the string.

# 6. Write a program  to reverse a string using a loop.
'''
string = "World Hello"
rev_str = ""
for char in string:
    rev_str = char + rev_str
print(rev_str)
'''
# Explination: Each character is added in reverse order to the new string.

# 7. Write a program to reverse a string using a reverse() and join() method.
'''
string = "Suraj Mahajan"
reversed_string = ''.join(reversed(string))
print(reversed_string)
'''
# Explination: The reversed() funtion creates a reversed iterator, and join() combines the elements into a single string.

# 8. Write a program to reverse a string using Recursion (Advanced).
'''
def reverse_string(string):
    if len(string) == 0:
        return string
    return string[-1] + reverse_string(string[:-1])

string = "Hello"
reversed_string = reverse_string(string)
print(reversed_string)
'''
# Explination: The funtion calls itself, taking the last character and addinf it to the reversed substring.

# 9. Write a program to reverse a string using a while loop.
'''
string = "My Name is Khan"
revers_string = ""
index = len(string) - 1

while index >= 0:
    revers_string = revers_string + string[index]
    index = index -1

print(revers_string)
'''
# Explination: A while loop iteraes from the last index to the first, building the reversed string.

# 4. Oprators
# 10. Write a program to check if a number entered by the user is divisible by both 3 and 5.
'''
num1 = int(input("Enter the Number: "))
if num1 % 3 == 0 and num1 % 5 == 0:
    print("Number is Divisible By 3 and 5.")
else:
    print("Number is not Divisible By 3 and 5.")
'''
# 11. Write a program to calculate the aera of a circle given the radius (use pi = 3.14).
'''
radius = float(input("Enter the radius of the circle:"))
area = 3.14 * radius**2
print(f"The Area of circile with the radius {radius} is {area}")
'''
# 5. Control Flow
# 12. Write a program to check if a number entered by user is positive, negative or zero.
'''
num = int(input("Enter the Number: "))
if num > 0:
    print("Number is Positive.")
elif num < 0:
    print("Number is Negative.")
else:
    print("Number is Zero.")
'''
# 13. Write a program to find the largest of three numbers entered by the user.
'''
num1 = int(input("Enter First Number:"))
num2 = int(input("Enter Second Number: "))
num3 = int(input("Enter Third Number: "))

if num1 > num2 and num1 > num3:
    print(f"{num1} is Largest Number.")
elif num2 > num1 and num2 > num3:
    print(f"{num2} is Largest Number.")
else:
    print(f"{num3} is Largest Number.")
'''
