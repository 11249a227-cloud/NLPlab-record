# Binary numbers divisible by 2

def divisible_by_2(binary):

    if binary.endswith("0"):
        print("Accepted (Divisible by 2)")
    else:
        print("Rejected")

binary = input("Enter Binary Number: ")

divisible_by_2(binary)