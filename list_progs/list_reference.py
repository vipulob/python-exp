#!/usr/bin/python3

# Description: This programs shows the = use to reference the object and not copy. list1 and list2 are same object

list1 = [1,2,3]

list2 = list1

list2.append(4)

# Prints [1,2,3,4]
print(list1)
