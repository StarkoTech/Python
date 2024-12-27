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
# 6. Loops
# 14. Write a program to print all even numbers between 1 to 50.
'''
for i in range(1,51):
    if i % 2 == 0:
        print(i)
'''
# 15. Write a program to calculaate the factorial of a number entered by the user.
'''
num = int(input("Enter the Number: "))
n = 1
for i in range(1, num+1):
    n = n * i
print(f"The Factorial of {num} is {n}")
'''
# 16. using while loop
'''
num = int(input("Enter the Number: "))
n = 1
while num > 0:
    n = n * num
    num = num - 1
print("The Factorial of Number is",n)
'''
# 7. Lists
# 17. Write a program to create a list of 5 numbers entered by user and print the list.
'''
Number_list = []
for i in range(5):
    num = float(input(f"Enter Number {i+1}:"))
    Number_list.append(num)
print("The list of number is", Number_list)

# 18. Write a program to find the maximum and minimun nummber in a list.
max_num = Number_list[0]
min_num = Number_list[0]
for i in Number_list:
    if i > max_num:
        max_num = i
    if i < min_num:
        min_num = i
print(f"The Maximum nunmber in the {Number_list} list is {max_num}")
print(f"The Minimum number in the {Number_list} list is {min_num}")
'''
# 8. Dictionaries
# 19. Write a program to create a dictionary with keys as subjects (e.g. Math, Scince) and values as marks. Print the subjecct with the highest marks.
'''
Dictionary = {"Math": 90, "Science": 80, "English": 70, "History": 85}
max_marks = max(Dictionary.values())
for key, values in Dictionary.items():
    if values == max_marks:
        print(f"The Subject with Highest Marks is {key} with {values}")

# 20. Without loop
Marks_Dict = {"Math": 85, "Scince": 90, "English": 78, "History": 88}
Highest_subject = max(Marks_Dict, key=Marks_Dict.get)
Highest_marks = Marks_Dict[Highest_subject]
print(f"The Subject with Highest Marks is {Highest_subject} with {Highest_marks}")
'''
# 20. Write a program to count the occurrences of each word in a given sentence.
# Input snentece
sentence = "Hello World, Hello Python, Hello World"
# Split the sentence into words by spaces
words = sentence.split()
# Create an empty dictionary to store the count of each word
words_count = {}
# loop through each word in the list of words
for i in words:
    # if word is already in the dictionary, increment its count
    if i in words_count:
        words_count[i] = words_count[i] + 1
    #if the word is not in the dictionary, add it with a count of 1
    else:
        words_count[i] = 1
    # Print the count of each word

for i, count in words_count.items():
    print(f" {i} appears {count} times in the sentence.")
