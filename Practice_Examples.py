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

#Guessing Game: write a program where the user has to guess a secret number between 1 and 10.
#Keep askking until they guess correstly.
#Use a while loop.
secretnum = ""
while secretnum != "2":
    secretnum = input("Guess a secret number between 1 and 10, Enter Number:  ")
print("Your guess is correct, secret number is 2")



#Multiplication Table: usee nested loops to prinit the multiplication table from 1 to 10.

for i in range(1, 11):
    for j in range(1, 11):
        mul = i * j
        print(mul)
    print("\n")    



