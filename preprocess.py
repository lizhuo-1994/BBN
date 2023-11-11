import datetime
import os
import csv
unprintStrptimeFmt = "%Y-%m-%d-%H:%M:%S"

error_id_Q1 = []
error_id_Q2 = []
error_id_Q3 = []
error_id_Q4 = []
fieldnames = []
data_list = []
with open('data4.csv', newline='') as f: 
    cr = csv.DictReader(f)
    for row in cr:
        data_list.append(row)
        # print(row)
        fieldnames = row.keys()
        # print(row['date'], row['Q1'], row['Q2'], row['Q3'])
        date_obj = datetime.datetime.strptime(row['date'], unprintStrptimeFmt)
        weekday = date_obj.weekday()
        
        
        Q1 = weekday + 1
        if int(row['Q1']) != Q1:
            error_id_Q1.append(row['randomID'])


        hour = date_obj.hour
        Q3 = (hour // 3) + 1
        if int(row['Q3']) != Q3:
            error_id_Q2.append(row['randomID'])

        if int(row['Q21']) == 4:
            error_id_Q3.append(row['randomID'])

        if date_obj.month == 7 and date_obj.day==29 and int(row['gender'])==1 and int(row['age'])==39:
            error_id_Q4.append(row['randomID'])

    print('Q1:\t', len(error_id_Q1), error_id_Q1)
    print('Q3:\t', len(error_id_Q2), error_id_Q2)
    print('Q21:\t', len(error_id_Q3), error_id_Q3)
    print('sb:\t', len(error_id_Q4), error_id_Q4)

    error_ids = error_id_Q1 + error_id_Q2 + error_id_Q3 + error_id_Q4

    error_ids = list(set(error_ids))
    print(len(error_ids), error_ids)

    cr = csv.DictReader(f)
    with open("data_4_processed.csv", "w") as f:
        cw = csv.DictWriter(f, fieldnames = fieldnames)
        cw.writeheader() 
        
        for row in data_list:
            print(row)
            if row['randomID'] in error_ids:
                continue
            cw.writerow(row)









       
