# Slip 1 A) Write a Python program to accept n numbers in list and remove duplicates from a
#  list

l = [1,2,3,4,4,5,6,6,6,7,7,8,1,2,1]
duplicate = []
for n in l:
    if n not in duplicate:
        duplicate.append(n)
        print(duplicate)