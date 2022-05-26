money = float(input())
year = int(input())
for year_now in range(1800, year + 1):
    if year_now % 2 == 0:
        money -= 12000
    else:
        money = money - (12000 + 50 * (year_now - 1800 + 18))
if money >= 0:
    print(f"Yes! He will live a carefree life and will have {money:.2f} dollars left.")
else:
    print(f"He will need {abs(money):.2f} dollars to survive.")
