#use a lambda funtion and filter() to filter out even number from a list
number = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = filter(lambda x: x % 2 == 0, number)
print("Even number:", list(even_numbers))