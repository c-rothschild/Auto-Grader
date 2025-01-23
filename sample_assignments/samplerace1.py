import math
# prompt user
print('Enter the location of')
print('            (a) the snacks')
print('            (b) yourself')
print('            (c) your friend')
print('The format should be: x,y (no parenthesis, no spaces please!)')

# take users input and save coordinates as strings
snack_coordinate = (input('first coordinate: '))
yourself_coordinate = (input('second coordinate: '))
friend_coordinate = (input('third coordinate: '))

# split the users input into x and y coordinates and make floats
split_snack = snack_coordinate.split(',')
snack_coordinate_x = float((split_snack[0]))
snack_coordinate_y = float((split_snack[1]))

# split the users input into x and y coordinates and make floats
split_yourself = yourself_coordinate.split(',')
yourself_coordinate_x = float((split_yourself[0]))
yourself_coordinate_y = float((split_yourself[1]))

# split the users input into x and y coordinates and make floats
split_friend = friend_coordinate.split(',')
friend_coordinate_x = float((split_friend[0]))
friend_coordinate_y = float((split_friend[1]))

# tell user information they just gave neatly
print(f'You are at {yourself_coordinate_x, yourself_coordinate_y} , your friend is at {friend_coordinate_x, friend_coordinate_y},and you are racing to the food at {snack_coordinate_x, snack_coordinate_y}')

# calculate your current distace to snack
your_current_distance = math.sqrt((float(yourself_coordinate_x - snack_coordinate_x))**2 + (yourself_coordinate_y - snack_coordinate_y)**2)
print(f'Your current distance to the food is {your_current_distance}')

# calculate friend current distace to snack
friend_current_distance = math.sqrt((float(friend_coordinate_x - snack_coordinate_x))**2 + (friend_coordinate_y - snack_coordinate_y)**2)
print(f'Your current distance to the food is {friend_current_distance}')

ratio_of_distance = your_current_distance / friend_current_distance
print(f'You are {ratio_of_distance}x as close as your friend. Run!')