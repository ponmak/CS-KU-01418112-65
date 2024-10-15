# 04 จำนวนวันอาทิตย์
import math

def check_valid_date(day, month):
    day_in_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    if day < 1 or day > day_in_month[month]:
        return False
    return True

def check_valid_month(month):
    if month < 1 or month > 12:
        return False
    return True

def count_sunday_in_range(start, end, first_sunday):
    DAYINMONTH = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    if start == end and (start[0] - first_sunday) % 7 == 0:

        return 1

    count = 0 + end[0] - start[0] + 1
    if start[1] != end[1]:
        count += DAYINMONTH[start[1] - 1] - start[0] + 1
        count += end[0]
        for i in range(start[1], end[1] - 1):
            count += DAYINMONTH[i]
    else:
        count = abs(end[0] - start[0]) + 1

    first_sunday_date = first_sunday
    sundays = 0

    while first_sunday_date < start[0]:
        first_sunday_date += 7

    while first_sunday_date <= end[0]:
        sundays += 1
        first_sunday_date += 7

    return sundays

# รับข้อมูล
start = input().split('-')
start = [int(i) for i in start]
end = input().split('-')
end = [int(i) for i in end]
first_sunday = int(input())

if check_valid_month(start[1]) and check_valid_month(end[1]):
    if check_valid_date(start[0], start[1]) and check_valid_date(end[0], end[1]):
        result = count_sunday_in_range(start, end, first_sunday)
        print(result)
    else:
        print("Wrong Day")
else:
    print("Wrong Month")
    if not (check_valid_date(start[0], start[1]) and check_valid_date(end[0], end[1])):
        print("Wrong Day")
