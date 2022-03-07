from pytimeNSW import pytimeNSW
from datetime import datetime, timedelta, date

# this script generates the reading group roster for an entire year starting at the start date and skipping public holidays
# its slightly hacky but it works -_('_')_-

# in order of roster
names = ["Amelie Girard",
         "Rohit Ram",
         "Quyu Kong",
         "Callum Pastuszak",
         "Thomas Willingham",
         "Pio Calderon",
         "Marian-Andrei Rizoiu",
         "Daniela Elia",
         "Frankie Yuan"
         ]

# start date
date_object = date(2022, 5, 30)
date_object += timedelta(days=1-date_object.isoweekday())
slots = []
while date_object.year == 2022:
    if not pytimeNSW.is_public(date_object) and not pytimeNSW.is_public_can(date_object):
        slots.append(date_object)
    date_object += timedelta(days=7)

i = 0
for slot in slots:
    date_str = str("{:02d}".format(slot.day)) + "/" + str("{:02d}".format(slot.month)) + "/" + str(slot.year)[2:]
    pres_str = names[i]
    # copy pasta this into the csv
    print(date_str + "," + pres_str + ",,,,,")

    i += 1
    if i >= len(names):
        i = 0
    
