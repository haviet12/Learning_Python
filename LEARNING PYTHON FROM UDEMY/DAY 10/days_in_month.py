def is_leap(year):
  if year % 4 == 0:
    return True
  else:
    return False

def days_in_month(year, month):
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]  
    if is_leap(year)==True:
        month_days[1] = month_days[1]+1
        day=month_days[month-1]
    elif is_leap(year)==False:
        day = month_days[month-1]
    return day

#🚨 Do NOT change any of the code below 
while True:
    year = int(input("Enter a year: "))
    month = int(input("Enter a month: "))
    print(days_in_month(year, month))








