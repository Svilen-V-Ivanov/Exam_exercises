from collections import deque


def crafting(combination):
    if 100 <= combination <= 199:
        crafted_dict['Gemstone'] += 1
    elif 200 <= combination <= 299:
        crafted_dict['Porcelain Sculpture'] += 1
    elif 300 <= combination <= 399:
        crafted_dict['Gold'] += 1
    elif 400 <= combination <= 499:
        crafted_dict['Diamond Jewellery'] += 1


materials = [int(x) for x in input().split(' ')]
magic_levels = deque(int(x) for x in input().split(' '))

crafted_dict = {
    'Gemstone': 0,
    'Porcelain Sculpture': 0,
    'Gold': 0,
    'Diamond Jewellery': 0
}

while materials and magic_levels:
    current_material = materials.pop()
    current_magic = magic_levels.popleft()
    combination = current_magic + current_material

    if combination < 100:
        if combination % 2 == 0:
            combination = current_material * 2 + current_magic * 3
        else:
            combination = current_material * 2 + current_magic * 2

    if combination > 499:
        combination = combination // 2

    crafting(combination)

if (crafted_dict['Gemstone'] > 0 and crafted_dict['Porcelain Sculpture'] > 0) \
        or (crafted_dict['Gold'] > 0 and crafted_dict['Diamond Jewellery'] > 0):
    print("The wedding presents are made!")
else:
    print("Aladdin does not have enough wedding presents.")

if materials:
    print(f"Materials left: {', '.join(str(x) for x in materials)}")

if magic_levels:
    print(f"Magic left: {', '.join(str(x) for x in magic_levels)}")

for key, value in sorted(crafted_dict.items()):
    if value != 0:
        print(f"{key}: {value}")
