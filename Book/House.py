n = int(input())
bottom = n // 2
bottom_print = []
for i in range(bottom):
    a = f'|{"*" * (n - 2)}|'
    bottom_print.append(a)
top = n - bottom
step = 0
top_print = []
for j in range(top):
    step += 2
    if j == 0:
        a = '*' * n
        top_print.append(a)
        step = 0
    else:
        a = f'{"-" * (j)}{"*" * (n - step)}{"-" * (j)}'
        top_print.append(a)
top_print = reversed(top_print)
print(*top_print, sep='\n')
print(*bottom_print, sep='\n')
