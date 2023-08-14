import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from factor_analyzer import FactorAnalyzer
from data import df_data
from factor_analyzer.factor_analyzer import calculate_bartlett_sphericity
from factor_analyzer.factor_analyzer import calculate_kmo



###################################### suitability of data for factor analysis
chi_square_value, p_value = calculate_bartlett_sphericity(df_data)
kmo_all,kmo_model=calculate_kmo(df_data)
# print('Bartlett analysis:\t', chi_square_value, p_value)
# print('KMO analysis:\t', kmo_all, kmo_model)

###################################### remove unimportant variables ##########################
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@ remove unimportant variables by correlation @@@@@@@@@@@@@@@@@@@#

overlap_rate = 0.5

from scipy.stats import pearsonr
# this computes the correlation coefficients
corr = df_data.corr(method=lambda x, y: pearsonr(x, y)[0]) 
# this computes the p-values
pvalues = df_data.corr(method=lambda x, y: pearsonr(x, y)[1]) - np.eye(len(df_data.columns)) 

corr = df_data.corr()
nodes = df_data.columns 
correlation_dict = dict()
for node in nodes:
    node_corr= corr[node]
    node_pvalue = pvalues[node]
    node_corr_dict = node_corr.to_dict()
    node_pvalue_dict = node_pvalue.to_dict()
    del node_corr_dict[node]
    max_corr_node = max(node_corr_dict, key=node_corr_dict.get)
    # print(node, 'is the most related with ', max_corr_node, 'by ', node_corr_dict[max_corr_node], ' p-value: ', node_pvalue_dict[max_corr_node])
    pattern_name1 = node + '@' + max_corr_node 
    pattern_name2 = max_corr_node + '@' + node
    if pattern_name1 in correlation_dict.keys() or pattern_name2 in correlation_dict.keys():
        continue
    correlation_dict[pattern_name1] = [node_corr_dict[max_corr_node], node_pvalue_dict[max_corr_node]]

import pprint
# pprint.pprint(correlation_dict)
# print('=======================================================================================')
sleected_correlation_dict = dict((k, v) for k, v in correlation_dict.items() if v[0] >= overlap_rate)
# pprint.pprint(sleected_correlation_dict)
overlap_variables = [x.split('@')[0] for x in sleected_correlation_dict.keys()]
# print(overlap_variables)


####### 2023.8.7 Li and Liu got [['Others_presence', 'Others_influence'], ['Average_sleeping_time', 'Sleeping_time'], ['Stress', 'Chronic_stress']]
####### we decide to delete  Others_presence, Average_sleeping_time, Chronic_stress


#@@@@@@@@@@@@@@@@@@@@@@@@@@@@ remove unimportant variables by data density @@@@@@@@@@@@@@@@@@@#

density_rate = 0.9

def density_calculation(data_list):
    data_items = set(data_list)
    density = dict()
    for item in data_items:
        density[item] = data_list.count(item) / len(data_list)
    return density

node_density_dict = dict()
for node in df_data.columns:
    density = density_calculation(df_data[node].tolist())
    node_density_dict[node] = density

sleected_density_dict = dict((k, v) for k, v in node_density_dict.items() if max(v.values()) >= density_rate)
# print(sleected_density_dict)
dense_variables = list(sleected_density_dict.keys())
# print(dense_variables)

####### 2023.8.7 Li and Liu got ['Indoor_outdoor', 'Location_nature', 'Accessory', 'Drunkenness']
####### we decide to delete 'Indoor_outdoor', 'Location_nature', 'Accessory', 'Drunkenness'

###################################### model the BBN edges ##########################

pvalue_rate = 0.05
correlation_rate = 0.2

from network import node_states
delete_variables = overlap_variables + dense_variables
for node in delete_variables:
    del node_states[node]
    del df_data[node]
    del corr[node]
    del pvalues[node]



