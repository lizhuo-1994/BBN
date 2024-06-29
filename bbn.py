import os, sys
import re, datetime
from network import node_states
import numpy as np
from data import all_data
from sklearn.cluster import KMeans
import pandas as pd
from pgmpy.estimators import BayesianEstimator
from pgmpy.inference import VariableElimination
from pgmpy.independencies import Independencies
from pgmpy.inference.EliminationOrder import WeightedMinFill
from pgmpy.models import BayesianNetwork


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

abstract_all_values = dict()
for snode in abstract_states.keys():

    # min_state = np.array([0 for i in abstract_states[snode]['variables']])
    # max_state = np.array([i for i in abstract_states[snode]['value_states']])

    # grid_num = 2
    # grid = Grid(min_state, max_state, grid_num)  
    
    data = all_data[abstract_states[snode]['variables']]
    data = data.to_numpy()
    # state_ids = grid.state_abstract(data)

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

from sklearn.model_selection import train_test_split

train, test = train_test_split(abstract_all_values, test_size=0.3, random_state=0)
#################################################### build model ##################################


# Create a BayesianModel object
model1 = BayesianNetwork()
model2 = BayesianNetwork()

# Define the variables, Define the dependence

for snode in abstract_states.keys():
    model1.add_node(snode)    
    model1.add_edge(snode, 'Cheating_indicator')


for snode in abstract_states.keys():
    model2.add_node(snode)    
model2.add_edge('Time and Environmental Factors', 'Social Interaction Factors')
model2.add_edge('Social Interaction Factors', 'Cheating_indicator')
model2.add_edge('Sleeping Pattern Factors', 'Environmental Comfort and Personal Perception Factors')
model2.add_edge('Health Status Factors', 'Environmental Comfort and Personal Perception Factors')
model2.add_edge('Personal Habits and Environment Interaction Factors', 'Environmental Comfort and Personal Perception Factors')
model2.add_edge('Dietary and Satiety Factors', 'Environmental Comfort and Personal Perception Factors')
model2.add_edge('Environmental Comfort and Personal Perception Factors', 'Cheating_indicator')
model2.add_edge('Personal Dressing Factors', 'Cheating_indicator')

# ############# network plot ################
# import networkx as nx
# import pylab as plt
# nx_graph = nx.DiGraph(model.edges())
# nx.draw(nx_graph, with_labels=True, pos=nx.spring_layout(nx_graph), width = 1, font_size = 2, arrowsize = 10, node_size=50, node_color = 'skyblue')
# plt.savefig('model.pdf')

model1.fit(train, estimator=BayesianEstimator, prior_type="BDeu") # default equivalent_sample_size=5
model2.fit(train, estimator=BayesianEstimator, prior_type="BDeu") # default equivalent_sample_size=5


model = model2

############# inference ################
infer = VariableElimination(model)
# query = infer.query(variables=['Space_size'], evidence={'Cheating_indicator': 1})
# print(query)

def mutual_information(variable1, variable2):
    query1 = infer.query(variables=[variable1], joint=True)
    query2 = infer.query(variables=[variable2], joint=True)
    query_joint = infer.query(variables=[variable1, variable2], joint=True)
    p_variable1 = query1.values
    p_variable2 = query2.values
    p_joint = query_joint.values

    mi = 0
    for i in range(len(p_variable1)):
        for j in range(len(p_variable2)):
            mi += p_joint[i,j] * np.log(p_joint[i,j] / (p_variable1[i] * p_variable2[j]))
    return mi

# print('the mutual information between Space_size and Cheating_indicator', mutual_information('Space_size', 'Cheating_indicator'))
# print('the mutual information between Chronic_stress and Cheating_indicator', mutual_information('Chronic_stress', 'Cheating_indicator'))
# print('the mutual information between Amenity and Cheating_indicator', mutual_information('Amenity', 'Cheating_indicator'))

mutual_info_list = []
mutual_node_list = []
for node in model.nodes():
    if node == 'Cheating_indicator':
        continue
    mutual_info = mutual_information(node, 'Cheating_indicator')
    mutual_node_list.append(node)
    mutual_info_list.append(mutual_info)

mutual_info_list, mutual_node_list = zip(*sorted(zip(mutual_info_list, mutual_node_list)))

for node, mutual_info in zip(mutual_node_list, mutual_info_list):
    print('mutual information==>\t', node, ':\t', mutual_info)


################### cross validation################
total_test_num = test.shape[0]
correct_num = 0

for i in range(test.shape[0]):
    data_point = dict()
    for node in model.nodes:
        if node == 'Cheating_indicator':
            continue
        data_point[node] = test[node].values[i]
    query = infer.query(variables=['Cheating_indicator'], evidence=data_point)
    probs, states = zip(*sorted(zip(query.values.tolist(), query.state_names["Cheating_indicator"])))
    predict = states[-1]
    target = test["Cheating_indicator"].values[i]
    print(predict, target)
    # if abs(predict - target) <= 6:
    if predict == target:
        correct_num += 1

print("Our BBN model exhibits {} accuracy.".format(correct_num / total_test_num))

    


