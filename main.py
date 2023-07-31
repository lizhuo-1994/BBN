from pgmpy.estimators import BayesianEstimator
from pgmpy.inference import VariableElimination
from pgmpy.independencies import Independencies
from pgmpy.inference.EliminationOrder import WeightedMinFill
import numpy as np

from data import node_value
from network import model
import pandas as pd

############# Build the network from data ################
data = pd.DataFrame(data=node_value)
model.fit(data, estimator=BayesianEstimator, prior_type="BDeu") # default equivalent_sample_size=5
# for cpd in model.get_cpds():
#     print(cpd)

print(model.check_model())



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

############# network plot ################
import networkx as nx
import pylab as plt
nx_graph = nx.DiGraph(model.edges())
nx.draw(nx_graph, with_labels=True, pos=nx.spring_layout(nx_graph), width = 1, font_size = 10, arrowsize = 10, node_size=500, node_color = 'skyblue')
plt.savefig("model.png")