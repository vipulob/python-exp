import sys

# Get size of integer. The int is 12 bytes
print("Integer Size ---->"+ str(sys.getsizeof(123)))


# Get the size of char. The output shows that there is additional space is maintained by Python
print("Char Size ----> "+ str(sys.getsizeof("x")))

# Get the size of string. The output shows the single char is 1 byte long
print("String size---->"+str(sys.getsizeof("xy")))

# Get the size of float. Its 16 bytes
print("Float Size --->"+str(sys.getsizeof(1.23)))

# Get the size of empty list. Its 32 bytes
print("List Size --->"+str(sys.getsizeof([])))

# Get the size of empty tuple. Empty tuple cannot be created
t = ()
print("Tuple Size---> "+str(sys.getsizeof(t)))









