import string as str
from random import *
import sys

passLength = int(sys.argv[1])

if passLength < 8:
    passLength = 8

myCharacters = str.ascii_letters + str.digits + str.punctuation
myPassword = "".join(choice(myCharacters) for i in range(passLength))

print("Your Password is : ", myPassword)
