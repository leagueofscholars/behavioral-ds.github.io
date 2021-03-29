from pytimeNSW import pytimeNSW
from datetime import datetime, timedelta
import pandas as pd
import random

 
date_object = date(2021, 3, 29)
date_object += timedelta(days=1-date_object.isoweekday())
slots = []
while date_object.year == 2021:
    if not pytimeNSW.is_public(date_object):
        slots.append(date_object)
    date_object += timedelta(days=7)
    

names = ["Quyu Kong", "Marian-Andrei Rizoiu", "Alexander Soen", "Rohit Ram", 
         "Pio Calderon", "Andrew Law", "Duy Khuu", "Frankie Yuan", "Dima Galat"]

sched = pd.DataFrame(columns=["date", "presenter"])
sched["date"] = slots
q = sorted(names)
for i in sched.index:
    if q == []:
        q = sorted(names)
    name = q.pop(random.randrange(len(q)))
    
    sched.loc[i, "presenter"] = name
    
    if i != 0:
        while sched.loc[i - 1, "presenter"] == name:
            q.append(name)
            name = q.pop(random.randrange(len(q)))
            sched.loc[i, "presenter"] = name

for i in sched.index:
    m = str(sched.loc[i,"date"].month)
    if len(m) == 1:
        m = "0" + m
    print("|" + str(sched.loc[i,"date"].day) + "/" + m + "|" + sched.loc[i,"presenter"] + "||||")
