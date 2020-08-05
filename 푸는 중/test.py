import sys

fixed_cost, variable_cost, product_price = map(int, sys.stdin.readline().split())
start_count = (fixed_cost // product_price)
total_cost = fixed_cost + (variable_cost * start_count)
total_income = product_price * start_count
while 1:
    start_count += 1
    print(f"start_count = {start_count}")
    total_cost += variable_cost
    print(f"total_cost = {total_cost}")
    total_income += product_price
    print(f"total_income = {total_income}")
    if total_cost < total_income:
        break
    print()
print(start_count)