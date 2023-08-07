import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from factor_analyzer import FactorAnalyzer
from data import df_data
from factor_analyzer.factor_analyzer import calculate_bartlett_sphericity
from factor_analyzer.factor_analyzer import calculate_kmo


####################################### load data ##############################
print(df_data.shape)


###################################### suitability of data for factor analysis
chi_square_value, p_value = calculate_bartlett_sphericity(df_data)
kmo_all,kmo_model=calculate_kmo(df_data)
print('Bartlett analysis:\t', chi_square_value, p_value)
print('KMO analysis:\t', kmo_all, kmo_model)


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
print('=======================================================================================')
sleected_correlation_dict = dict((k, v) for k, v in correlation_dict.items() if v[0] >= overlap_rate)
pprint.pprint(sleected_correlation_dict)
overlap_variables = [x.split('@')[0] for x in sleected_correlation_dict.keys()]
print(overlap_variables)


####### 2023.8.7 Li and Liu got [['Weekday', 'Time_zone'], ['Others_presence', 'Others_influence'], ['Average_sleeping_time', 'Sleeping_time'], ['Stress', 'Chronic_stress']]
####### we decide to delete Weekday, Others_presence, Average_sleeping_time, Chronic_stress


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
print(sleected_density_dict)
dense_variables = list(sleected_density_dict.keys())
print(dense_variables)

####### 2023.8.7 Li and Liu got ['Indoor_outdoor', 'Location_nature', 'Accessory', 'Drunkenness']
####### we decide to delete 'Indoor_outdoor', 'Location_nature', 'Accessory', 'Drunkenness'

###################################### model the BBN ##########################
from network import node_states
from pgmpy.estimators import BayesianEstimator
from pgmpy.inference import VariableElimination
from pgmpy.independencies import Independencies
from pgmpy.inference.EliminationOrder import WeightedMinFill
from pgmpy.models import BayesianNetwork
import numpy as np

delete_variables = overlap_variables + dense_variables
for node in delete_variables:
    del node_states[node]
    del df_data[node]


print(len(node_states), df_data.shape)


# Create a BayesianModel object
model = BayesianNetwork()

# Define the variables, Define the dependence

for node in node_states.keys():
    model.add_node(node)    
    for next_node in node_states[node]['next_nodes']:
        if next_node in delete_variables:
            continue
        model.add_edge(node, next_node)

model.fit(df_data, estimator=BayesianEstimator, prior_type="BDeu") # default equivalent_sample_size=5
# for cpd in model.get_cpds():
#     print(cpd)

print(model.check_model())
