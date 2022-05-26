name = input()
adults_tickets_count = int(input())
kids_tickets_count = int(input())
ticket_price_adults = float(input())
tax = float(input())
final_price_adults_ticket = ticket_price_adults + tax
kids_tickets_price = 0.3 * ticket_price_adults
final_price_kids_ticket = kids_tickets_price + tax
total_tickets_price = final_price_kids_ticket * kids_tickets_count + final_price_adults_ticket * adults_tickets_count
profit = 0.2 * total_tickets_price
print(f"The profit of your agency from {name} tickets is {profit:.2f} lv.")
