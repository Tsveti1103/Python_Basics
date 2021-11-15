month = int(input())
water = 0
internet = 0
other = 0
electricity_bill = 0.0
for i in range(0, month):
    electricity_bill_for_month = float(input())
    electricity_bill += electricity_bill_for_month
water = 20 * month
internet = 15 * month
other += (electricity_bill + water + internet) * 1.2
average_bills = (electricity_bill + water + internet + other) / month
print(f"Electricity: {electricity_bill:.2f} lv")
print(f"Water: {water:.2f} lv")
print(f"Internet: {internet:.2f} lv")
print(f"Other: {other:.2f} lv")
print(f"Average: {average_bills:.2f} lv")
