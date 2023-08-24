import datetime
import os
import csv
unprintStrptimeFmt = "%Y-%m-%d-%H:%M:%S"

error_id = []

with open('data4.csv','rt') as f: 
    cr = csv.DictReader(f)
    for row in cr:
        # print(row['date'], row['Q1'], row['Q2'], row['Q3'])
        date_obj = datetime.datetime.strptime(row['date'], unprintStrptimeFmt)
        weekday = date_obj.weekday()
        print(date_obj)
        
        Q1 = weekday + 1
        if int(row['Q1']) != Q1:
            error_id.append(row['randomID'])


        hour = date_obj.hour
        Q3 = (hour // 3) + 1
        if int(row['Q3']) != Q3:
            error_id.append(row['randomID'])

    print(len(error_id), error_id)
    error_id = list(set(error_id))
    print(len(error_id), error_id)

    with open("data_4_processed.csv", "w") as f:
        cw = csv.DictWriter(f)
        cw.writeheader() 
        
        for row in cr:
            if row['randomID'] in error_id:
                continue
            cw.writerow(row)









       