relation_list = []
for node_i in corr.columns:
    for node_j in corr.columns:
        if node_i != node_j:
            if pvalues[node_i][node_j] < pvalue_rate and abs(corr[node_i][node_j]) > correlation_rate:
                # print(node_i, '@', node_j, corr[node_i][node_j], pvalues[node_i][node_j], '#' if pvalues[node_i][node_j] < 0.01 else '')
                if node_j + '@' + node_i in relation_list:
                    continue
                relation_list.append(node_i + '@' + node_j)

print('relation_list:\n', pprint.pprint(relation_list))


#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ need manual identification of the relations @@@@@@@@@@@@@@@@@@@@@@#

from pgmpy.estimators import BayesianEstimator
from pgmpy.inference import VariableElimination
from pgmpy.independencies import Independencies
from pgmpy.inference.EliminationOrder import WeightedMinFill
from pgmpy.models import BayesianNetwork
import numpy as np
from data import node_value

relation_dict = {
    'Time_zone': ['Location'],
    'Weekday': ['Location'],
    'Location': ['Others_influence'],
    'Shelter': ['Others_influence'],
    'Brightness': ['Others_influence'],
    'Others_influence': ['Cheating_indicator'],
    # 'Clothing_type': ['Clothing_color'],
    'Clothing_color': ['Cheating_indicator'],
    # 'Period': ['Weather'],
    'Weather': ['Amenity'],
    # 'Dinner': ['Full_stomach'],
    # 'Full_stomach': ['Thirst_degree'],
    'Thirst_degree': ['Amenity'],
    'Space_size':['Amenity'],
    # 'Color_Temperature': ['Subjective_temperature'],
    'Subjective_temperature': ['Cheating_indicator'],
    'Satisfaction_with_reward': ['Socioeconomic_level'],
    # 'Supplement': ['Medicine'],
    'Medicine': ['Health_Status'],
    'Drinking_habits': ['Health_Status'],
    'Health_Status': ['Socioeconomic_level'],
    'Socioeconomic_level': ['Cheating_indicator'],
    'Amenity': ['Stress'],
    'Stress': ['Cheating_indicator'],
    # 'Sleeping_time': ['Sleepiness'],
    'Sleepiness': ['Stress']
}

# Create a BayesianModel object
model = BayesianNetwork()

# Define the variables, Define the dependence

for node in relation_dict.keys():
    model.add_node(node)    
    for next_node in relation_dict[node]:
        model.add_edge(node, next_node)

# ############# network plot ################
# import networkx as nx
# import pylab as plt
# nx_graph = nx.DiGraph(model.edges())
# nx.draw(nx_graph, with_labels=True, pos=nx.spring_layout(nx_graph), width = 1, font_size = 2, arrowsize = 10, node_size=50, node_color = 'skyblue')
# plt.savefig("model.pdf")

data_dict = dict()

for node in model.nodes:
    data_dict[node] = node_value[node]

data = pd.DataFrame(data=data_dict)
model.fit(data, estimator=BayesianEstimator, prior_type="BDeu") # default equivalent_sample_size=5
# for cpd in model.get_cpds():
#     print(cpd)

# chi_square_value, p_value = calculate_bartlett_sphericity(data)
# kmo_all,kmo_model=calculate_kmo(data)
# print('Bartlett analysis:\t', chi_square_value, p_value)
# print('KMO analysis:\t', kmo_all, kmo_model)

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


from data import df_test_data

test_data = dict()
for node in model.nodes:
    test_data[node] = df_test_data[node]

total_test_num = df_test_data.shape[0]
correct_num = 0

for i in range(df_test_data.shape[0]):
    data_point = dict()
    for node in model.nodes:
        if node == 'Cheating_indicator':
            continue
        data_point[node] = test_data[node][i]
    query = infer.query(variables=['Cheating_indicator'], evidence=data_point)
    probs, states = zip(*sorted(zip(query.values.tolist(), query.state_names["Cheating_indicator"])))
    if states[-1] == test_data["Cheating_indicator"][i]:
        correct_num += 1

print("Our BBN model exhibits {} accuracy.".format(correct_num / total_test_num))
