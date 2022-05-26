pages_count = int(input())
pages_per_hour = int(input())
days_count = int(input())
time = pages_count / pages_per_hour
result = time / days_count
print(result)