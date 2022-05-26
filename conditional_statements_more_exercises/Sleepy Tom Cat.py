days_off = int(input())
work_days = 365 - days_off
play_time = days_off * 127 + work_days * 63
if play_time > 30000:
    print("Tom will run away")
    more_time = play_time - 30000
    H = more_time // 60
    M = more_time % 60
    print(f"{H} hours and {M} minutes more for play")
elif play_time < 30000:
    print("Tom sleeps well")
    free_time = 30000 - play_time
    H = free_time // 60
    M = free_time % 60
    print(f"{H} hours and {M} minutes less for play")