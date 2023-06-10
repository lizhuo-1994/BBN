from pgmpy.estimators import BayesianEstimator
from pgmpy.inference import VariableElimination
from pgmpy.independencies import Independencies
from pgmpy.inference.EliminationOrder import WeightedMinFill
import numpy as np
from variables import nodes
from random_data import node_values
from network import model
import pandas as pd


data = pd.DataFrame(data=node_values)
model.fit(data, estimator=BayesianEstimator, prior_type="BDeu") # default equivalent_sample_size=5
for cpd in model.get_cpds():
    print(cpd)

print(model.check_model())



############# inference ################
infer = VariableElimination(model)
query = infer.query(variables=['Cheating_Indicator'], evidence={'Satisfaction_with_Reward': 1, 'Subjective_Stress_Level': 2})
print(query)
query = infer.query(variables=['Cheating_Indicator'], evidence={'Space_Size': 1})
print(query)


############# Variables Estimation ################
print(WeightedMinFill(model).get_elimination_order(model.nodes))

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


query = infer.query(variables=['Space_Size'], joint=True)
print(query)
print(query.values)

query = infer.query(variables=['Cheating_Indicator'], joint=True)
print(query)
print(query.values)

query = infer.query(variables=['Space_Size', 'Cheating_Indicator'], joint=True)
print(query)
print(query.values)

print('the mutual information between Space_Size and Cheating_Indicator', mutual_information('Space_Size', 'Cheating_Indicator'))
print('the mutual information between Satisfaction_with_Reward and Cheating_Indicator', mutual_information('Satisfaction_with_Reward', 'Cheating_Indicator'))
print('the mutual information between Season and Cheating_Indicator', mutual_information('Season', 'Cheating_Indicator'))

for node in model.nodes():
    if node == 'Cheating_Indicator':
        continue
    print('the mutual information between {0} and Cheating_Indicator'.format(node), mutual_information(node, 'Cheating_Indicator'))

import networkx as nx
import pylab as plt
nx_graph = nx.DiGraph(model.edges())
nx.draw(nx_graph, with_labels=True, pos=nx.spring_layout(nx_graph), width = 1, font_size = 10, arrowsize = 10, node_size=500, node_color = 'skyblue')
plt.show()