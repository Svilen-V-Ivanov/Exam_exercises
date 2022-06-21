def flights(*args):
    travel_info = {}
    for value in range(0, len(args)):
        passengers = 0
        if value % 2 == 0:
            if args[value] != 'Finish':
                destination = args[value]
            else:
                break
        if value % 2 != 0:
            passengers = int(args[value])

        if destination not in travel_info.keys():
            travel_info[destination] = passengers
        else:
            travel_info[destination] += passengers

    return travel_info


print(flights('Vienna', 256, 'Vienna', 26, 'Morocco', 98, 'Paris', 115, 'Finish', 'Paris', 15))
print('----------------------------------------------')
print(flights('London', 0, 'New York', 9, 'Aberdeen', 215, 'Sydney', 2, 'New York', 300, 'Nice', 0, 'Finish'))
print('----------------------------------------------')
print(flights('Finish', 'New York', 90, 'Aberdeen', 300, 'Sydney', 0))