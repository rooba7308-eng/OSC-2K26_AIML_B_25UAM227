"""
Problem 56: Budget Filter
Error Type: TYPE_ERROR
Difficulty: Medium
"""

def update_budget(current_val, input_val):
     
    return current_val + int(input_val)

current_val = 100
input_val = "50"
print(update_budget(current_val, input_val))