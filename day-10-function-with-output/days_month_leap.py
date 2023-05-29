def is_leap(y_ear):
    if y_ear % 4 == 0:
        if y_ear % 100 == 0:
            if y_ear % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False


def days_in_month(years, months):
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if is_leap(years) and months == 2:
        return 29
    return month_days[month - 1]


year: int = int(input("Enter year: "))
month = int(input("Enter month: "))
days = days_in_month(years=year, months=month)
print(days)
