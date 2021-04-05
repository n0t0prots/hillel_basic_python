x_position_of_knight = int(input('Enter first coordinate of knight: '))
y_position_of_knight = int(input('Enter second coordinate of knight: '))
x_possible_position = int(input('Enter first coordinate of possible position: '))
y_possible_position = int(input('Enter second coordinate of possible position: '))
x_position = abs(x_position_of_knight-x_possible_position)
y_position = abs(y_position_of_knight-y_possible_position)
if x_position == 1 and y_position == 2 or x_position == 2 and y_position == 1:
    print('Yes, this action is possible')
else:
    print('Wrong move')
