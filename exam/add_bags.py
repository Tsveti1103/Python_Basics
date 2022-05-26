baggage_price = float(input())
kilo_baggage = float(input())
days_before_trip = int(input())
baggage_count = int(input())
if kilo_baggage < 10:
    baggage_price *= 0.2
elif 10 <= kilo_baggage <= 20:
    baggage_price *= 0.5
if days_before_trip < 7:
    baggage_price *= 1.4
elif 7 <= days_before_trip <= 30:
    baggage_price *= 1.15
elif days_before_trip > 30:
    baggage_price *= 1.1

print(f"The total price of bags is: {baggage_price * baggage_count:.2f} lv. ")
