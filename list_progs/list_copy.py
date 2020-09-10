#!/usr/bin/python3

# Use of shallow copy and deep copy

import copy

list1 = [1,2,3,4]

list2 = [list1]

# Shallow copy, copies the reference object.
list3 = copy.copy(list2)

# Deep copy, copies the value of objects
list4 = copy.deepcopy(list2)

list1.append(5)

# Prints [[1,2,3,4,5]]
print("list2={0}".format(list2))

# Prints [[1,2,3,4,5]]
print("list3={0}".format(list3))

# Prints [[1,2,3,4]]
print("list4={0}".format(list4))
