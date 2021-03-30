from pytimeNSW import pytimeNSW
from datetime import datetime, timedelta, date
import pandas as pd
import random
import hashlib

seed = int(hashlib.sha1(str("BDS Reading").encode("utf-8")).hexdigest(), 16) % (10 ** 4)
random.seed(seed)

date_object = date(2021, 3, 29)
date_object += timedelta(days=1-date_object.isoweekday())
slots = []
while date_object.year == 2021:
    if not pytimeNSW.is_public(date_object):
        slots.append(date_object)
    date_object += timedelta(days=7)
    

names = ["Quyu Kong", "Marian-Andrei Rizoiu", "Dima Galat","Thomas Willinghanm", "Rohit Ram", 
         "Pio Calderon", "Andrew Law",   "Duy Khuu", "Frankie Yuan"]

sched = pd.DataFrame(columns=["date", "presenter"])
sched["date"] = slots
q = names.copy()
for i in sched.index:
    if q == []:
        #q = sorted(names)
        q = names.copy()
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
