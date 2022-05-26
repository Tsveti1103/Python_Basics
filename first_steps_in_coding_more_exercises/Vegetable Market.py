price_per_kilogram_of_vegetables = float(input())
price_per_kilogram_of_fruits = float(input())
total_kilograms_of_vegetables = int(input())
total_kilograms_of_fruits = int(input())
income= ((price_per_kilogram_of_vegetables*total_kilograms_of_vegetables)+(price_per_kilogram_of_fruits*total_kilograms_of_fruits))/1.94
format_income ="{:.2f}".format(income)
print(format_income)