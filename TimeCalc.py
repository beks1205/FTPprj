from datetime import datetime,timedelta
from ftplib import print_line

date1 = input('Type a Date in Format (Day.Month.Year)\n')
datetime_object = datetime.strptime(date1, '%d.%m.%Y')
end_date = datetime_object + timedelta(days=30)
print(end_date)
