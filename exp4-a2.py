# Activity 2: Test DFA

def dfa(string):
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

test_strings = ["a", "ab", "abb", "abbb"]

for s in test_strings:
    if dfa(s):
        print(s, "-> Accepted")
    else:
        print(s, "-> Rejected")