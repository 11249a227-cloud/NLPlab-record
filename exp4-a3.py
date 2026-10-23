# Activity 3: Incorrect Transition Table

transition = {
    "q0": {"a": "q2"},   # Wrong transition
    "q1": {"b": "q1"}
}

print("Incorrect Transition Table")
print(transition)

print("\nCorrect Transition Table")

correct = {
    "q0": {"a": "q1"},
    "q1": {"b": "q1"}
}

print(correct)