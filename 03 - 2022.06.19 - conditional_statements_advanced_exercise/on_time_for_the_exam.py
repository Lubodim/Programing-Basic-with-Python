exam_hour = int(input())
exam_minutes = int(input())
arriving_hour = int(input())
arriving_minutes = int(input())

time_of_exam = exam_hour * 60 + exam_minutes
time_of_arriving = arriving_hour * 60 + arriving_minutes

if time_of_arriving > time_of_exam:
    print("Late")
elif time_of_arriving < time_of_exam - 30:
    print("Early")
elif time_of_arriving >= time_of_exam - 30:
    print("On time")

difference = abs(time_of_exam - time_of_arriving)
hour = difference // 60
minutes = difference % 60

if time_of_arriving < time_of_exam:
    if hour < 1:
        print(f"{minutes} minutes before the start")
    else:
        print(f"{hour}:{minutes:02d} hours before the start")
elif time_of_arriving > time_of_exam:
    if hour < 1:
        print(f"{minutes} minutes after the start")
    else:
        print(f"{hour}:{minutes:02d} hours after the start")
