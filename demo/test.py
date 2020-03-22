import random

l1_cost = 0.75 + 8 * 0.05


def l1_to_3():
    l3_cost = l1_cost * 12 + 0.39 + 10
    return l3_cost


def l3_to_4():
    sum_cost = 0
    while (random.random() > 0.4878):
        sum_cost += l1_cost * 16 + 0.897
    else:
        sum_cost += l1_to_3() + l1_cost * 16 + 0.897 + 10
    return sum_cost


def l4_to_6():
    sum_cost = 0
    for i in range(0, 12):
        sum_cost += l3_to_4()
    return sum_cost + 19.75 + 10


avg_price = 0
for i in range(0, 10000):
    avg_price += l4_to_6()
print(avg_price / 10000)
