import sys

n = int(input())
OddSum = 0
OddMin = sys.maxsize
OddMax = - sys.maxsize
EvenSum = 0
EvenMin = sys.maxsize
EvenMax = - sys.maxsize
for i in range(1, n + 1):
    num = float(input())
    if i % 2 != 0:
        OddSum += num
        if OddMin > num:
            OddMin = num
        if OddMax < num:
            OddMax = num
    else:
        EvenSum += num
        if EvenMin > num:
            EvenMin = num
        if EvenMax < num:
            EvenMax = num
print(f"OddSum={OddSum:.2f},")
if OddMin == sys.maxsize:
    print("OddMin=No,")
else:
    print(f"OddMin={OddMin:.2f},")
if OddMax == - sys.maxsize:
    print("OddMax=No,")
else:
    print(f"OddMax={OddMax:.2f},")
print(f"EvenSum={EvenSum:.2f},")
if EvenMin == sys.maxsize:
    print("EvenMin=No,")
else:
    print(f"EvenMin={EvenMin:.2f},")
if EvenMax == - sys.maxsize:
    print("EvenMax=No")
else:
    print(f"EvenMax={EvenMax:.2f}")
