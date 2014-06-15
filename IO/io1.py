import io
import string
import random


# Generates Random String
def string_generator(size=6, chars=string.ascii_uppercase + string.digits):

    return ''.join(random.choice(chars) for _ in range(size))


s = string_generator(size=512,chars=string.ascii_uppercase + string.digits + string.ascii_lowercase)

# io module doesn't accept string but unicode
s = unicode(s)

print s

sdb = io.open("/dev/sdb","w")

sdb.write(s)

sdb.close()

sdb = io.open("/dev/sdb","r")

s1 = sdb.read(512)

# Comparing which was written and read
if s == s1:
    print "There is no mismatch"

sdb.close()



