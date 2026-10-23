import re

patterns = {
    "Aadhaar": r'^\d{4}\s\d{4}\s\d{4}$',
    "PAN": r'^[A-Z]{5}[0-9]{4}[A-Z]$',
    "Vehicle": r'^[A-Z]{2}[0-9]{2}[A-Z]{1,2}[0-9]{4}$',
    "Date": r'^\d{2}/\d{2}/\d{4}$',
    "Time": r'^([01]?[0-9]|2[0-3]):[0-5][0-9]$'
}

tests = {
    "Aadhaar": "1234 5678 9012",
    "PAN": "ABCDE1234F",
    "Vehicle": "TN38AB1234",
    "Date": "25/12/2025",
    "Time": "14:30"
}

for key in patterns:
    if re.match(patterns[key], tests[key]):
        print(key, "-> Valid")
    else:
        print(key, "-> Invalid")