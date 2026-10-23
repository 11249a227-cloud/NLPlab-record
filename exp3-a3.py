import re
pattern = r'[a-z]'
text = "Hello World"
result = re.findall(pattern, text)
print(result)