from pytimeNSW import pytimeNSW
from datetime import datetime, timedelta, date
import holidays

# this script generates the reading group roster for an entire year starting at the start date and skipping public holidays
# its slightly hacky but it works -_('_')_-

# in order of roster
names = ["Marian-Andrei Rizoiu",
         #"Rohit Ram",
         #"Amelie Girard",
         "Elaine Gong",
         "Pio Calderon",
         # "Daniela Elia",
         "Frankie Yuan",
         "Jooyoung Lee"
         ]

# start date
date_object = date(2024, 1, 22)
date_object += timedelta(days=1-date_object.isoweekday())
slots = []
holiday_dates = set()

while date_object.year == 2024:
    slots.append(date_object)
    print()
    if date_object in holidays.AU(subdiv="NSW"):
        holiday_dates.add(date_object)
	
    date_object += timedelta(days=14)

print(holiday_dates)

i = 0
for slot in slots:
    if slot not in holiday_dates :
        date_str = str("{:02d}".format(slot.day)) + "/" + str("{:02d}".format(slot.month)) + "/" + str(slot.year)[2:]
        pres_str = names[i]
        # copy pasta this into the csv
        print(date_str + "," + pres_str + ",,,,,")

        i += 1
        if i >= len(names):
            i = 0
    else:
        date_str = str("{:02d}".format(slot.day)) + "/" + str("{:02d}".format(slot.month)) + "/" + str(slot.year)[2:]
        # copy pasta this into the csv
        print(date_str + ",--," + "No reading due to public holiday,,,," )

    
