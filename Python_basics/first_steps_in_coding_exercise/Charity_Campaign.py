days = int(input())
bakers = int(input())
cakes = int(input())
waffles = int(input())
pancakes = int(input())
daily_tatal = bakers * (cakes*45+waffles*5.80+pancakes*3.20)
income = daily_tatal * days
net_income = income - income/8
print(net_income)