#write a program to calculate the sum of all numbers from 1 to 100 using a for loop.
sum1 = 0
for sum in range(1, 101):
    sum1 = sum + sum1
print(sum1)

#Factorial: write a program to find the factorial of a number(e.g., 5! = 5 * 4 * 3 * 2 * 1).
num = int(input("Enter the Number: "))
num1 = 1
for i in range(num+1):
    if i > 0:
        num1 = i * num1
        i += 1
     
print(f"The Factorial Of {num} is {num1}")
