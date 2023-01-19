works_days = int(input())
dollars = float(input())
dollar_exchange_rate = float(input())
monthly_salary = works_days * dollars
annual_salary = monthly_salary * 12 + monthly_salary * 2.5
taxes = annual_salary * 0.25
daily_salary = (annual_salary - taxes) / 365
total = daily_salary * dollar_exchange_rate
print(f"{total:.2f}")