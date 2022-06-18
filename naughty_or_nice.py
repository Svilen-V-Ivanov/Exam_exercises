def naughty_or_nice_list(children, *args, **kwargs):
    nice_children = []
    naughty_children = []

    for kid in args:
        value, status = kid.split('-')
        value = int(value)
        kid_name = None

        is_unique = False
        for number, identity in children:
            if value == number and is_unique:
                is_unique = False
                break
            elif value == number:
                kid_name = identity
                is_unique = True

        if is_unique:
            children.remove((value, kid_name))

            if status == 'Nice':
                nice_children.append(kid_name)
            else:
                naughty_children.append(kid_name)

    for name, status in kwargs.items():
        num = None
        is_unique = False

        for number, identity in children:
            if name == identity and is_unique:
                is_unique = False
                break
            elif name == identity:
                num = number
                is_unique = True

        if is_unique:
            children.remove((num, name))
            if status == 'Nice':
                nice_children.append(name)
            else:
                naughty_children.append(name)

    not_found = [name for _, name in children]

    result = ''
    if nice_children:
        result += f"Nice: {', '.join(nice_children)}\n"
    if naughty_children:
        result += f"Naughty: {', '.join(naughty_children)}\n"
    if not_found:
        result += f"Not found: {', '.join(not_found)}\n"

    return result.strip()


print(naughty_or_nice_list(
    [
        (3, "Amy"),
        (1, "Tom"),
        (7, "George"),
        (3, "Katy"),
    ],
    "3-Nice",
    "1-Naughty",
    Amy="Nice",
    Katy="Naughty",
))
