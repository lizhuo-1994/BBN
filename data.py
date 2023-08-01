import numpy as np
import copy
import csv
import json
from network import node_states
import scipy.stats as stats
import pandas as pd
import pingouin as pg


data_list = []
with open('data.csv','rt') as f: 
    cr = csv.DictReader(f)
    for row in cr:
        data_point = dict()
        for i in range(1, 37):
            data_point['Q' + str(i)] = int(row['Q' + str(i)])
        data_point['diff_coin_resp'] = int(row['coin_real_resp'])
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
    


# for node in node_states.keys():
#     if node == 'Cheating_indicator':
#         continue
#     print(node, '- Cheating_indicator:')
#     # print(data_value[node_states[node]['name']])
#     # print(data_value['diff_coin_resp'])
#     print('kendalltau:\t', stats.kendalltau(data_value[node_states[node]['name']], data_value['diff_coin_resp']))
#     print('pearsonr:\t', stats.pearsonr(data_value[node_states[node]['name']], data_value['diff_coin_resp']))
#     print('spearmanr:\t', stats.spearmanr(data_value[node_states[node]['name']], data_value['diff_coin_resp']))
#     print('==================================================================')

df = pd.DataFrame(node_value)   
for node_i in node_value.keys():
    for node_j in node_value.keys():
        if node_i != node_j and node_i != 'Cheating_indicator' and node_j != 'Cheating_indicator':
            print(node_i + '+' + node_j, '->', 'Cheating_indicator:')
            print(pg.partial_corr(data=df, x=[node_i, node_j], y='Cheating_indicator', method='pearson'))
            print(pg.partial_corr(data=df, x=[node_i, node_j], y='Cheating_indicator', method='spearman'))
            print('==================================================================')

