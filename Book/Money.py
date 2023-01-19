bitcoins = float(input())
chinese_yuan = float(input())
commission = float(input()) / 100
euro = bitcoins * 1168 / 1.95 + chinese_yuan * 0.15 * 1.76 / 1.95
total = euro - commission * euro
print(f"{total:.2f}")