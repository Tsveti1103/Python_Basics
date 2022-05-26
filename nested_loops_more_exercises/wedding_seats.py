last_sector = input()
row_count_sector_a = int(input())
odd_row_seats = int(input())
start_sector = 65
start_seats = 97
counter = 0
for sector in range(start_sector, ord(last_sector) + 1):
    for row in range(1, row_count_sector_a + 1):
        if row % 2 != 0:
            for seats in range(start_seats, start_seats + odd_row_seats):
                print(f"{chr(sector)}{row}{chr(seats)}")
                counter += 1
        elif row % 2 == 0:
            for seats in range(start_seats, start_seats + odd_row_seats + 2):
                print(f"{chr(sector)}{row}{chr(seats)}")
                counter += 1
    row_count_sector_a += 1
print(counter)
