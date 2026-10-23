import re

text = """
Contact us at student@gmail.com or admin@yahoo.com.
Call: 9876543210, 9123456789
Website: https://www.google.com
Visit: http://example.org
"""

# Email IDs
emails = re.findall(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b', text)

# Mobile Numbers (10 digits starting with 6-9)
phones = re.findall(r'\b[6-9]\d{9}\b', text)

# URLs
urls = re.findall(r'https?://[^\s]+', text)

print("Email IDs:")
print(emails)

print("\nMobile Numbers:")
print(phones)

print("\nURLs:")
print(urls)