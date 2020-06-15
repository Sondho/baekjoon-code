import sys

fixed_cost, variable_cost, product_price = map(int, sys.stdin.readline().split())
break_even_point = -1
if (product_price*1 - fixed_cost + (variable_cost*1)) < (product_price*2 - fixed_cost + (variable_cost*2)):
    if fixed_cost/(1-variable_cost/product_price)/product_price > 0:
        break_even_point = int(fixed_cost/(1-(variable_cost/product_price)))

print(break_even_point)