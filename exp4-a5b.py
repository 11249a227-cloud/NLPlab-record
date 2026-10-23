import re

identifier = input("Enter Identifier: ")

pattern = r'^[A-Za-z_][A-Za-z0-9_]*$'

if re.match(pattern, identifier):
    print("Valid Identifier")
else:
    print("Invalid Identifier")