def is_inside(row, column, rows):
    return 0 <= row < rows and 0 <= column < rows


def score_calculator(row, column):
    if is_inside(row, column, rows):
        if matrix[row][column] == 'B':
            return 501
        elif matrix[row][column].isdigit():
            return int(matrix[row][column])
        elif matrix[row][column] == 'D':
            sum = int(matrix[row][0]) + int(matrix[row][6]) + int(matrix[0][column]) + int(matrix[6][column])
            return sum * 2
        elif matrix[row][column] == 'T':
            sum = int(matrix[row][0]) + int(matrix[row][6]) + int(matrix[0][column]) + int(matrix[6][column])
            return sum * 3
    else:
        return 0


rows = 7
players = list(input().split(', '))
matrix = []
for row in range(rows):
    row_elements = input().split()
    matrix.append(row_elements)

throws_dict = dict.fromkeys(players, 0)
score_dict = dict.fromkeys(players, 501)

is_won = False
while True:
    current_player = players[0]
    input_shot = input()
    proper_shot = input_shot[1:-1]
    dart_row, dart_column = (int(x) for x in proper_shot.split(', '))

    shot_score = score_calculator(dart_row, dart_column)
    score_dict[current_player] -= shot_score
    throws_dict[current_player] += 1

    if score_dict[current_player] <= 0:
        is_won = True
        break
    else:
        players[0], players[1] = players[1], players[0]

print(f"{current_player} won the game with {throws_dict[current_player]} throws!")
