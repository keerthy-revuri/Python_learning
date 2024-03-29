#Number of days per month, first value is 0 for indexing purpose
month_days = [0,31,28,31,30,31,30,31,31,30,31,30,31]

def is_leap(year):
    #returns true for leap years and false for non-leap years
    return year % 4 == 0 and (year % 100!= 0 or year % 400 == 0)

def days_in_month(year, month):
    #return number of days in that month in that year
    if not  1 <= month <= 12:
        return 'invalid_month'
    if month == 2 and is_leap(year):
        return 29

    return month_days[month]

res = days_in_month(2024, 2)
print(res)

