exam_hour = int(input())
exam_minutes = int(input())
arrival_hour = int(input())
arrival_minutes = int(input())
exam_time = exam_hour * 60 + exam_minutes
arrival_time = arrival_hour * 60 + arrival_minutes
if arrival_time > exam_time:
    print("Late")
    dif = arrival_time - exam_time
    if dif < 60:
        print(f"{dif} minutes after the start")
    else:
        hour = dif // 60
        minutes = dif % 60
        print(f"{hour}:{minutes:02} hours after the start")
else:
    dif = exam_time - arrival_time
    if dif <= 30:
        print("On time")
        print(f"{dif} minutes before the start")
    elif 30 < dif < 60:
        print("Early")
        print(f"{dif} minutes before the start")
    elif dif >= 60:
        print("Early")
        hour = dif // 60
        minutes = dif % 60
        print(f"{hour}:{minutes:02} hours before the start")
