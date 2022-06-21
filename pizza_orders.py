from collections import deque

orders = deque(int(x) for x in input().split(', '))
workers = [int(x) for x in input().split(', ')]

pizza_count = 0
while orders and workers:
    current_order = orders.popleft()
    if current_order <= 0 or current_order > 10:
        continue

    current_worker = workers.pop()
    if current_worker >= current_order:
        pizza_count += current_order
    else:
        pizza_count += current_worker
        current_order -= current_worker
        orders.appendleft(current_order)

if not orders:
    print("All orders are successfully completed!")
    print(f"Total pizzas made: {pizza_count}")
    print(f"Employees: {', '.join(str(x) for x in workers)}")
else:
    print("Not all orders are completed.")
    print(f"Orders left: {', '.join(str(x) for x in orders)}")
