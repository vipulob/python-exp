# How to modify the text of file in python program?

# Contents of file.txt
# abc
# Now you need to change abc to def in the same file

import fileinput
import re

# Open the file using fileinput library and loop over line by line
for line in fileinput.input('file.txt',inplace=1):
 
    # Match the line which u need to change
    match = re.search(r"abc",line)
    
    if match:
        # If match then change the file using re.sub()
        p = re.compile(r"abc")

        line = p.sub('def',line)

    print line.strip()




# File contents after program execution
# def