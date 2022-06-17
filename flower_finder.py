from collections import deque

vowels = deque(input().split(' '))
consonants = list(input().split(' '))
flowers = ['rose', 'tulip', 'lotus', 'daffodil']
checked_flowers = []

for plant in flowers:
    checked_flowers.append(plant)

is_found = False
while vowels and consonants:
    vowel = vowels.popleft()
    consonant = consonants.pop()

    for index, flower in enumerate(checked_flowers):
        if vowel in flower:
            flower = flower.replace(vowel, '-')
            checked_flowers[index] = flower
        if consonant in flower:
            flower = flower.replace(consonant, '-')
            checked_flowers[index] = flower

    for index, flower in enumerate(checked_flowers):
        count = 0
        for letter in flower:
            if letter == '-':
                count += 1

        if count == len(flower):
            is_found = True
            print(f"Word found: {flowers[index]}")
            break

    if is_found:
        break

if not is_found:
    print("Cannot find any word!")

if vowels:
    print(f"Vowels left: {' '.join(vowels)}")

if consonants:
    print(f"Consonants left: {' '.join(consonants)}")
