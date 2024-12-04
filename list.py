# write a program to find the largest number in a list.
Number_list = [23, 45, 12, 67, 34, 89, 21]
 
largest_Num = max(Number_list)
print("The Largest Number is: ", largest_Num)

# without max()
largest = Number_list[0]
for num in Number_list:
    if num > largest:
        largest = num
print("The largest number is: ", largest)