set1 = {1, 2, 3}
set2 = {3, 4, 5, 6}
#Union (|)
print(set1 | set2)
#Intersection (&)
print(set1 & set2)
#Difference (-)
print(set1 - set2)
#Symmetric Difference (^)
print(set1 ^ set2)

#Remove Duplicates: Write a function remove_dumplicates(1st) that takes a list and return a list with duplicates removed using a set.
def remove_duplicates(lst):
    set1 = set(lst)
    print(set1)
remove_duplicates([1,2,2,3,4,4])

# Write a program to check if all elements of one list are present in another using sets.
def is_subset(list1, list2):
    set1 = set(list1)
    set2 = set(list2)

    return set1 <= set2

list1 = [1, 2, 3]
list2 = [1, 2, 3, 4, 5]
result = is_subset(list1, list2)
print(result)

# Write a program to check if all elements of one list are present in another list without using sets.
def is_subset(list1, list2):
    for item in list1:
        if item not in list2:
            return False
    return True

list1 = [1, 2, 3]
list2 = [1, 2, 4, 5]
print(is_subset(list1, list2))

#Which Method to Use?
#Use sets when you want faster performance, especially for large lists.
#Use loops if you want to avoid using advanced data structures.


