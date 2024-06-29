import numpy as np
import copy
import csv
import json
from network import node_states
import scipy.stats as stats
import pandas as pd
import pingouin as pg


data_list = []
with open('data_4_processed.csv','rt') as f: 
    cr = csv.DictReader(f)
    for row in cr:
        data_point = dict()
        for i in range(1, 37):
            data_point['Q' + str(i)] = int(row['Q' + str(i)])
       
        if int(row['diff_coin_resp']) < 0:
            data_point['diff_coin_resp'] = -1
        elif int(row['diff_coin_resp']) > 0:
            data_point['diff_coin_resp'] = 1
        else:
            data_point['diff_coin_resp'] = int(row['diff_coin_resp'])
       
        #data_point['diff_coin_resp'] = int(row['diff_coin_resp'])
        #data_point['diff_coin_resp'] = int(row['coin_real_resp'])
        data_list.append(data_point) 


training_list = data_list[: int(0.7 * len(data_list))]
test_list     = data_list[int(0.7 * len(data_list)): ]


data_value = dict()
for key in training_list[0].keys():
    data_value[key] = []
    for data_point in training_list:
        data_value[key].append(data_point[key])

node_value = dict()
for node in node_states.keys():
    node_value[node] = np.array(data_value[node_states[node]['name']])

df_data = pd.DataFrame(node_value)   

test_data = dict()
for key in test_list[0].keys():
    test_data[key] = []
    for data_point in training_list:
        test_data[key].append(data_point[key])

test_value = dict()
for node in node_states.keys():
    test_value[node] = np.array(test_data[node_states[node]['name']])

df_test_data = pd.DataFrame(test_value)  


all_data_values = dict()
for key in data_list[0].keys():
    all_data_values[key] = []
    for data_point in data_list:
        all_data_values[key].append(data_point[key])


all_data = dict()
for node in node_states.keys():
    all_data[node] = np.array(all_data_values[node_states[node]['name']])

all_data = pd.DataFrame(all_data)  


