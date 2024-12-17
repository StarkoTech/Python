file = open("example.txt", "r")
content = file.read()
print(content)
file.close()


file = open("example.txt", "w")
file.write("Hello, this is a test.\n")
file.write("Another line here.\n")
file.close()

file = open("example.txt", "a")
file.write("This is appended test. \n")
file.close

with open("example.txt", "r") as file:
    content = file.read()
    print(content)
    

#exercises
#1 file reader: write a program that reads a file called dada.txt and prints its content line by line.
file = open("data.txt", "r")
content = file.read()
print(content)
file.close()

# Reading line by line: Create a file log.txt and write a log message like: "Log entry at [current timestamp]".
file = open("data.txt", "r")
for line in file:
    print(line.strip())
file.close

# Word Counter: Write a program that counts the number of words in a text file sample.txt.
file = open("data.txt", "w")
file.write("1.Python Basics:\n")
file.write("Variables, Data Types, Input/Output, Basic Operators.\nTime: ~2-3 days.\n")
file.close()

# Copy Content: write a program to copy the content of one file (source.txt) to another (destination.txt).
file = open("data.txt", "a")
file.write("This is appended text.\n")
file.close()

# using with statement
with open("data.txt", "r") as file:
    content = file.read()
    print(content)
    