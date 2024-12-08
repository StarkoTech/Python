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
