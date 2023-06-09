from pgmpy.factors.discrete import TabularCPD
from pgmpy.estimators import BayesianEstimator
from pgmpy.inference import VariableElimination
from pgmpy.independencies import Independencies
from pgmpy.inference.EliminationOrder import WeightedMinFill
from sklearn.metrics.pairwise import cosine_similarity

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

query = infer.query(variables=['Space_Size', 'Cheating_Indicator'], joint=True)
print(query)
print(cosine_similarity([query.values[0]], [query.values[1]]))

query = infer.query(variables=['Satisfaction_with_Reward', 'Cheating_Indicator'], joint=True)
print(query)
print(cosine_similarity([query.values[0]], [query.values[1]]))

query = infer.query(variables=['Season', 'Cheating_Indicator'], joint=True)
print(query)
print(cosine_similarity([query.values[0]], [query.values[1]]))




# import networkx as nx
# import pylab as plt
# nx_graph = nx.DiGraph(model.edges())
# nx.draw(nx_graph, with_labels=True, pos=nx.spring_layout(nx_graph), width = 1, font_size = 10, arrowsize = 10, node_size=500, node_color = 'skyblue')
# plt.show()