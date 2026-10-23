import re
resume = """
Name : ram murathy
Email : rammurathy@gmail.com
Phone : 9876543210
Skills:
Python
Java
Machine Learning
SQL
"""
name = re.search(r'Name\s*:\s*(.*)', resume)
email = re.search(r'[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}', resume)
phone = re.search(r'[6-9]\d{9}', resume)
skills = re.findall(r'Python|Java|Machine Learning|SQL', resume)
print("Name:", name.group(1))
print("Email:", email.group())
print("Phone:", phone.group())
print("Skills:", skills)