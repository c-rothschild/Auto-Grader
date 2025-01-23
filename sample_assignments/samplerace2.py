#!/usr/bin/env python3

# I *could* do what I need to do here with something like var**(1/2), 
# but I think this way is more readable
import math

NUMBER_OF_ROUNDING_DIGITS = 2

def calculate_distance_component(num1: float, num2: float):
    return (num2 - num1)**2

def calculate_distance(x1: float, y1: float, x2: float, y2: float):
    return math.sqrt(calculate_distance_component(x1, x2) + calculate_distance_component(y1, y2))

# Creating a separate function to return the rounded result is a design choice.
# a) It allows me to keep the unrounded function in case it's needed later in
# the life of the program, and b) the number of digits to round to is stored in
# one place
def calculate_rounded_distance(x1: float, y1: float, x2: float, y2: float):
    return round(calculate_distance(x1, y1, x2, y2), NUMBER_OF_ROUNDING_DIGITS)

def get_input_as_tuple(prompt: str):
    # The map() component of this expression is yoinked from Stack Overflow
    # https://stackoverflow.com/questions/1614236/how-do-i-convert-all-of-the-items-in-a-list-to-floats
    return tuple(map(float, input(prompt).split(",")))

print("Please enter the requested locations. Format them as x,y - no spaces or parentheses please!")

snack_coordinates = get_input_as_tuple("Snack coordinates: ")
user_coordinates = get_input_as_tuple("Your coordinates: ")
friend_coordinates = get_input_as_tuple("Your friend's coordinates: ")

print(f"You are at {user_coordinates}, your friend is at {friend_coordinates}, and you are racing to the snacks at {snack_coordinates}!")
# Grabbed the *tuple unpacking syntax from Stack Overflow - https://stackoverflow.com/a/1993732
user_distance = calculate_distance(*user_coordinates, *snack_coordinates)
friend_distance = calculate_distance(*friend_coordinates, *snack_coordinates)
print(f"Your current distance to the food is {round(user_distance, NUMBER_OF_ROUNDING_DIGITS)}.")
print(f"Your friend's distance to the food is {round(friend_distance, NUMBER_OF_ROUNDING_DIGITS)}.")
print(f"You are {round(user_distance / friend_distance, NUMBER_OF_ROUNDING_DIGITS)}x as close as your friend. Run!")
