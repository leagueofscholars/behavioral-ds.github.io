from pytimeNSW import pytimeNSW
from datetime import datetime, timedelta, date

# this script generates the reading group roster for an entire year starting at the start date and skipping public holidays
# its slightly hacky but it works -_('_')_-

# in order of roster
names = ["Rohit Ram",
         "Frankie Yuan",
         "Amelie Girard",
         "Pio Calderon",
         "Marian-Andrei Rizoiu",
         "Daniela Elia",
         "Elaine Gong",
         "Jooyoung Lee"
         ]

# start date
date_object = date(2023, 10, 23)
date_object += timedelta(days=1-date_object.isoweekday())
slots = []
holidays = set()

while date_object.year == 2023:
    slots.append(date_object)
    if pytimeNSW.is_public(date_object):
        holidays.add(date_object)
	
    date_object += timedelta(days=7)

i = 0
for slot in slots:
    if slot not in holidays:
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

    
