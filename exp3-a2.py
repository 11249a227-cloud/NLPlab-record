import re

pattern = r'^[A-Za-z0-9._%+-]+@gmail\.com$'

emails = [
    "student@gmail.com",
    "abc123@gmail.com",
    "hello@yahoo.com"
]

for email in emails:
    if re.match(pattern, email):
        print(email, "-> Valid Gmail")
    else:
        print(email, "-> Invalid Gmail")