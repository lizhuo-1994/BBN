import numpy as np
import copy
import csv
import json


data_list = []
with open('data.csv','rt') as f: 
    cr = csv.DictReader(f)
    for row in cr:
        data_point = dict()
        for i in range(1, 37):
            data_point['Q' + str(i)] = int(row['Q' + str(i)])
        data_point['diff_coin_resp'] = int(row['diff_coin_resp'])
        data_list.append(data_point) 

node_value = dict()
for key in data_list[0].keys():
    node_value[key] = []
    for data_point in data_list:
        node_value[key].append(data_point[key])

print(node_value)