def list_manipulator(numbers, first_command, second_command, *args):
    if first_command == 'add':
        args = list(args)
        if second_command == 'end':
            for a in args:
                numbers.append(a)
        else:
            args = reversed(args)
            for a in args:
                numbers.insert(0, a)

    if first_command == 'remove':
        if second_command == 'beginning':
            if not args:
                numbers.pop(0)
            else:
                count = int(args[0])
                for a in range(count):
                    numbers.pop(0)
        else:
            if not args:
                numbers.pop(-1)
            else:
                count = int(args[0])
                for a in range(count):
                    numbers.pop()

    return numbers


print(list_manipulator([1,2,3], "remove", "end"))
print(list_manipulator([1,2,3], "remove", "beginning"))
print(list_manipulator([1,2,3], "add", "beginning", 20))
print(list_manipulator([1,2,3], "add", "end", 30))
print(list_manipulator([1,2,3], "remove", "end", 2))
print(list_manipulator([1,2,3], "remove", "beginning", 2))
print(list_manipulator([1,2,3,4], "remove", "end", 2))
print(list_manipulator([1,2,3,4], "remove", "beginning", 2))
print(list_manipulator([1,2,3], "add", "beginning", 20, 30, 40))
print(list_manipulator([1,2,3], "add", "end", 30, 40, 50))