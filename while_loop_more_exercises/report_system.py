needed_amount = int(input())
amount = ""
counter = 0
total_amount = 0
cs = 0
cc = 0
cc_counter = 0
cs_counter = 0
while amount != "End":
    amount = input()
    if amount == "End":
        print("Failed to collect required money for charity.")
        break
    counter += 1
    if counter % 2 != 0:
        if int(amount) > 100:
            print("Error in transaction!")
        else:
            print("Product sold!")
            cs += int(amount)
            cs_counter += 1
    else:
        if int(amount) < 10:
            print("Error in transaction!")
        else:
            print("Product sold!")
            cc += int(amount)
            cc_counter += 1
    total_amount = cc + cs
    if total_amount >= needed_amount:
        print(f"Average CS: {cs / cs_counter:.2f}")
        print(f"Average CC: {cc / cc_counter:.2f}")
        break
