Hours = int(input("Enter the hours: "))
Mins = int(input("Enter the minutes: "))
Secs = int(input("Enter the seconds: "))

if (Hours >= 0 and Hours <= 23) and (Mins >= 0 and Mins <= 59) and (Secs >= 0 and Secs <= 59):
    print("Your time is valid.")
else:
    print("Your time is invalid.")