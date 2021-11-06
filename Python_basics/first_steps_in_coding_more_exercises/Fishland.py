price_mackerel = float(input())  # скумрия
price_sprat = float(input())  # цаца
amount_bonito = float(input())  # паламуд
amount_horse_mackerel = float(input())  # сафрид
amount_mussels = int(input())  # миди
price_bonito = price_mackerel * 0.6 + price_mackerel
price_horse_mackerel = price_sprat * 0.8 + price_sprat
price_mussels = 7.5
total = price_bonito * amount_bonito + price_horse_mackerel * amount_horse_mackerel + price_mussels * amount_mussels
print(f'{total:.2f}')
