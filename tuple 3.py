from datetime import datetime

date1 = (17, 2, 2025)
date2 = (10, 3, 2025)

date_obj1 = datetime(date1[2], date1[1], date1[0])
date_obj2 = datetime(date2[2], date2[1], date2[0])

difference = abs((date_obj2 - date_obj1).days)

print(f"The number of days between {date1} and {date2} is {difference} days.")
