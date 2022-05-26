exam_hour = int(input())
exam_minutes = int(input())
arrival_hour = int(input())
arrival_minutes = int(input())
exam_time = exam_hour * 60 + exam_minutes
arrival_time = arrival_hour * 60 + arrival_minutes
difference = arrival_time - exam_time
text = ""
if difference < -30:
    text = "Early"
elif -30 <= difference <= 0:
    text = "On time"
else:
    text = "Late"
print(f"{text}")
if difference != 0:
    hours = abs(difference) // 60
    minutes = abs(difference) % 60
    if 0 > difference > -60:
        print(f"{minutes} minutes before the start")
    elif difference <= -60:
        print(f"{hours}:{minutes:02d} hours before the start")
    elif 0 < difference < 60:
        print(f"{minutes} minutes after the start")
    elif difference >= 60:
        print(f"{hours}:{minutes:02d} hours after the start")
