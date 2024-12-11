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

with open("example.txt", "r"):
    content = file.read()
    print(content)
