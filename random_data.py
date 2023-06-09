import numpy as np
import copy
from variables import *
# node_values = []

# for i in range(100):
#     data = dict()
#     for node in node_states.keys():
#         data[node] = np.random.choice(range(1, node_states[node] + 1))
#     node_values.append(data)

node_values = copy.deepcopy(node_states)
for node in node_states.keys():
    states = node_states[node]
    data = np.random.choice(range(1, states + 1), size= 5)
    node_values[node] = data

# data_list = []

# for node in node_values:
#     data_list.append(node_values[node])

# data_list = np.array(data_list)
# data_list = data_list.T

# node_data = list()
# for line in data_list:
#     data = dict()
#     for i in range(len(nodes)):
#         data[node] = 


# print(data_list)



