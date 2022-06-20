def is_inside(row, column, rows):
    return 0 <= row < rows and 0 <= column < rows


def prize(points):
    if 100 <= points <= 199:
        return 'Football'
    elif 200 <= points <= 299:
        return 'Teddy Bear'
    elif 300 <= points:
        return 'Lego Construction Set'


rows, columns = 6, 6

matrix = []

for row in range(rows):
    row_elements = input().split()
    matrix.append(row_elements)

won_points = 0
for throw in range(3):
    input_shot = input()
    proper_shot = input_shot[1:-1]
    shot_row, shot_column = (int(x) for x in proper_shot.split(', '))

    if not is_inside(shot_row, shot_column, rows):
        continue

    if matrix[shot_row][shot_column] == 'B':
        for value in range(rows):
            if matrix[value][shot_column] != 'B' and matrix[value][shot_column] != '.':
                won_points += int(matrix[value][shot_column])
        matrix[shot_row][shot_column] = '.'

if won_points < 100:
    print(f"Sorry! You need {100 - won_points} points more to win a prize.")
else:
    won_prize = prize(won_points)
    print(f"Good job! You scored {won_points} points, and you've won {won_prize}.")
