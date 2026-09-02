"""
date1, date2
room1, room2, room3
cap1, cap2, cap3
avail11, avail12, avail13
avail21, avail22, avail23
"""
date1='09/02/2026'
date2='09/03/2026'
room1 = 101
room2 = 102
room3 = 103
cap1 = 20
cap2 = 50
cap3 =  100
avail11 = avail12 = avail13 = avail21 = avail22 = avail23 = True
response = ""
preferred_date = input("Enter your preferred date: ")
expected_attendance = int(input("Enter expected attendance: "))
if preferred_date == date1:
    # find room
    if expected_attendance > 100:
        response = "We do not have a large enough room"
    elif expected_attendance >50:
        response = room3
    elif expected_attendance > 20:
        response = room2
    else:
        response = room1
elif preferred_date == date2:
    # find room
    if expected_attendance > 100:
        response = "We do not have a large enough room"
    elif expected_attendance >50:
        response = room3
    elif expected_attendance > 20:
        response = room2
    else:
        response = room1
else:
   response = "No availability"
print(response)



