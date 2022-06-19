def is_inside(next_row, next_column, rows):
    return 0 <= next_row < rows and 0 <= next_column < rows


def movement(snake_row, snake_column, action):
    movements = {
        'up': [-1, 0],
        'down': [1, 0],
        'left': [0, -1],
        'right': [0, 1]
    }
    snake_row += movements[action][0]
    snake_column += movements[action][1]

    return snake_row, snake_column


rows = int(input())

matrix = []
snake_row, snake_column = 0, 0
burrows = []

for row in range(rows):
    row_elements = list(input())
    for column in range(rows):
        if row_elements[column] == 'S':
            snake_row, snake_column = row, column
        elif row_elements[column] == 'B':
            burrows.append(f"{row} {column}")
    matrix.append(row_elements)

food = 0
while True:
    action = input()
    next_row, next_column = movement(snake_row, snake_column, action)
    matrix[snake_row][snake_column] = '.'

    if not is_inside(next_row, next_column, rows):
        print("Game over!")
        break

    if matrix[next_row][next_column] == '*':
        food += 1
    elif matrix[next_row][next_column] == 'B':
        matrix[next_row][next_column] = '.'
        entrance = f"{next_row} {next_column}"
        burrows.remove(entrance)
        exit_burrow = burrows.pop()
        exit_row, exit_column = (int(x) for x in exit_burrow.split(' '))
        next_row, next_column = exit_row, exit_column

    snake_row, snake_column = next_row, next_column
    matrix[snake_row][snake_column] = 'S'

    if food == 10:
        break

if food == 10:
    print("You won! You fed the snake.")
print(f"Food eaten: {food}")

for row in matrix:
    print(''.join(row))
