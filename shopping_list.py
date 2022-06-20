def shopping_list(money, **kwargs):
    if money < 100:
        return "You do not have enough budget."

    bought_items = 0
    purchases = ''
    for key, value in kwargs.items():
        (price, quantity) = value
        if price * quantity < money:
            money -= price * quantity
            bought_items += 1
            purchases += f"You bought {key} for {price * quantity:.2f} leva.\n"

        if bought_items == 5:
            break

    return purchases.strip()


print(shopping_list(100,
                    microwave=(70, 2),
                    skirts=(15, 4),
                    coffee=(1.50, 10),
                    ))
print('---------------------------------------------')
print(shopping_list(20,
                    jeans=(19.99, 1),
                    ))
print('---------------------------------------------')
print(shopping_list(104,
                    cola=(1.20, 2),
                    candies=(0.25, 15),
                    bread=(1.80, 1),
                    pie=(10.50, 5),
                    tomatoes=(4.20, 1),
                    milk=(2.50, 2),
                    juice=(2, 3),
                    eggs=(3, 1),
                    ))