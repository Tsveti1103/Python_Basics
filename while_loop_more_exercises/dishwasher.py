bottles = int(input())
preparation = 750 * bottles
counter = 0
vessels = ""
dishes_count = 0
pots_count = 0
vessels_count = 0
while vessels != "End":
    vessels = input()
    if vessels == "End":
        print("Detergent was enough!")
        print(f"{dishes_count} dishes and {pots_count} pots were washed.")
        print(f"Leftover detergent {preparation} ml.")
        break
    vessels_count = int(vessels)
    counter += 1
    if counter % 3 != 0:
        preparation -= vessels_count * 5
        dishes_count += vessels_count
    else:
        preparation -= vessels_count * 15
        pots_count += vessels_count
    if preparation < 0:
        print(f"Not enough detergent, {abs(preparation)} ml. more necessary!")
        break
