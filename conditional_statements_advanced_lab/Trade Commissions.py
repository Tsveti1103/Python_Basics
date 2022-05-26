city = input()
sales = float(input())
percent = 0.0
if city == "Sofia":
    if 0 <= sales <= 500:
        percent = 5
    elif 500 < sales <= 1000:
        percent = 7
    elif 1000 < sales <= 10000:
        percent = 8
    elif sales > 10000:
        percent = 12
elif city == "Varna":
    if 0 <= sales <= 500:
        percent = 4.5
    elif 500 < sales <= 1000:
        percent = 7.5
    elif 1000 < sales <= 10000:
        percent = 10
    elif sales > 10000:
        percent = 13
elif city == "Plovdiv":
    if 0 <= sales <= 500:
        percent = 5.5
    elif 500 < sales <= 1000:
        percent = 8
    elif 1000 < sales <= 10000:
        percent = 12
    elif sales > 10000:
        percent = 14.5
if percent == 0:
    print("error")
else:
    final_result = percent / 100 * sales
    print(f"{final_result:.2f}")
