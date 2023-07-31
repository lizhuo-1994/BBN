import numpy as np
import copy
import csv
import json
from network import node_states

data_list = []
with open('data.csv','rt') as f: 
    cr = csv.DictReader(f)
    for row in cr:
        data_point = dict()
        for i in range(1, 37):
            data_point['Q' + str(i)] = int(row['Q' + str(i)])
        if int(row['diff_coin_resp']) < 0:
            ret = -1
        elif int(row['diff_coin_resp']) == 0:
            ret = 0
        else:
            ret = 1
        data_point['diff_coin_resp'] = ret
        data_list.append(data_point) 

data_value = dict()
for key in data_list[0].keys():
    data_value[key] = []
    for data_point in data_list:
        data_value[key].append(data_point[key])


# print(data_value['diff_coin_resp'], set(data_value['diff_coin_resp']))
# exit()

node_value = dict()
for node in node_states.keys():
    node_value[node] = np.array(data_value[node_states[node]['name']])
    
