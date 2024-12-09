#funtion and parameters
def greet(name):
    print(f"Hello, welcome to Python! {name}")

greet("Alice")
greet("Bob")

#return values
def add(a, b):
    return a + b

result = add(5, 3)
print(result)

#Default Parameters
def greet(name="Guest"):
    print(f"Hello, {name}!")

greet("Alice")
greet()

#keyword arguments
def introduce(name, age):
    print(f"My name is {name}, and I am {age} year old.")

introduce(age = 30, name = "Alice")

#Exercises
#1 Basic Funtion: write a function square(num) that returns the square of a number.
def square(num):
    return num ** 2
    
Sq = square(3)
print(f"Square of the number is: {Sq}")

#2 Greeting Functino: write a function greet_user(name, age) that takes a user name and age and print: "Hello [name]! You are [age] years old."
def greet_user(name, age):
    print(f"Hello {name}! Your are {age} year old.")

greet_user("Suraj", 28)

#Calculator: write calculate(a, b, operator) that performs addition, substraction, multiplication, or division based on the oprator passed.
def calculate(a, b, op):
    if op == "+":
        add = a + b
        print(f"Addition of {a} and {b} is: {add}")
    elif op == "-":
        sub = a - b
        print(f"Substraction of {a} and {b} is: {sub}")
    elif op == "*":
        mul = a * b
        print(f"Multiplication of {a} and {b} is: {mul}")
    elif op == "/":
        div = a / b
        print(f"Division of {a} and {b} is: {div}")
    else:
        print("You Enterd Invalied Oprator")

calculate(5, 3, "+")
calculate(5, 3, "-")
calculate(10, 2, "*")
calculate(10, 2, "/")    

#4 Even or Odd Checker: write a function is_even(number) thet returns True if the number is even, and False if it's odd.
number = int(input("Enter the number: "))
def is_even(number):
    if number % 2 == 0:
        print(f"{number} is Even Number")
    else:
        print(f"{number} is Odd Number")

is_even(number)