# Develop a module over datetime library for calculating difference between 2 given time and date.​

import datetime

def difference(time1, time2):

    date1 = datetime.datetime.strptime(time1, "%Y-%m-%d %H:%M:%S")
    date2 = datetime.datetime.strptime(time2, "%Y-%m-%d %H:%M:%S")
    
    if (date2>date1):   #added this if-statement so that the order of input of datetime args (old,new) or (new,old) doesn't matter
        diff = date2 - date1
    else: 
        diff = date1 - date2
        
    return diff

print(difference("2023-01-15 10:00:00","2023-01-16 10:41:23"))