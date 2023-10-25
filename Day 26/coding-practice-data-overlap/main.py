# reading the file1.txt
with open("Day 26/coding-practice-data-overlap/file1.txt") as file1:
    list1 = file1.readlines()

# reading the file2.txt
with open("Day 26/coding-practice-data-overlap/file2.txt") as file2:
    list2 = file2.readlines()

# Converting the read list into integer with list comprehension
int_list_1 = [int(n.strip()) for n in list1]
int_list_2 = [int(n.strip()) for n in list2]

# fetching out the common number between two lists
# result = [n for n in int_list_1 if n in int_list_2]
result = [int(n) for n in list1 if n in list2]
print(result)
