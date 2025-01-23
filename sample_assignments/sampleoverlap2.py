#!/usr/bin/env python3

# hmmm I could make this function more versatile by including a delimiter param
def get_input_as_set(prompt: str):
    return set(input(prompt).split(","))

print("Please enter the two requested lists of classes separated with commas and no extra spaces!")
set1 = get_input_as_set("Enter the first list of classes: ")
set2 = get_input_as_set("Enter the second list of classes: ")

common_items = set1.intersection(set2)

print(f"The two lists have {len(common_items)} entries in common.")
print(f"They are: {', '.join(common_items)}")
