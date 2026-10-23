# Activity 1: DFA for ab*

def dfa_ab_star(string):
    state = "q0"

    for ch in string:
        if state == "q0":
            if ch == 'a':
                state = "q1"
            else:
                return False

        elif state == "q1":
            if ch == 'b':
                state = "q1"
            else:
                return False

    return state == "q1"

text = input("Enter a string: ")

if dfa_ab_star(text):
    print("Accepted")
else:
    print("Rejected")