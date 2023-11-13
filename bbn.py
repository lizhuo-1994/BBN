import os, sys
import re, datetime
from network import node_states
import numpy as np
from data import all_data
from sklearn.cluster import KMeans
import pandas as pd

class AbstractModel():
    def __init__(self):
        self.initial = []
        self.final = []

class Grid(AbstractModel):
    '''
    Multiple DTMCs from a set of sets of traces
    traces: a set of sets of traces
    '''
    def __init__(self, min_val, max_val, grid_num, clipped=True):
        super().__init__()
        self.min = min_val
        self.max = max_val
        self.k = grid_num
        self.dim = max_val.shape[0]
        self.total_states = pow(grid_num,self.dim)
        self.unit = (max_val - min_val) / self.k
        self.clipped = clipped
        
    def state_abstract(self, con_states):
        con_states = con_states
        lower_bound = self.min
        upper_bound = self.max
        unit = (upper_bound - lower_bound)/self.k
        abs_states = np.zeros(con_states.shape[0],dtype=np.int8)
        
        #print(lower_bound)
        #print(upper_bound)
        indixes = np.where(unit == 0)[0]
        unit[indixes] = 1
        #print('unit:\t', unit)
        
        tmp = ((con_states-self.min)/unit).astype(int)
        if self.clipped:
            tmp = np.clip(tmp, 0, self.k-1)
            
        dims = tmp.shape[1]
        for i in range(dims):
            abs_states = abs_states + tmp[:,i]*pow(self.k, i)
#         abs_states = np.expand_dims(abs_states,axis=-1)
        abs_states = [str(item) for item in abs_states]
        return abs_states

groups = [
    ['Q1', 'Q2', 'Q3', 'Q16'],
    ['Q4', 'Q5', 'Q6', 'Q8', 'Q9', 'Q19', 'Q20', 'Q24', 'Q25'],
    ['Q7', 'Q12', 'Q13', 'Q14', 'Q15', 'Q28', 'Q30', 'Q31', 'Q33', 'Q34', 'Q35', 'Q36'], 
    ['Q10', 'Q11'],
    ['Q17', 'Q18'],
    ['Q21', 'Q22', 'Q23'],
    ['Q26', 'Q27'],
    ['Q29', 'Q32']
]


group_names = []
value_scales = []
for group in groups:
    group_name = []
    value_scale = []
    for node in node_states.keys():
        if node_states[node]['name'] in group:
            group_name.append(node)
            value_scale.append(node_states[node]['states'])
    group_names.append(group_name)
    value_scales.append(value_scale)


abstract_states = {
    'Time and Environmental Factors': {
        'variables': group_names[0],
        'value_states': value_scales[0],
        'clusters': 4
    },
    'Personal Habits and Environment Interaction Factors': {
        'variables': group_names[1],
        'value_states': value_scales[1],
        'clusters': 5
    },
    'Environmental Comfort and Personal Perception Factors': {
        'variables': group_names[2],
        'value_states': value_scales[2],
        'clusters': 8
    },
    'Social Interaction Factors': {
        'variables': group_names[3],
        'value_states': value_scales[3],
        'clusters': 2
    },
    'Personal Dressing Factors': {
        'variables': group_names[4],
        'value_states': value_scales[4],
        'clusters': 2
    },
    'Health Status Factors': {
        'variables': group_names[5],
        'value_states': value_scales[5],
        'clusters': 4
    },
    'Sleeping Pattern Factors': {
        'variables': group_names[6],
        'value_states': value_scales[6],
        'clusters': 4
    },
    'Dietary and Satiety Factors': {
        'variables': group_names[7],
        'value_states': value_scales[7],
        'clusters': 4
    },
}

print(abstract_states)



abstract_all_values = dict()
for snode in abstract_states.keys():

    min_state = np.array([0 for i in abstract_states[snode]['variables']])
    max_state = np.array([i for i in abstract_states[snode]['value_states']])

    grid_num = 2
    grid = Grid(min_state, max_state, grid_num)  
    
    data = all_data[abstract_states[snode]['variables']]
    data = data.to_numpy()
    state_ids = grid.state_abstract(data)

    # print(len(state_ids), len(set(state_ids)))
    # unique, counts = np.unique(state_ids, return_counts=True)
    # counts, unique = zip(*sorted(zip(counts, unique), reverse=True))
    # print(unique, counts)


    clustering = KMeans(n_clusters=abstract_states[snode]['clusters'], random_state=0, n_init="auto").fit(data)
    unique, counts = np.unique(clustering.labels_, return_counts=True)
    print(unique, counts)

    abstract_all_values[snode] = clustering.labels_


abstract_all_values['Cheating_indicator'] = all_data['Cheating_indicator']
abstract_all_values = pd.DataFrame(abstract_all_values)  
print(abstract_all_values)



    


