k = int(input())  # - началото на интервала за първото число от първия номер – цяло число в интервала [0..8]
l = int(input())  # - началото на интервала за второто число от първия номер – цяло число в интервала [9..0]
m = int(input())  # - началото на интервала за първото число от втория номер – цяло число в интервала [0..8]
n = int(input())  # - началото на интервала за второто число от втория номер – цяло число в интервала [9..0]
transfer_counter = 0
flag = False
for K in range(k, 10):
    for L in range(9, l - 1, -1):
        for M in range(m, 10):
            for N in range(9, n - 1, -1):
                if K % 2 == 0 and L % 2 == 1 and M % 2 == 0 and N % 2 == 1:
                    if K == M and L == N:
                        print("Cannot change the same player.")
                    else:
                        print(f"{K}{L} - {M}{N}")
                        transfer_counter += 1
                    if transfer_counter == 6:
                        flag = True
                        break
            if flag:
                break
        if flag:
            break
    if flag:
        break
