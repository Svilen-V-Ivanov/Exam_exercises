from collections import deque

bomb_effects = deque(int(x) for x in input().split(', '))
bomb_casings = [int(x) for x in input().split(', ')]

bomb_types = {
    'Datura Bombs': 40,
    'Cherry Bombs': 60,
    'Smoke Decoy Bombs': 120
}

crafted_bombs = {
    'Datura Bombs': 0,
    'Cherry Bombs': 0,
    'Smoke Decoy Bombs': 0
}
is_crafted = False
while bomb_effects and bomb_casings:
    effect = bomb_effects.popleft()
    casing = bomb_casings.pop()
    bomb = effect + casing

    is_in = False
    for name, power in bomb_types.items():
        if bomb == power:
            crafted_bombs[name] += 1
            is_in = True

    if not is_in:
        bomb_effects.appendleft(effect)
        bomb_casings.append(casing - 5)

    count = 0
    for key, value in crafted_bombs.items():
        if value >= 3:
            count += 1

    if count == len(crafted_bombs):
        is_crafted = True
        break

if is_crafted:
    print("Bene! You have successfully filled the bomb pouch!")
else:
    print("You don't have enough materials to fill the bomb pouch.")

if bomb_effects:
    print(f"Bomb Effects: {', '.join(str(x) for x in bomb_effects)}")
else:
    print("Bomb Effects: empty")

if bomb_casings:
    print(f"Bomb Casings: {', '.join(str(x) for x in bomb_casings)}")
else:
    print("Bomb Casings: empty")

for key, value in sorted(crafted_bombs.items(), key=lambda x: x[0]):
    print(f"{key}: {value}")
