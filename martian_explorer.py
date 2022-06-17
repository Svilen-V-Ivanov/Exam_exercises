def movement(move_row, move_column, action, rows):
    movements = {
        'up': [-1, 0],
        'down': [1, 0],
        'left': [0, -1],
        'right': [0, 1]
    }
    move_row += movements[action][0]
    move_column += movements[action][1]

    if move_row == rows:
        move_row = 0
    elif move_row < 0:
        move_row = rows - 1

    if move_column == rows:
        move_column = 0
    elif move_column < 0:
        move_column = rows - 1

    return move_row, move_column


rows, columns = 6, 6
matrix = []
rover_row, rover_column = 0, 0

for row in range(rows):
    row_elements = input().split()
    for column in range(columns):
        if row_elements[column] == 'E':
            rover_row, rover_column = row, column
    matrix.append(row_elements)

resources = {
    'W': 0,
    'M': 0,
    'C': 0
}
abbreviations = {
    'W': 'Water',
    'M': 'Metal',
    'C': 'Concrete'
}
commands = input().split(', ')
matrix[rover_row][rover_column] = '-'
is_broken = False
for order in commands:
    next_row, next_column = movement(rover_row, rover_column, order, rows)
    rover_row, rover_column = next_row, next_column

    if matrix[rover_row][rover_column] in resources.keys():
        resources[matrix[rover_row][rover_column]] += 1
        print(f"{abbreviations[matrix[rover_row][rover_column]]} deposit found at ({rover_row}, {rover_column})")
    elif matrix[rover_row][rover_column] == 'R':
        print(f"Rover got broken at ({rover_row}, {rover_column})")
        is_broken = True
        break

counter = 0
for key, item in resources.items():
    if item != 0:
        counter += 1

if counter != len(resources):
    print("Area not suitable to start the colony.")
else:
    print("Area suitable to start the colony.")
