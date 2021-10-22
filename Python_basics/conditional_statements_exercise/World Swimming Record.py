record = float(input())
distance = float(input())
time_for_meter = float(input())
water_resistance = distance // 15
delay = water_resistance * 12.5
time = distance * time_for_meter + delay
if time < record:
    print(f" Yes, he succeeded! The new world record is {time:.2f} seconds.")
else:
    missing_seconds = time - record
    print(f"No, he failed! He was {missing_seconds:.2f} seconds slower.")